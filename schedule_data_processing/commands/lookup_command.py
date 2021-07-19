import json

from schedule_data_processing.package import data

class LookupCommand:
    def __init__(self):
        pass

    def execute(self, args):
        flight_numbers = args[2].split(",")
        for flight_number in flight_numbers:
            data.get_data()
            schedule = data.SCHEDULE
            fleet = data.FLEET
            airports = data.AIRPORTS
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