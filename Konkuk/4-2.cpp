#include <iostream>
#include <stdio.h>

using namespace std;

string f(int x){

    if(x == 0){return "0";}
    if(x == 1){return "1";}
    char middle = '0' + (x % 2);
    return f(x/2) + middle + f(x / 2);
}


int main(){

    int n, l, r; std::cin >> n >> l >> r;
    string s = f(n);
    int count(0);
    for(long p = l - 1; p < r; p++){count += (s[p] - '0');}
    std::cout << count << std::endl;

    return 0;
}
