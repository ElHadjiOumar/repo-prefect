# Importation de flow
from prefect import flow

# Importation des dependances de airbyte 
from prefect_airbyte.server import AirbyteServer
from prefect_airbyte.connections import AirbyteConnection
from prefect_airbyte.flows import run_connection_sync

# Importation des dependances de DBT 
from prefect_dbt.cli import DbtCliProfile, DbtCoreOperation

# Import les dependances pour deployer et schedules notre code
from prefect.deployments import run_deployment
from prefect.deployments import Deployment
from prefect.server.schemas.schedules import CronSchedule
from prefect.filesystems import GitHub
import os
import asyncio
from prefect import flow
from prefect_azure import AzureBlobStorageCredentials
from prefect_azure.blob_storage import blob_storage_download


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

# azure_credentials_block = AzureBlobStorageCredentials.load("azureblobmdp")

# azure_credentials_block = AzureBlobStorageCredentials.load("blopblockstorage")
# blob_service_client = azure_credentials_block.get_blob_client("blobmdp", "test-folder")



# deploiement_airbyte = Deployment.build_from_flow(
#     flow= airbyte_syncs,
#     name= "cron_airflow",
#     work_queue_name="default",
#     storage=blob_service_client,
#     schedule=(CronSchedule(cron="*/3 * * * *", timezone="Europe/Paris"))
# )
# deploiement_airbyte.apply()

# def main_airflow():
#     run_deployment(name="flow_airbyte/cron_airflow")


if __name__ == "__main__":
    #main_airflow()
    airbyte_syncs()
    # main_dbt()


