import os

import pandas as pd

from azure.storage.blob import BlobClient
from schedule_data_processing.configuration.app_configuration import AppConfiguration


def cleanup_temp_file(file):
    if os.path.exists(file):
        os.remove(file)


class AzureDataStorage:
    def __init__(self):
        self.config = AppConfiguration()

    def __get_file(self, pd_read, blob_name, usecols=None):
        blob = BlobClient.from_connection_string(conn_str=self.config.blob_connection_string,
                                                 container_name=self.config.blob_container_name,
                                                 blob_name=blob_name)
        with open(blob_name, "wb") as f:
            blob.download_blob().readinto(f)

        if usecols:
            df = pd_read(blob_name, usecols=usecols)
        else:
            df = pd_read(blob_name)

        cleanup_temp_file(blob_name)

        return df

    def get_schedule(self):
        return self.__get_file(pd.read_json, self.config.schedule_blob_name)

    def get_fleet(self, usecols=None):
        return self.__get_file(pd.read_csv, self.config.fleet_blob_name, usecols=usecols)

    def get_airports(self):
        return self.__get_file(pd.read_csv, self.config.airports_blob_name)
