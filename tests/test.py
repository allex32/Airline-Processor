import unittest
import pandas as pd

from schedule_data_processing.commands.response_decorator import ResponseStatus
from schedule_data_processing.commands.command_executor import CommandExecutor
from schedule_data_processing.configuration.app_configuration import AppConfiguration


class TestCLI(unittest.TestCase):
    lookup = 'lookup'
    merge = 'merge'
    unsupported_request = "unsupported_request"

    def setUp(self):
        self.config = AppConfiguration()

    def test_lookup_method_valid_schema(self):
        result = CommandExecutor(command=self.lookup, flight_numbers="ZG2362").execute()

        assert result.status == ResponseStatus.SUCCESS

        df = pd.read_json(result.data)

        assert set(df.columns.values) == set(self.config.lookup_schema)

    def test_lookup_method_result_when_signle_input(self):
        result = CommandExecutor(command=self.lookup, flight_numbers="ZG2362").execute()

        assert result.status == ResponseStatus.SUCCESS

        df = pd.read_json(result.data)

        assert len(df.index) == 1
        assert set(df['flight_number'].values) == {'ZG2362'}
        assert set(df['aircraft_registration'].values) == {'ZGAUI'}

    def test_lookup_method_result_when_multiple_input(self):
        result = CommandExecutor(command=self.lookup, flight_numbers="ZG2361,ZG2362").execute()

        assert result.status == ResponseStatus.SUCCESS

        df = pd.read_json(result.data)

        assert len(df.index) == 2
        assert set(df['flight_number'].values) == {'ZG2361', 'ZG2362'}
        assert set(df['aircraft_registration'].values) == {'ZGAUI'}

    def test_lookup_method_result_when_flight_is_not_found(self):
        result = CommandExecutor(command=self.lookup, flight_numbers="Nonexistent flight").execute()
        assert result.status == ResponseStatus.FLIGHT_NOT_FOUND

    def test_merge_method_nautical_miles_calculation(self):
        result = CommandExecutor(command=self.merge).execute()

        assert result.status == ResponseStatus.SUCCESS

        df = pd.read_csv(self.config.merge_output_file_path)

        airports = ['FRA', 'ACE']
        expected_distance = 1617.76
        actual_distances = df[
            (df.departure_airport.isin(airports)) & (df.arrival_airport.isin(airports))].distance_nm.round(2)

        assert (actual_distances == expected_distance).all()

    def test_unsupported_request(self):
        result = CommandExecutor(command=self.unsupported_request).execute()
        assert result.status == ResponseStatus.NOT_SUPPORTED_REQUEST


if __name__ == '__main__':
    unittest.main()
