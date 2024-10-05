from reservation import Reservation

reservation = Reservation()


def main():
    while True:
        reservation.setName(input("Enter Name: "))
        reservation.setDate(input("Enter Date: "))
        reservation.setTime(input("Enter Time: "))
        reservation.setNumAdults(input("Enter NsetNumAdults: "))
        reservation.setNumChild(input("Enter NsetNumChild: "))
        reservation.addReservation()
        print(reservation.viewReservation())
    
if __name__ == '__main__':
    main()

    