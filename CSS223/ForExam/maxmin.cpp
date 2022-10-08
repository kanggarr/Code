#include <iostream>

using namespace std;

int main(){
    int a[10] = { 7, 3, 4, 1, 9, 8, 10, 2, 5, 6 };
    int min = a[0];
    int max = a[0];
    for (int i = 0; i < 10; i++)
    {
        if (a[i] < min)
        {
            min = a[i];
        }
        if (a[i] > max)
        {
            max = a[i];
        }
    }
    cout << "Minimum: " << min << endl;
    cout << "Maximum: " << max << endl;
    return 0;
}