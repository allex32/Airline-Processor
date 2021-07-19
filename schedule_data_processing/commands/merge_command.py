from schedule_data_processing.storage import data

class MergeCommand:
    def __init__(self):
        pass
    def execute(self):
        data.get_schedule()
        data.get_airports()
        data.get_fleet()
        schedule = data.SCHEDULE
        fleet = data.FLEET
        airports = data.AIRPORTS
        fleet["aircraft_registration"] = fleet["Reg"]
        joined = schedule.merge(fleet, on="aircraft_registration")
        airports["departure_airport"] = airports["Airport"]
        joined = joined.merge(airports, on="departure_airport", suffixes=(None, "_departure"))
        airports["arrival_airport"] = airports["Airport"]
        joined = joined.merge(airports, on="arrival_airport", suffixes=(None, "_arrival"))
        joined.drop(columns=["departure_airport_arrival"], inplace=True)
        joined.to_csv("output.csv")