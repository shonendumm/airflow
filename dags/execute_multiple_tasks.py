from airflow.utils.dates import days_ago
from airflow import DAG
from airflow.operators.bash import BashOperator


default_args = {
    'owner': 'soohian',
}


with DAG(
    dag_id='execute_multiple_tasks',
    description='Execute Multiple Tasks',
    default_args=default_args,
    start_date=days_ago(1),
    schedule_interval="@once",
    tags = ['beginner', 'bash', 'multiple tasks']

) as dag:
    
    taskA = BashOperator(
        task_id='taskA',
        bash_command='echo "This is task A 2"'
    )
    
    taskB = BashOperator(
        task_id='taskB',
        bash_command='echo "This is task B 2"'
    )

# To indicate that taskB should run after taskA, you can use the bitshift operator >> to set the downstream dependency.
taskA >> taskB
# taskA.set_downstream(taskB) # execute taskB after taskA
# taskA.set_upstream(taskB) # execute taskA after taskB