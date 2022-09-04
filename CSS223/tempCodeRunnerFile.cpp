#include <iostream>

using namespace std;

struct students
{
    string name;
    int score;
}student[10];

int main()
{


    while (true)
    {
        int new_number;
        cout << "Enter a number: ";
        cin >> new_number;
        
        // Sorting name, score
        for (int i = 0; i < 10; i++)
        {
            if (new_number > student[i].score)
            {
                for (int j = 9; j > i; j--)
                {
                    student[j].score = student[j - 1].score;
                    student[j].name = student[j - 1].name;
                }
                student[i].score = new_number;
                cout << "Enter a name: ";
                cin >> student[i].name;
                break;
            }
        }

    }
}