import os
from configparser import ConfigParser


class AppConfiguration:
    def __init__(self, config_file_path = None):
        if config_file_path is None:
            config_file_path = os.path.join(os.path.dirname(__file__), 'app_configuration.ini')

        self._config_parser = ConfigParser()
        self._config_parser.read(config_file_path)

        self.blob_connection_string = self._config_parser['Storage']['ConnectionString']
        self.blob_container_name = self._config_parser['Storage']['ContainerName']
        self.schedule_blob_name = self._config_parser['Storage']['ScheduleBlobName']
        self.fleet_blob_name = self._config_parser['Storage']['FleetBlobName']
        self.airports_blob_name = self._config_parser['Storage']['AirportsBlobName']

        self.lookup_schema = self._config_parser['Lookup']['Schema'].split(',')

        self.merge_output_file_path = self._config_parser['Merge']['OutputFilePath']

