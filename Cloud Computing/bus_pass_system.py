# Cloud-Based Bus Pass System

def book_pass():
    name = input("Enter Passenger Name: ")
    source = input("Enter Source: ")
    destination = input("Enter Destination: ")

    distance = int(input("Enter Distance (km): "))
    price = distance * 2

    with open("bus_passes.txt", "a") as file:
        file.write(f"{name},{source},{destination},{distance},{price}\n")

    print("\nPass Booked Successfully!")
    print("Ticket Price =", price)


def view_bookings():
    try:
        with open("bus_passes.txt", "r") as file:
            data = file.readlines()

            if not data:
                print("No bookings found.")
                return

            print("\n----- Booking Records -----")

            for line in data:
                name, source, destination, distance, price = line.strip().split(",")

                print("Passenger Name :", name)
                print("Source         :", source)
                print("Destination    :", destination)
                print("Distance (km)  :", distance)
                print("Price          :", price)
                print("--------------------------")

    except FileNotFoundError:
        print("No booking records available.")


while True:
    print("\n===== Cloud-Based Bus Pass System =====")
    print("1. Book Bus Pass")
    print("2. View Bookings")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        book_pass()

    elif choice == "2":
        view_bookings()

    elif choice == "3":
        print("Thank You!")
        break

    else:
        print("Invalid choice!")