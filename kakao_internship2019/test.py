#include <iostream>
#include <map>
#include <algorithm>

int main(){

    const string initial = "polycarp";
    map<string, long> rank;
    rank[initial] = 1;

    long n; scanf("%ld\n", &n);
    long length(0);
    while(n--){
        string to, action, from; cin >> to >> action >> from;
        transform(from.begin(), from.end(), from.begin(), ::tolower);
        transform(to.begin(), to.end(), to.begin(), ::tolower);
        rank[to] = rank[from] + 1;
        if(rank[to] > length){length = rank[to];}
    }

    cout << length << endl;
    return 0;
}
