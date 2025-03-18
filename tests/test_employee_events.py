import pytest
from pathlib import Path
from sqlite3 import connect

# Using pathlib create a project_root variable set to the absolute path for the root of this project
project_root = Path(__file__).resolve().parent

# Apply the pytest fixture decorator to a `db_path` function
@pytest.fixture
def db_path():
    return project_root / 'employee_events.db'

# Define a function called `test_db_exists`
# This function should receive an argument with the same name as the function that creates the "fixture" for the database's filepath
def test_db_exists(db_path):
    assert db_path.is_file(), "Database file does not exist."

# Fixture to provide a database connection
@pytest.fixture
def db_conn(db_path):
    conn = connect(db_path)
    yield conn
    conn.close()

# Fixture to provide the list of table names from the database
@pytest.fixture
def table_names(db_conn):
    name_tuples = db_conn.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
    return [x[0] for x in name_tuples]

# Define a test function called `test_employee_table_exists`
# This function should receive the `table_names` fixture as an argument
def test_employee_table_exists(table_names):
    assert 'employee' in table_names, "Employee table does not exist."

# Define a test function called `test_team_table_exists`
# This function should receive the `table_names` fixture as an argument
def test_team_table_exists(table_names):
    assert 'team' in table_names, "Team table does not exist."

# Define a test function called `test_employee_events_table_exists`
# This function should receive the `table_names` fixture as an argument
def test_employee_events_table_exists(table_names):
    assert 'employee_events' in table_names, "Employee_events table does not exist."