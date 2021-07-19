import json
from schedule_data_processing.storage.data import AzureDataStorage


class LookupCommand:
    def __init__(self):
        self.storage = AzureDataStorage()

    def execute(self, args):
        flight_numbers = args[2].split(",")
        for flight_number in flight_numbers:
            schedule = self.storage.get_schedule()
            fleet = self.storage.get_fleet()
            fleet["aircraft_registration"] = fleet["Reg"]
            joined = schedule.merge(fleet, on="aircraft_registration")
            result = joined[joined.flight_number == flight_number]
            result = result.to_dict(orient="list")
            keys = []
            for x in result.keys():
                keys.append(x)
            for x in keys:
                if x in "F,C,E,M":
                    del result[x]
                elif x in "RangeLower,RangeUpper,Reg":
                    del result[x]
                elif x == "Total":
                    result["total_seats"] = str(result[x][0])
                    del result[x]
                else:
                    result[x] = str(result[x][0])
            return json.dumps(result)