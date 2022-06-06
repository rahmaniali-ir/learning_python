from colors import colors


def echo_bold(content=""):
    print(f"{colors.BOLD}{content}{colors.ENDC}")


def echo_command(command=""):
    echo_bold(f"{colors.OKBLUE}### {command}")


def echo_result(result=""):
    echo_bold(f"{colors.OKGREEN}>>> {result}")


def echo_error(error=""):
    echo_bold(f"{colors.FAIL}!!! {error}")


def get_confirmation(message=""):
    answer = input(f"{message} (yes/no) : ")
    return answer.lower() == "yes"
