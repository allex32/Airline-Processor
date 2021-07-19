import unittest
import pandas as pd

from schedule_data_processing.app import main
from schedule_data_processing.commands.response_decorator import ResponseStatus


class TestCLI(unittest.TestCase):
    def test_lookup_when_signle_input(self):
        result = main(["app.py", "lookup", "ZG2362"])

        assert result.status == ResponseStatus.SUCCESS

        df = pd.read_json(result.data)

        assert len(df.index) == 1
        assert set(df['flight_number'].values) == {'ZG2362'}
        assert set(df['aircraft_registration'].values) == {'ZGAUI'}

    def test_lookup_when_multiple_input(self):
        result = main(["app.py", "lookup", "ZG2361,ZG2362"])

        assert result.status == ResponseStatus.SUCCESS

        df = pd.read_json(result.data)

        assert len(df.index) == 2
        assert set(df['flight_number'].values) == {'ZG2361', 'ZG2362'}
        assert set(df['aircraft_registration'].values) == {'ZGAUI'}

    def test_lookup_when_flight_is_not_found(self):
        result = main(["app.py", "lookup", "Nonexistent flight"])

        assert result.status == ResponseStatus.FLIGHT_NOT_FOUND

    def test_merge(self):
        result = main(["app.py", "merge"])
        assert result.status == ResponseStatus.SUCCESS

    def test_unsupported_request(self):
        result = main(["app.py", "unsupported_request"])
        assert result.status == ResponseStatus.NOT_SUPPORTED_REQUEST


if __name__ == '__main__':
    unittest.main()
