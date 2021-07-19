class NotSupportedCommandException(Exception):
    def __init__(self, command, *args, **kwargs):
        msg = f'Provided command {command} is not supported'
        super().__init__(msg, *args, **kwargs)

class LookupEmptyResultException(Exception):
    def __init__(self, flight_numbers, *args, **kwargs):
        msg = f'The dataset does not contain any values for the following flight numbers: {flight_numbers}'
        super().__init__(msg, *args, **kwargs)