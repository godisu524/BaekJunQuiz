#include <iostream>

using namespace std;

int main()
{
    int m;
    cin >> m;
    if (m % 2 == 0 && m > 2)
    {
        cout << "YES" << endl;
    }
    else
    {
        cout << "NO" << endl;
    }
    return 0;
}