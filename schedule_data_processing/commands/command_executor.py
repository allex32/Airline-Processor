from schedule_data_processing.commands.exceptions import NotSupportedCommandException
from schedule_data_processing.commands.lookup_command import LookupCommand
from schedule_data_processing.commands.merge_command import MergeCommand


class CommandExecutor:
    def __init__(self, args):
        self.__args = args

    def execute(self):
        command = self.__args[1]

        if command == "lookup":
            lookup_command = LookupCommand()
            return lookup_command.execute(self.__args)

        if command == "merge":
            merge_command = MergeCommand()
            return merge_command.execute()

        raise NotSupportedCommandException(f'Provided command {command} is not supported')