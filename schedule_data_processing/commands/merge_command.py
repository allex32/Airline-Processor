from geopy import Point
from geopy.distance import distance

from schedule_data_processing.storage.data import AzureDataStorage
from schedule_data_processing.configuration.app_configuration import AppConfiguration


class MergeCommand:
    def __init__(self):
        self.storage = AzureDataStorage()
        self.config = AppConfiguration()

    def __merge(self):
        schedule = self.storage.get_schedule()
        fleet = self.storage.get_fleet()
        airports = self.storage.get_airports()

        fleet["aircraft_registration"] = fleet["Reg"]
        joined = schedule.merge(fleet, on="aircraft_registration")
        airports["departure_airport"] = airports["Airport"]
        joined = joined.merge(airports, on="departure_airport", suffixes=(None, "_departure"))
        airports["arrival_airport"] = airports["Airport"]
        joined = joined.merge(airports, on="arrival_airport", suffixes=(None, "_arrival"))

        joined.drop(columns=["departure_airport_arrival"], inplace=True)

        joined['distance_nm'] = joined.apply(lambda row: distance(Point(latitude=row['Lat'], longitude=row['Lon']),
                                                              Point(latitude=row['Lat_arrival'], longitude=row['Lon_arrival'])).nm, axis=1)

        return joined

    def execute(self):
        self.__merge().to_csv(self.config.merge_output_file_path)

    def execute_with_result(self):
        return self.__merge()
