from option import EmployeeOption

option = EmployeeOption()


def main():
    while True:
        # Display Options
        option.showOption()
        # user prompt
        option.select(input(" "))


if __name__ == '__main__':
    main()
