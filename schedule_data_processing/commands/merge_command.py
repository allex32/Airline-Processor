from schedule_data_processing.storage.data import AzureDataStorage

class MergeCommand:
    def __init__(self):
        self.storage = AzureDataStorage()

    def execute(self):
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
        joined.to_csv("output.csv")