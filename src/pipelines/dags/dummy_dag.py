from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

# Default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2025, 7, 8),  # Adjust to today's date or earlier
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
with DAG(
    'dummy_test_dag',
    default_args=default_args,
    description='A simple dummy DAG for testing',
    schedule='@daily',  # or use timedelta(days=1)
    catchup=False,
) as dag:

    # Task 1: Print the current date
    print_date = BashOperator(
        task_id='print_date',
        bash_command='date',
    )

    # Task 2: Simple Python task
    def print_hello():
        print('Hello world from Airflow!')

    hello_task = PythonOperator(
        task_id='hello_task',
        python_callable=print_hello,
    )

    # Define task dependencies
    print_date >> hello_task
