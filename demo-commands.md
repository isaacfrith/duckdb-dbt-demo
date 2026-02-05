list all files: ls -la

mac installation of python version: brew install python@3.11

create virtual environment using python version 3.11: /opt/homebrew/bin/python3.11 -m venv venv

activate virtual environment: source venv/bin/activate

check python version: python --version

upgrade pip: python3 -m pip install --upgrade pip

instlall requirement files: python3 -m pip install -r requirements.txt


DBT commands

dbt seed

dbt compile

dbt run

dbt test

dbt build

dbt docs generate

dbt docs serve -> http://localhost:8080

dagster

touch dagster_job.py

dbt parse

dagster dev -f dagster_job.py   
