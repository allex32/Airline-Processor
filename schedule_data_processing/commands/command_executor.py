from schedule_data_processing.commands.exceptions import NotSupportedCommandException
from schedule_data_processing.commands.lookup_command import LookupCommand
from schedule_data_processing.commands.merge_command import MergeCommand
from schedule_data_processing.commands.response_decorator import decorate_response
from schedule_data_processing.logging.app_logger import log_response


class CommandExecutor:
    def __init__(self, args):
        self.__args = args
        self.command = args[1]

    @log_response
    @decorate_response
    def execute(self):
        if self.command == "lookup":
            lookup_command = LookupCommand()
            return lookup_command.execute(self.__args)

        if self.command == "merge":
            merge_command = MergeCommand()
            return merge_command.execute()

        raise NotSupportedCommandException(f'Provided command {self.command} is not supported')