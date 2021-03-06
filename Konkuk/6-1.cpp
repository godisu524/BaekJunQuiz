#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(){

    
    long n;
    cin >> n;
    vector<long> c(n);
    for(long p = 0; p < n; p++){cin >> c[p];}
    vector<string> s(n);
    for(long p = 0; p < n; p++){cin >> s[p];}

    vector<vector<long long> > dp(n, vector<long long>(2, 0));
    dp[0][0] = 0; dp[0][1] = c[0];
    for(int p = 1; p < n; p++){
        string rr = s[p - 1]; reverse(rr.begin(), rr.end());
        string rc = s[p];     reverse(rc.begin(), rc.end());

        long long candA(-1), candB(-1);
        if(s[p - 1] <= s[p] && dp[p - 1][0] >= 0){candA = dp[p - 1][0];}
        if(rr <= s[p] && dp[p - 1][1] >= 0){candB = dp[p - 1][1];}

        if(candA >= 0 && candB >= 0){dp[p][0] = (candA < candB) ? candA : candB;}
        else if(candA >= 0){dp[p][0] = candA;}
        else if(candB >= 0){dp[p][0] = candB;}
        else{dp[p][0] = -1;}

        candA = candB = -1;
        if(s[p - 1] <= rc && dp[p - 1][0] >= 0){candA = dp[p - 1][0] + c[p];}
        if(rr <= rc && dp[p - 1][1] >= 0){candB = dp[p - 1][1] + c[p];}

        if(candA >= 0 && candB >= 0){dp[p][1] = (candA < candB) ? candA : candB;}
        else if(candA >= 0){dp[p][1] = candA;}
        else if(candB >= 0){dp[p][1] = candB;}
        else{dp[p][1] = -1;}
    }

    long long ans;
    if(dp[n - 1][0] >= 0 && dp[n - 1][1] >= 0){ans = (dp[n - 1][0] < dp[n - 1][1]) ? dp[n - 1][0] : dp[n - 1][1];}
    else if(dp[n - 1][0] >= 0){ans = dp[n - 1][0];}
    else if(dp[n - 1][1] >= 0){ans = dp[n - 1][1];}
    else{ans = -1;}

    cout << ans << endl;

    return 0;
}
