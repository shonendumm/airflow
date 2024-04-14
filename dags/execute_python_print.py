from airflow.utils.dates import days_ago
from airflow import DAG

from airflow.operators.python_operator import PythonOperator

default_args = {
    'owner': 'soohian',
}

with DAG(
    dag_id='execute_python_print',
    description='Execute Python Print',
    default_args=default_args,
    start_date=days_ago(1),
    schedule_interval="@once",
    tags = ['beginner', 'python', 'print']
) as dag:
    
    def print_hello():
        print("Hello Soohian!")
    
    task = PythonOperator(
        task_id='print_hello',
        python_callable=print_hello
    )

task