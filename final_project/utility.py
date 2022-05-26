from colors import colors


def echo_command(command=""):
    print(f"{colors.BOLD}{colors.OKBLUE}\n=== {command} ==={colors.ENDC}")


def echo_result(command=""):
    print(f"{colors.BOLD}{colors.OKGREEN}\n>>> {command} <<<{colors.ENDC}")


def get_confirmation(message=""):
    answer = input(f"{message} (yes/no) : ")
    return answer.lower() == "yes"