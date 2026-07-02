#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
    int n;
    float grade, credit;
    float totalCredits = 0, totalGradePoints = 0;

    cout << "===== CGPA Calculator =====" << endl;

    cout << "Enter number of courses: ";
    cin >> n;

    for(int i = 1; i <= n; i++)
    {
        cout << "\nCourse " << i << endl;

        cout << "Enter Grade Point: ";
        cin >> grade;

        cout << "Enter Credit Hours: ";
        cin >> credit;

        totalCredits += credit;
        totalGradePoints += grade * credit;
    }

    float cgpa = totalGradePoints / totalCredits;

    cout << "\n===== RESULT =====" << endl;
    cout << "Total Credits = " << totalCredits << endl;
    cout << "Total Grade Points = " << totalGradePoints << endl;

    cout << fixed << setprecision(2);
    cout << "Final CGPA = " << cgpa << endl;

    return 0;
}