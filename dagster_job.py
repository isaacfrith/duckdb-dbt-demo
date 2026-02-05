import os
from dagster import ScheduleDefinition, Definitions, define_asset_job, AssetSelection
# IMPORT DbtCliResource here
from dagster_dbt import DbtProject, dbt_assets, DbtCliResource

# 1. Point to your existing dbt project
dbt_project = DbtProject(
    project_dir=os.getcwd(),
)

# This generates the manifest.json automatically if it doesn't exist
dbt_project.prepare_if_dev()

# 2. Load dbt models
# Note: We use the 'DbtCliResource' type hint here so Dagster knows it's a resource
@dbt_assets(manifest=dbt_project.manifest_path)
def jaffle_shop_dbt_assets(context, dbt: DbtCliResource):
    yield from dbt.cli(["build"], context=context).stream()

# 3. Define a job
run_dbt_job = define_asset_job(
    name="run_dbt_job",
    selection=AssetSelection.all()
)

# 4. Schedule it (e.g., Run at midnight)
daily_schedule = ScheduleDefinition(
    job=run_dbt_job,
    cron_schedule="0 0 * * *",
)

# 5. Definitions
defs = Definitions(
    assets=[jaffle_shop_dbt_assets],
    schedules=[daily_schedule],
    resources={
        # The resource must be an instance of DbtCliResource, not just the project path
        "dbt": DbtCliResource(project_dir=dbt_project),
    },
)