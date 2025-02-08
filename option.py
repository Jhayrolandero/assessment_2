from employee import Employee
from texttable import Texttable
import sys


class EmployeeOption(Employee):

    def showOption(self):
        print("""
        EMPLOYEE LIST
""")
        print("System Menu")
        print("a. View All Employee")
        print("b. Make Employee")
        print("c. Delete Employee")
        print("d. Update Employee")
        print("e. Sort Employee")
        print("f. Search Employee")
        print("h. Save employee")
        print("g. Exit")

    def select(self, user_input):
        match user_input:
            case "a":
                self.tabulateView(self.getEmployee())
            case "b":
                self.userPrompt()
            case "c":
                self.deleteOption(
                    input("Enter the number of employee to delete: "))
            case "d":
                self.editEmployee()
            case "e":
                self.tabulateView(self.sortTable(input("Sort by: ")))
            case "f":
                self.searchForEmployee(
                    input("Enter the ID of employee: "))
            case "h":
                self.saveToText()
            case "g":
                print("Thank you!")
                sys.exit()
            case _:
                print("No Option")

    def userPrompt(self):
        try:
            self.setName(input("Enter Name: ").strip())
            self.setPosition(input("Enter Position: ").strip())
            self.setSalary(input("Enter Salary: ").strip())
            self.addEmployee()
        except Exception as e:
            if str(e) == "NoValue":
                print("Error: No value provided!")
            elif str(e) == "Zero":
                print("Error: Value cannot be zero or less!")
            elif str(e) == "NonInteger":
                print("Error: Value must be an integer!")
            elif str(e) == "DateError":
                print("Error: Invalid date format")
            elif str(e) == "InvalidTime":
                print("Error: Invalid time format")
            elif str(e) == "Negative":
                print("Error: Value is less than zero")
            elif str(e) == "SpecialChar":
                print("Error: Special character is invalid")
            else:
                print(f"An unexpected error occurred: {e}")
            return

    def saveToText(self):
        try:
            self.saveEmployee()
            print("Saved!")
        except:
            print("Error saving")

    def tabulateView(self, reserveList):
        table = Texttable()

        if (len(reserveList) <= 0):
            table.add_row(['No Employees!'])
            print(table.draw())
            return

        # Get the keys (Header)
        header = [key.title() for key in reserveList[0]]
        # # header.insert(0, "#")
        table.header(header)

        for idx, i in enumerate(reserveList):
            row = [i.get(values) for values in i]
            table.add_row(row)

        print(table.draw())

    def sortTable(self, input):
        return self.sortEmployee(input)

    def deleteOption(self, idx):
        try:
            idx = int(idx)
        except ValueError:
            print("Value must be number")
            return

        if idx < 1:
            print("Number cannot be less than 1")
            return

        self.delEmployee(idx)
        pass

    def editEmployee(self):
        try:
            id = input("Enter ID: ").strip()
            self.setName(input("Enter Name: ").strip())
            self.setPosition(input("Enter Position: ").strip())
            self.setSalary(input("Enter Salary: ").strip())
            self.updateEmployee(id)

        except Exception as e:
            if str(e) == "NoValue":
                print("Error: No value provided!")
            elif str(e) == "Zero":
                print("Error: Value cannot be zero or less!")
            elif str(e) == "NonInteger":
                print("Error: Value must be an integer!")
            elif str(e) == "DateError":
                print("Error: Invalid date format")
            elif str(e) == "InvalidTime":
                print("Error: Invalid time format")
            elif str(e) == "Negative":
                print("Error: Value is less than zero")
            elif str(e) == "SpecialChar":
                print("Error: Special character is invalid")
            else:
                print(f"An unexpected error occurred: {e}")
            return
        pass

    def searchForEmployee(self, number):
        data = self.searchEmployee(number)
        print("""
        EMPLOYEE INFORMATION
        """)

        print(f"ID: ", data["id"])
        print(f"Name: ", data["name"])
        print(f"Position: ", data["position"])
        print(f"Salary: ", data["salary"])

#     def tableHeading(self, type):
#         match type:
#             case "list":
#                 print("""
#  ___ ___  __  ___ ___  _   _   __ _____ _  __  __  _   _   _   __ _____
# | _ \ __/' _/| __| _ \| \ / | /  \_   _| |/__\|  \| | | | | |/' _/_   _|
# | v / _|`._`.| _|| v /`\ V /'| /\ || | | | \/ | | ' | | |_| |`._`. | |
# |_|_\___|___/|___|_|_\  \_/  |_||_||_| |_|\__/|_|\__| |___|_||___/ |_|
# """)
#             case "report":
#                 print("""
#  ___ ___  __  ___ ___  _   _   __ _____ _  __  __  _   ___ ___ ___  __  ___ _____
# | _ \ __/' _/| __| _ \| \ / | /  \_   _| |/__\|  \| | | _ \ __| _,\/__\| _ \_   _|
# | v / _|`._`.| _|| v /`\ V /'| /\ || | | | \/ | | ' | | v / _|| v_/ \/ | v / | |
# |_|_\___|___/|___|_|_\  \_/  |_||_||_| |_|\__/|_|\__| |_|_\___|_|  \__/|_|_\ |_|
#                       """)
