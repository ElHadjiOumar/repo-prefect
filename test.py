# Importing Prefect dependencies
from prefect import flow, task
from prefect.task_runners import SequentialTaskRunner

# Importing Airbyte dependencies
from prefect_airbyte.server import AirbyteServer
from prefect_airbyte.connections import AirbyteConnection
from prefect_airbyte.flows import run_connection_sync

# Importing DBT dependencies
from prefect_dbt.cli.commands import DbtCoreOperation

# Initialize AirbyteServer
server = AirbyteServer.load("airbyte-server")

# Load Airbyte Connections
airbyte_connection_bordeaux = AirbyteConnection.load("airbyte-connection-bordeaux", validate=False)
airbyte_connection_montreal = AirbyteConnection.load("airbyte-connection-montreal", validate=False)
airbyte_connection_paris = AirbyteConnection.load("airbyte-connection-paris", validate=False)
airbyte_connection_rennes = AirbyteConnection.load("airbyte-connection-rennes", validate=False)
   

# Define DBT task
@task
def dbt_task():
    result = DbtCoreOperation(
        commands=["dbt run --models onepointparis onepointrennes onepointbordeaux onepointmontreal --target dev","dbt run --models bordeauxsilver montrealsilver parissilver rennessilver --target silver","dbt run --models weathergold weathergold2 --target gold"],
        project_dir=r"./dbt_code",
        profiles_dir=r"./dbt_code",
    )
    return result.run()

# Create a Prefect Flow
# with Flow('combined_flow') as flow:
@flow(task_runner=SequentialTaskRunner())
def flow_combo():
    run_connection_sync(airbyte_connection_bordeaux)
    run_connection_sync(airbyte_connection_montreal)
    run_connection_sync(airbyte_connection_paris)
    run_connection_sync(airbyte_connection_rennes)
    dbt_task.submit()
    

if __name__ == "__main__":
    flow_combo()
