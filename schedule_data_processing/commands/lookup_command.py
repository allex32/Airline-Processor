from schedule_data_processing.commands.exceptions import LookupEmptyResultException
from schedule_data_processing.commands.merge_command import MergeCommand
from schedule_data_processing.configuration.app_configuration import AppConfiguration


class LookupCommand:
    def __init__(self):
        self.merge_command = MergeCommand()
        self.config = AppConfiguration()

    def execute(self, flight_numbers):
        df = self.merge_command.execute_with_result()

        df.rename(columns={"Total": "total_seats"}, inplace=True)

        result = df[df.flight_number.isin(flight_numbers)][self.config.lookup_schema]

        if result.empty:
            raise LookupEmptyResultException(flight_numbers)

        return result.assign(**result.select_dtypes(['datetime']).astype(str)).to_json(orient="records")
