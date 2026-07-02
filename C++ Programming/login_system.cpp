#include <iostream>
#include <fstream>
#include <string>
using namespace std;

void registerUser()
{
    string username, password;

    cout << "\n===== User Registration =====\n";

    cout << "Enter Username: ";
    cin >> username;

    cout << "Enter Password: ";
    cin >> password;

    ofstream file(username + ".txt");

    file << username << endl;
    file << password << endl;

    file.close();

    cout << "Registration Successful!\n";
}

void loginUser()
{
    string username, password;
    string storedUsername, storedPassword;

    cout << "\n===== User Login =====\n";

    cout << "Enter Username: ";
    cin >> username;

    cout << "Enter Password: ";
    cin >> password;

    ifstream file(username + ".txt");

    if (!file)
    {
        cout << "User does not exist!\n";
        return;
    }

    getline(file, storedUsername);
    getline(file, storedPassword);

    file.close();

    if (username == storedUsername && password == storedPassword)
    {
        cout << "Login Successful!\n";
    }
    else
    {
        cout << "Incorrect Password!\n";
    }
}

int main()
{
    int choice;

    while (true)
    {
        cout << "\n===== Login and Registration System =====\n";
        cout << "1. Register\n";
        cout << "2. Login\n";
        cout << "3. Exit\n";

        cout << "Enter Your Choice: ";
        cin >> choice;

        switch (choice)
        {
            case 1:
                registerUser();
                break;

            case 2:
                loginUser();
                break;

            case 3:
                cout << "Thank You!\n";
                return 0;

            default:
                cout << "Invalid Choice!\n";
        }
    }

    return 0;
}