from schedule_data_processing.commands.exceptions import NotSupportedCommandException
from enum import Enum


class ResponseStatus(str, Enum):
    SUCCESS = 'SUCCESS'
    NOT_SUPPORTED_REQUEST = 'NOT_SUPPORTED_REQUEST'
    FAILURE = "FAILURE"


class Response:
    def __init__(self, status, error_message=None, data=None):
        self.status = status
        self.error_message = error_message
        self.data = data


def decorate_response(fn):
    def decorator(*args, **kwargs):
        try:
            result = fn(*args, **kwargs)
            return Response(status=ResponseStatus.SUCCESS, data=result)
        except NotSupportedCommandException as e:
            return Response(status=ResponseStatus.NOT_SUPPORTED_REQUEST, error_message=str(e))
        except Exception as e:
            return Response(status=ResponseStatus.FAILURE, error_message=str(e))

    return decorator
