# Importation de flow
from prefect import Flow,task

# Importation des dépendances de airbyte
from prefect_airbyte.server import AirbyteServer
from prefect_airbyte.connections import AirbyteConnection
from prefect_airbyte.flows import run_connection_sync

# Importation des dependances de DBT 
from prefect_dbt.cli.commands import DbtCoreOperation

server = AirbyteServer.load("airbyte-server")

airbyte_connection_bordeaux = AirbyteConnection.load("airbyte-connection-bordeaux",validate=False)
airbyte_connection_montreal = AirbyteConnection.load("airbyte-connection-montreal",validate=False)
airbyte_connection_paris = AirbyteConnection.load("airbyte-connection-paris",validate=False)
airbyte_connection_rennes = AirbyteConnection.load("airbyte-connection-rennes",validate=False)

@task
def airbyte_task():
    run_connection_sync(airbyte_connection_bordeaux)

    run_connection_sync(airbyte_connection_montreal)

    run_connection_sync(airbyte_connection_paris)

    run_connection_sync(airbyte_connection_rennes)

@task
def dbt_task() -> str:
    result = DbtCoreOperation(
        commands=["dbt run --models onepointparis onepointrennes onepointbordeaux onepointmontreal --target dev"],
        project_dir=r"./dbt_code",
        profiles_dir=r"./dbt_code",
    )
    return result.run()

with Flow("flow_combo") as flow_combo:
    airbyte_result = airbyte_task()
    dbt_result = dbt_task()
    dbt_result.set_upstream(airbyte_result)

if __name__ == "__main__":
    flow_combo.run()


