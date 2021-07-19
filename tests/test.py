import unittest

from schedule_data_processing.app import main
from schedule_data_processing.commands.response_decorator import ResponseStatus


class TestCLI(unittest.TestCase):
    def test_lookup(self):
        result = main(["app.py", "lookup", "ZG2362"])
        assert result.status == ResponseStatus.SUCCESS
        assert result.data == '{"aircraft_registration": "ZGAUI", "departure_airport": "MCO", "arrival_airport": "FRA", "scheduled_departure_time": "2020-01-01 16:05:00", "scheduled_takeoff_time": "2020-01-01 16:15:00", "scheduled_landing_time": "2020-01-02 00:55:00", "scheduled_arrival_time": "2020-01-02 01:05:00", "flight_number": "ZG2362", "IATATypeDesignator": "789", "TypeName": "Boeing 787-9", "Hub": "FRA", "Haul": "LH", "total_seats": "216"}'

    def test_merge_count(self):
        result = main(["app.py", "merge"])
        assert result.status == ResponseStatus.SUCCESS
        # assert len(result.data.index) == 898

    def test_unsupported_request(self):
        result = main(["app.py", "unsupported_request"])
        assert result.status == ResponseStatus.NOT_SUPPORTED_REQUEST

if __name__ == '__main__':
    unittest.main()
