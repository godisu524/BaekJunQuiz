#include <stdio.h>
#include <algorithm>

using namespace std;

long long a[100005];
long long b[100005];
long long c[100005];
long long D[100005][2];

int main(){
    int N, n, i;
    long long temp;
    long long ans =0;
    
    scanf("%d", &N);
    for (i = 0; i<N; i++){
        scanf("%lld",&a[i]);
    }
    
    sort(a, a+N);
    b[0] = a[0];
    c[0] = 1;
    n=0;
    i=1;
    
    while (i<N){
        if (a[i-1] == a[i]){
            c[n]++;
        }
        else{
            n++;
            b[n]= a[i];
            c[n]=1;
        }i++;
    }
    n++;
    D[0][0] = 0;
    D[0][1] = (long long)b[0] * c[0];
    i=1;
    while(i<n){
        D[i][0] = D[i-1][0];
        if (D[i-1][1]> D[i][0])
            D[i][0]=D[i-1][1];
        D[i][1] = D[i-1][0] + b[i]*c[i];
        if (b[i-1] < b[i] -1 && temp > D[i][1])
            D[i][1] = temp;
        i++;
    }
    ans = D[n-1][0];
            if(D[n-1][1]>ans)
                ans = D[n-1][1];
    printf("%lld\n",ans);
    
}
