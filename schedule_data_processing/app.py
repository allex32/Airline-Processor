import sys
from schedule_data_processing.commands.command_executor import CommandExecutor


def main(args):
    flight_numbers = None
    if len(args) > 2:
        flight_numbers = args[2]

    executor = CommandExecutor(command=args[1], flight_numbers=flight_numbers)
    return executor.execute().data


if __name__ == "__main__":
    print(main(sys.argv))
