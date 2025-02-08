from validate import Validate


class Employee:

    def __init__(self):
        self.id = self.fetchEmployeeNumber()
        self.name = ''
        self.position = ''
        self.salary = 0
        self.employeeList = []
        self.readEmployee()
        self.validate = Validate()

    def addEmployee(self):
        employeeForm = {
            "id": self.id,
            "name": self.name,
            "position": self.position,
            "salary": self.salary
        }
        self.setEmployee(employeeForm)
        self.saveEmployee()
        self.incrementEmployeeNumber()

    def setEmployee(self, form):
        self.employeeList.append(form)

    def setName(self, name):
        if self.validate.validateRequired(name) == False:
            raise Exception('NoValue')
        if self.validate.validateSpecialCharacters(name) == False:
            raise Exception('SpecialChar')
        self.name = name

    def setPosition(self, position):
        self.position = position

    def setSalary(self, salary):
        self.salary = salary

    def getEmployee(self):
        print(self.employeeList)
        return self.employeeList

    def fetchEmployeeNumber(self):
        with open("number.txt", "r") as file:
            number = file.read().strip()

            if not number or not number.isdigit():
                number = "100"
                with open("number.txt", "w") as f:
                    f.write(number)

            return number

    def incrementEmployeeNumber(self):

        print(type(int(self.id)))
        new_id = int(self.id) + 1

        with open("number.txt", "w") as f:
            f.write(str(new_id))

        self.id = str(new_id)

    def delEmployee(self, id):
        id = str(id).strip()

        self.employeeList = [
            item for item in self.employeeList if str(item.get('id')).strip() != id]

        self.saveEmployee()

    def readEmployee(self):
        f = open("employees.txt", "r")
        for idx, x in enumerate(f):
            if idx == 0:
                continue

            val = x.split(",")

            self.setEmployee(
                {
                    "id": val[0],
                    "name": val[1],
                    "position": val[2],
                    "salary": int(val[3]),
                }
            )

        f.close()

    def updateEmployee(self, id):
        current = [
            item for item in self.employeeList if str(item.get('id')).strip() == id]

        if (len(current) < 1):
            print("===============")
            print("No Employee")
            print("===============")
            return ""

        # Remove
        self.employeeList = [
            item for item in self.employeeList if str(item.get('id')).strip() != id]

        temp = current[0]

        currentId = temp["id"]

        newData = {"id": currentId, "name": self.name,
                   "position": self.position, "salary": self.salary}

        print(newData)
        self.employeeList.append(newData)

        self.saveEmployee()
        return

    def searchEmployee(self, id):
        employee = [
            item for item in self.employeeList if str(item.get('id')).strip() == id]

        print(employee[0])
        return employee[0]

    def sortEmployee(self, by):
        match by:
            case "name":
                self.employeeList = sorted(
                    self.employeeList, key=lambda x: x['name'])
            case "salary":
                self.employeeList = sorted(
                    self.employeeList, key=lambda x: x['salary'])
            case _:
                print("No Option")

        return self.employeeList

    def saveEmployee(self):
        f = open("employees.txt", "w")

        f.write("id,name,position,salary\n")
        # f.write("name,date,time,adults,children\n")

        for i in self.employeeList:
            row = [str(i.get(values)) for values in i]
            f.write(",".join(row)+"\n")

        f.close()
        pass
