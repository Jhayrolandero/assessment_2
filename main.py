from option import ReservationOption

option = ReservationOption()

def main():
    while True:
        # Display Options
        option.showOption()
        # user prompt
        option.select(input(" "))
    
if __name__ == '__main__':
    main()

    