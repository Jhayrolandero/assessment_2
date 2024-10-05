class Reservation:
    
    def __init__(self):
        self.name = ''
        self.date = ''
        self.time = ''
        self.numAdults = 0
        self.numChild = 0
        self.reservationList = ["Lol"]
        
    def addReservation(self):
        reservationForm = {
            "name": self.name,
            "date": self.date,
            "adults": self.numAdults,
            "children": self.numChild
        }
        
        self.reservationList.append(reservationForm)
    
    def setName(self, name):
        self.name = name
        
    def setDate(self, date):
        self.date = date
        
    def setTime(self, time):
        self.time = time
        
    def setNumAdults(self, numAdults):
        self.numAdults = numAdults
        
    def setNumChild(self, numChild):
        self.numChild = numChild
    
    def viewReservation(self):
        return self.reservationList
    
    def delReservation(self, index):
        pass
    
    def genReport(self):
        pass