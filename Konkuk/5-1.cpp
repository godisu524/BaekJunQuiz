#include <stdio.h>

int D[5000]; // D[i] optimal count for length i

int main(){
    int n, a, b, c;
    int i;
    long long ans;
    scanf("%d %d %d %d", &n, &a, &b, &c);
    D[0] =0;
    for (i=1; i<=n ; i ++){
        if (i-a >=0) if(D[i-a] >=0) D[i]= D[i-a] +1;
        if (i-b >=0) if(D[i-b] >=0) if (D[i-b] +1 > D[i]) D[i] = D[i-b] +1;
        if (i-c >=0) if(D[i-c] >=0) if (D[i-c] +1 > D[i]) D[i] = D[i-c] +1;
    }
    ans = D[n];
    printf("%lld",ans);
}
