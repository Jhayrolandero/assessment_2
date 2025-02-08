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
        match user_input.lower():
            case "a":
                self.tabulateView(self.getEmployee())
            case "b":
                self.userPrompt()
            case "c":
                self.tabulateView(self.getEmployee())
                self.deleteOption(
                    input("Enter the ID of employee to delete: "))
            case "d":
                self.editEmployee()
            case "e":
                self.tabulateView(self.sortTable(input("Sort by(ID/Name): ")))
            case "f":
                self.tabulateView(self.getEmployee())
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
        
        if(data == -1):
            print("Employee not found!")
            return
        
        print("""
        ====================
        EMPLOYEE INFORMATION
        ====================
        """)

        print(f"ID: ", data["id"])
        print(f"Name: ", data["name"])
        print(f"Position: ", data["position"])
        print(f"Salary: ", data["salary"])

