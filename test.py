# Importation de flow
from prefect import flow

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

@flow(name="flow_airbyte2")
def airbyte_syncs():
    run_connection_sync(airbyte_connection_bordeaux)

    run_connection_sync(airbyte_connection_montreal)

    run_connection_sync(airbyte_connection_paris)

    run_connection_sync(airbyte_connection_rennes)

@flow(name="flow_dbt")
def dbt_flow() -> str:
    result = DbtCoreOperation(
        commands=["dbt run --models onepointparis onepointrennes onepointbordeaux onepointmontreal --target dev"],
        project_dir=r"./dbt_code",
        profiles_dir=r"./dbt_code",
    )
    return result.run()

if __name__ == "__main__":
    airbyte_syncs()


