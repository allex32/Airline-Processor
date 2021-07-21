from schedule_data_processing.commands.exceptions import NotSupportedCommandException
from schedule_data_processing.commands.lookup_command import LookupCommand
from schedule_data_processing.commands.merge_command import MergeCommand
from schedule_data_processing.commands.response_decorator import decorate_response
from schedule_data_processing.logging.app_logger import log_response


class CommandExecutor:
    def __init__(self, command, **predicates):
        self.command = command
        self.predicates = predicates

    @log_response
    @decorate_response
    def execute(self):
        if self.command.lower() == "lookup":
            lookup_command = LookupCommand()
            return lookup_command.execute(self.predicates.get('flight_numbers').split(","))

        if self.command.lower() == "merge":
            merge_command = MergeCommand()
            return merge_command.execute()

        raise NotSupportedCommandException(self.command)