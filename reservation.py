from validate import Validate
class Reservation:
    
    def __init__(self):
        self.name = ''
        self.date = ''
        self.time = ''
        self.numAdults = 0
        self.numChild = 0
        self.reservationList = []
        self.readReservation()
        self.validate = Validate()
        
        
    def addReservation(self):
        reservationForm = {
            "name": self.name,
            "date": self.date,
            "time": self.time,
            "adults": self.numAdults,
            "children": self.numChild
        }
        self.setReservation(reservationForm)
        self.saveReservation()
        
    def setReservation(self, form):
        self.reservationList.append(form)
    
    def setName(self, name):
        if self.validate.validateRequired(name) == False:
            raise Exception('NoValue')
        if self.validate.validateSpecialCharacters(name) == False:
            raise Exception('SpecialChar')
        self.name = name
        
    def setDate(self, date):
        if self.validate.validateRequired(date) == False:
            raise Exception('NoValue')
        if self.validate.validateDateFormat(date) == False:
            raise Exception('DateError') 
        self.date = date
        
    def setTime(self, time):
        if self.validate.validateRequired(time) == False:
            raise Exception('NoValue')
        if self.validate.validateTimeFormat(time) == False:
            raise Exception('InvalidTime')
        self.time = time
        
    def setNumAdults(self, numAdults):
        if self.validate.validateRequired(numAdults) == False:
            raise Exception('NoValue')
        if self.validate.validateInteger(numAdults) == False:
            raise Exception('NonInteger')
        if int(numAdults) <= 0:
            raise Exception("Zero") 
        
        self.numAdults = int(numAdults)
        
    def setNumChild(self, numChild):
        if self.validate.validateRequired(numChild) == False:
            raise Exception('NoValue')
        if self.validate.validateInteger(numChild) == False:
            raise Exception('NonInteger')
        if int(numChild) < 0:
            raise Exception("Negative")
         
        self.numChild = int(numChild)
    
    def getReservation(self):
        return self.reservationList
    
    def delReservation(self, index):
        
        if(len(self.reservationList) <= 0):
            print("The reservation list is currently empty")
            return 
        
        if index > len(self.reservationList)-1:
            print("Number is greater than current reservation")
            return
         
        del self.reservationList[index]
        self.saveReservation()
        
    def genReport(self):
        
        numAdult = 0
        numChild = 0
        for i in self.reservationList:
            numAdult += i.get("adults")
            numChild += i.get("children")
            
        print(
        f"""
Total number of Adults: {numAdult}
Total number of Kids: {numChild}
Grand Total: PHP {(numAdult*500) + (numChild*300)}    
        """
        )

    def readReservation(self):
        f = open("reservation.txt", "r")
        for idx, x in enumerate(f):
            if idx == 0:
                continue
            
            val = x.split(",") 
            
            self.setReservation(
                {
                    "name": val[0],
                    "date": val[1],
                    "time": val[2],
                    "adults": int(val[3]),
                    "children": int(val[4])
                }                
            )
            
        f.close()

    def saveReservation(self):
        f = open("reservation.txt", "w")

        f.write("name,date,time,adults,children\n")

        for i in self.reservationList:
            row = [str(i.get(values)) for values in i]
            f.write(",".join(row)+"\n")

        f.close()
        pass