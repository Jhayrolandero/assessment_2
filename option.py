from reservation import Reservation
from texttable import Texttable
import sys
class ReservationOption(Reservation):
    
    def showOption(self):
        print("""
╦═╗╔═╗╔═╗╔╦╗╔═╗╦ ╦╦═╗╔═╗╔╗╔╔╦╗  ╦═╗╔═╗╔═╗╔═╗╦═╗╦  ╦╔═╗╔╦╗╦╔═╗╔╗╔  ╔═╗╦ ╦╔═╗╔╦╗╔═╗╔╦╗
╠╦╝║╣ ╚═╗ ║ ╠═╣║ ║╠╦╝╠═╣║║║ ║   ╠╦╝║╣ ╚═╗║╣ ╠╦╝╚╗╔╝╠═╣ ║ ║║ ║║║║  ╚═╗╚╦╝╚═╗ ║ ║╣ ║║║
╩╚═╚═╝╚═╝ ╩ ╩ ╩╚═╝╩╚═╩ ╩╝╚╝ ╩   ╩╚═╚═╝╚═╝╚═╝╩╚═ ╚╝ ╩ ╩ ╩ ╩╚═╝╝╚╝  ╚═╝ ╩ ╚═╝ ╩ ╚═╝╩ ╩
""")
        print("System Menu")
        print("a. View All Reservation")
        print("b. Make Reservation")
        print("c. Delete Reservation")
        print("d. Generate Report")
        print("e. Exit")

    def select(self, user_input):
        match user_input:
            case "a":
                self.tabulateView(self.getReservation(), "list")
            case "b":
                try:
                    self.setName(input("Enter Name: ").strip())
                    self.setDate(input("Enter Date(mm-dd-yyyy): ").strip())
                    self.setTime(input("Enter Time: ").strip())
                    self.setNumAdults(input("Enter number of adults: ").strip())
                    self.setNumChild(input("Enter number of children: ").strip())
                    self.addReservation()
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
            case "c":
                self.deleteOption(input("Enter the number of reservation to delete: "))
            case "d":
                self.tabulateView(self.getReservation(), "report")
                self.genReport()
            case "e":
                print("Thank you!")
                sys.exit()
            case _:
                print("No Option")
            
    def tabulateView(self, reserveList, type):
        self.tableHeading(type)
        table = Texttable()
        
        if(len(reserveList) <= 0):
            table.add_row(['No Reservations!'])
            print(table.draw())
            return
        
        # Get the keys (Header)
        header = [key.title() for key in reserveList[0]]
        header.insert(0, "#")
        table.header(header)
        
        # Populate the rows (values)
        for idx, i in enumerate(reserveList):
            row = [i.get(values) for values in i]
            row.insert(0, idx+1)
            table.add_row(row)
        
        print(table.draw())
        
    def deleteOption(self, idx):
        try:
            idx = int(idx)
        except ValueError:
            print("Value must be number")
            return
        
        if idx < 1:
            print("Number cannot be less than 1")
            return
        
        self.delReservation(idx-1)
        pass
    
    def tableHeading(self, type):
        match type:
            case "list":
                print("""
 ___ ___  __  ___ ___  _   _   __ _____ _  __  __  _   _   _   __ _____  
| _ \ __/' _/| __| _ \| \ / | /  \_   _| |/__\|  \| | | | | |/' _/_   _| 
| v / _|`._`.| _|| v /`\ V /'| /\ || | | | \/ | | ' | | |_| |`._`. | |   
|_|_\___|___/|___|_|_\  \_/  |_||_||_| |_|\__/|_|\__| |___|_||___/ |_|
""")
            case "report":
                print("""
 ___ ___  __  ___ ___  _   _   __ _____ _  __  __  _   ___ ___ ___  __  ___ _____  
| _ \ __/' _/| __| _ \| \ / | /  \_   _| |/__\|  \| | | _ \ __| _,\/__\| _ \_   _| 
| v / _|`._`.| _|| v /`\ V /'| /\ || | | | \/ | | ' | | v / _|| v_/ \/ | v / | |   
|_|_\___|___/|___|_|_\  \_/  |_||_||_| |_|\__/|_|\__| |_|_\___|_|  \__/|_|_\ |_|   
                      """)
