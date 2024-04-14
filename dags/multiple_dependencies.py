from datetime import datetime, timedelta
from airflow.utils.dates import days_ago
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'soohian',
}

with DAG(
    dag_id='multiple_dependencies',
    description='Multiple Dependencies',
    default_args=default_args,
    start_date=days_ago(1),
    schedule_interval=timedelta(days=1),
    tags = ['beginner', 'bash', 'multiple dependencies']

) as dag:
    
    taskA = BashOperator(
        task_id='taskA',
        bash_command='''
                echo Starting task A
                for i in {1..10}
                do
                    echo TASK A printing $i
                done
                echo Task A completed
            '''
            )
    
    taskB = BashOperator(
        task_id='taskB',
        bash_command='''
                echo Starting task B
                sleep 4
                echo Task B completed
            '''
            )
    
    taskC = BashOperator(
        task_id='taskC',
        bash_command='''
                echo Starting task C
                sleep 4
                echo Task C completed
            '''
            )
    
    taskD = BashOperator(
        task_id='taskD',
        bash_command='''
                echo Task D completed
            '''
            )
    
taskA >> [taskB, taskC] >> taskD
# [taskB, taskC] >> taskD
