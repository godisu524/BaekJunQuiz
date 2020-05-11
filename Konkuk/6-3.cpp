#include<stdio.h>

#define MAX(a,b) (((a)>(b))?(a):(b))
#define MIN(a,b) (((a)<(b))?(a):(b))

int NN[100005];
int m[100005];
int n;
int ans;
int a,ac,b,bc,i,j,k;


int solve(){
    if(n==1) return 1;
    for (k=2; k<=n; k++)
        if (NN[k] !=NN[k-1]) break;
    if (k== n+1) return n;
    i =1; j=k+1;
    a= MIN(NN[k-1],NN[k]);
    b= MAX(NN[k-1],NN[k]);
    m[k]=k;
    
    if (b==NN[k]){
        bc=1;
        ac=k-1;
    }else{
        ac=1; bc=k-1;
    }
    while(1){
        while(j<=n){
            if( NN[j] == a) {
                ac++;
                m[j]= j-i+1;
                j++;
            }
            else if(NN[j]==b){
                bc++;
                m[j]=j-i+1;
                j++;
            }else
                break;
        }
        if (j==n+1)
            break;
        if (NN[j] == a-1){
            while(bc!=0) {
                if(NN[i]==a){
                    ac--;
                    i++;
                }
                else{
                    bc--;
                    i++;
                }
                a = b;
                ac= bc;
                b= b+1;
                bc= 1;
            }
        }else{//NN[j] == b+1;
            while(ac!=0) {
                if( NN[i] ==a) {
                    ac--;
                    i++;
                }else{
                    bc--;
                    i++;
                }
            }
            a=b;
            ac=bc;
            b=b+1;
            bc=1;
        }
    }
    
    ans= m[1];
    for (k=2;k<=n; k++){
        ans= MAX(ans,m[k]);
    }
    
    return ans;
}


int main(){
    scanf("%d",&n);
    for(k=1; k<=n;k++)
        scanf("%d", &NN[k]);
    ans=solve();
    printf("%d\n",ans);
   
}
