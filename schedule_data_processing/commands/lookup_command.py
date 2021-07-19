from schedule_data_processing.commands.exceptions import LookupEmptyResultException
from schedule_data_processing.storage.data import AzureDataStorage


class LookupCommand:
    def __init__(self):
        self.storage = AzureDataStorage()

    def execute(self, args):
        schedule = self.storage.get_schedule()

        fleet = self.storage.get_fleet(usecols=['IATATypeDesignator', 'TypeName', 'Total', 'Reg', 'Hub', 'Haul'])
        fleet.rename(columns={"Reg" : "aircraft_registration", "Total": "total_seats"}, inplace=True)

        flight_numbers = args[2].split(",")

        joined = schedule.merge(fleet, on="aircraft_registration")

        result = joined[joined.flight_number.isin(flight_numbers)]

        if result.empty:
            raise LookupEmptyResultException(flight_numbers)

        return result.assign(**result.select_dtypes(['datetime']).astype(str)).to_json(orient="records")
