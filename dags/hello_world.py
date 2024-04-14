from datetime import datetime, timedelta
from airflow.utils.dates import days_ago

from airflow import DAG

from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'soohian',
}


# dag1 = DAG(
#     dag_id='hello_world_dag',
#     description='Hello World DAG',
#     default_args=default_args,
#     start_date=days_ago(1),
#     schedule_interval="@daily",
#     tags = ['beginner', 'bash', 'hello world']
# )

# task1 = BashOperator(
#     task_id='hello_world_task',
#     bash_command='echo "Hello World once again!"',
#     dag=dag1
# )

with DAG(
    dag_id='hello_world_dag',
    description='Hello World DAG',
    default_args=default_args,
    start_date=days_ago(1),
    schedule_interval="@daily",
    tags = ['beginner', 'bash', 'hello world']
) as dag:
    task = BashOperator(
        task_id='hello_world_task',
        bash_command='echo "Hello World again!"'
    )

# indicates that this is the only task with no dependency
task