import os
import sys

# Ensure src directory is on PYTHONPATH for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from pipelines.dags.dummy_dag import dag, DAG


def test_dag_loaded():
    assert dag, "DAG should be loaded"  # nosec
    assert isinstance(dag, DAG), "DAG should be instance of DAG"  # nosec


def test_tasks_present():
    task_ids = set(dag.task_dict.keys())
    assert task_ids == {"print_date", "hello_task"}, f"Expected tasks {{'print_date','hello_task'}}, got {task_ids}"  # nosec


def test_dependencies():
    downstream = dag.task_dict["print_date"].downstream_task_ids
    upstream = dag.task_dict["hello_task"].upstream_task_ids
    assert downstream == {"hello_task"}, f"print_date should be upstream of hello_task, got downstream {downstream}"  # nosec
    assert upstream == {"print_date"}, f"hello_task should have upstream print_date, got upstream {upstream}"  # nosec


def test_default_args():
    defaults = dag.default_args
    assert defaults.get("owner") == "airflow", "Owner in default_args should be 'airflow'"  # nosec
    assert not defaults.get("depends_on_past"), "depends_on_past should be False"  # nosec
    assert defaults.get("retries") == 1, "retries should be 1"  # nosec


def test_schedule_and_catchup():
    assert dag.schedule_interval == "@daily", f"Expected schedule_interval '@daily', got {dag.schedule_interval}"  # nosec
    assert not dag.catchup, f"Expected catchup False, got {dag.catchup}"  # nosec
