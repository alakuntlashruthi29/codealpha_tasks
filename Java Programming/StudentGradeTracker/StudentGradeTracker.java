import java.util.ArrayList;
import java.util.Scanner;

public class StudentGradeTracker {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        ArrayList<Integer> marks = new ArrayList<>();

        System.out.print("Enter number of subjects: ");
        int n = sc.nextInt();

        for(int i=1;i<=n;i++)
        {
            System.out.print("Enter marks for Subject " + i + ": ");
            marks.add(sc.nextInt());
        }

        int total = 0;
        int highest = marks.get(0);
        int lowest = marks.get(0);

        for(int mark : marks)
        {
            total += mark;

            if(mark > highest)
                highest = mark;

            if(mark < lowest)
                lowest = mark;
        }

        double average = (double) total / n;

        System.out.println("\n----- Student Report -----");
        System.out.println("Total Marks = " + total);
        System.out.println("Average Marks = " + average);
        System.out.println("Highest Marks = " + highest);
        System.out.println("Lowest Marks = " + lowest);

        sc.close();
    }
}