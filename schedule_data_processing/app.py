from schedule_data_processing.commands.command_executor import CommandExecutor

if __name__ == "__main__":
    from package import data
else:
    from schedule_data_processing.package import data

def main(args):
    executor = CommandExecutor(args)
    return executor.execute()


if __name__ == "__main__":
    print(main(list(["", "lookup", "ZG2361"])))
    # print(main(sys.argv))

