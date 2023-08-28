# Importation de flow
from prefect import flow

# Importation des dépendances de airbyte
from prefect_airbyte.server import AirbyteServer
from prefect_airbyte.connections import AirbyteConnection
from prefect_airbyte.flows import run_connection_sync

server = AirbyteServer.load("airbyte-server")

airbyte_connection_bordeaux = AirbyteConnection.load("airbyte-connection-bordeaux",validate=False)
airbyte_connection_montreal = AirbyteConnection.load("airbyte-connection-montreal",validate=False)
airbyte_connection_paris = AirbyteConnection.load("airbyte-connection-paris",validate=False)
airbyte_connection_rennes = AirbyteConnection.load("airbyte-connection-rennes",validate=False)

@flow(name="flow_airbyte")
def airbyte_syncs():
    run_connection_sync(airbyte_connection_bordeaux)

    run_connection_sync(airbyte_connection_montreal)

    run_connection_sync(airbyte_connection_paris)

    run_connection_sync(airbyte_connection_rennes)

if __name__ == "__main__":
    airbyte_syncs()


