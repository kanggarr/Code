// quick sort

#include <iostream>

using namespace std;

int partition(int a[], int p, int r)
{
    int x = a[r];
    int i = p - 1;
    for (int j = p; j <= r - 1; j++)
    {
        if (a[j] <= x)
        {
            i++;
            int temp = a[i];
            a[i] = a[j];
            a[j] = temp;
        }
    }
    int temp = a[i + 1];
    a[i + 1] = a[r];
    a[r] = temp;
    return i + 1;
}

void quicksort(int a[], int p, int r)
{
    if (p < r)
    {
        int q = partition(a, p, r);
        quicksort(a, p, q - 1);
        quicksort(a, q + 1, r);
    }
}

int main()
{
    int a[10] = { 7, 3, 4, 1, 9, 8, 10, 2, 5, 6 };
    quicksort(a, 0, 9);
    // for (int i = 0; i < 10; i++)
    // {
    //     cout << a[i] << " ";
    // }
    // cout << endl;
    cout << "Minimum: " << a[0] << endl;
    cout << "Maximum: " << a[9] << endl;
    return 0;
}