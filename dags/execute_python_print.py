from airflow.utils.dates import days_ago
from airflow import DAG

from airflow.operators.python_operator import PythonOperator

default_args = {
    'owner': 'soohian',
}

def print_hello(name):
    print(f"Hello {name}!")

def print_goodbye(name, city):
    print(f"Goodbye {name} from {city}!")

with DAG(
    dag_id='execute_python_print',
    description='Execute Python Print',
    default_args=default_args,
    start_date=days_ago(1),
    schedule_interval="@once",
    tags = ['beginner', 'python', 'print']
) as dag:
    
    taskA = PythonOperator(
        task_id='print_hello',
        python_callable=print_hello,
        op_kwargs={'name': 'Soohian'}

    )

    taskB = PythonOperator(
        task_id='print_goodbye',
        python_callable=print_goodbye,
        op_kwargs={'name': 'Soohian', 'city': 'Singapore'}
    )

taskA >> taskB