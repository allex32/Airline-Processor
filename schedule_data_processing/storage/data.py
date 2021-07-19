import os

import pandas as pd

from azure.storage.blob import BlobClient
from schedule_data_processing.configuration.app_configuration import AppConfiguration

SCHEDULE = None
FLEET = None
AIRPORTS = None

def cleanup_temp_file(file):
    if os.path.exists(file):
        os.remove(file)


def get_file(pd_read, blob_name):
    config = AppConfiguration()
    blob = BlobClient.from_connection_string(conn_str=config.blob_connection_string,
                                             container_name=config.blob_container_name,
                                             blob_name=blob_name)
    with open(blob_name, "wb") as f:
        blob.download_blob().readinto(f)

    df = pd_read(blob_name)
    cleanup_temp_file(blob_name)

    return df


def get_schedule():
    config = AppConfiguration()
    global SCHEDULE
    SCHEDULE = get_file(pd.read_json, config.schedule_blob_name)
    return SCHEDULE


def get_fleet():
    config = AppConfiguration()
    global FLEET
    FLEET = get_file(pd.read_csv, config.fleet_blob_name)
    return FLEET


def get_airports():
    config = AppConfiguration()
    global AIRPORTS
    AIRPORTS = get_file(pd.read_csv, config.airports_blob_name)
    return AIRPORTS


def get_data():
    get_schedule()
    get_airports()
    get_fleet()
