import java.util.Scanner;

public class HotelReservationSystem {

    static boolean standardBooked = false;
    static boolean luxuryBooked = false;

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        while(true)
        {
            System.out.println("\n===== HOTEL RESERVATION SYSTEM =====");
            System.out.println("1. View Rooms");
            System.out.println("2. Book Room");
            System.out.println("3. Cancel Booking");
            System.out.println("4. Exit");

            System.out.print("Enter Choice: ");
            int choice = sc.nextInt();

            switch(choice)
            {
                case 1:
                    viewRooms();
                    break;

                case 2:
                    bookRoom(sc);
                    break;

                case 3:
                    cancelBooking(sc);
                    break;

                case 4:
                    System.out.println("Thank You!");
                    System.exit(0);

                default:
                    System.out.println("Invalid Choice");
            }
        }
    }

    static void viewRooms()
    {
        System.out.println("\nRoom Details");

        System.out.println("1. Standard Room - Rs.2000");
        System.out.println("Booked: " + standardBooked);

        System.out.println("2. Luxury Room - Rs.5000");
        System.out.println("Booked: " + luxuryBooked);
    }

    static void bookRoom(Scanner sc)
    {
        System.out.println("\n1. Standard Room");
        System.out.println("2. Luxury Room");

        System.out.print("Select Room: ");
        int room = sc.nextInt();

        if(room == 1)
        {
            if(!standardBooked)
            {
                standardBooked = true;
                System.out.println("Standard Room Booked Successfully!");
                System.out.println("Payment: Rs.2000 Paid");
            }
            else
            {
                System.out.println("Room Already Booked");
            }
        }
        else if(room == 2)
        {
            if(!luxuryBooked)
            {
                luxuryBooked = true;
                System.out.println("Luxury Room Booked Successfully!");
                System.out.println("Payment: Rs.5000 Paid");
            }
            else
            {
                System.out.println("Room Already Booked");
            }
        }
    }

    static void cancelBooking(Scanner sc)
    {
        System.out.println("\n1. Standard Room");
        System.out.println("2. Luxury Room");

        System.out.print("Select Room to Cancel: ");
        int room = sc.nextInt();

        if(room == 1)
        {
            standardBooked = false;
            System.out.println("Standard Room Booking Cancelled");
        }
        else if(room == 2)
        {
            luxuryBooked = false;
            System.out.println("Luxury Room Booking Cancelled");
        }
    }
}