#include <cstdio>
#include <vector>
#include <stdio.h>

using namespace std;

vector<int> Edges[200005];
vector<int> fromCh[200005];
bool Visit[200005];


class node{
    public:
    int bw, upMax, ans;
}a[200005];


int dfs(int pos){
    
    int thisChild;
    a[pos].upMax = 0;
    int i, k;
    k = Edges[pos].size();
    
    Visit[pos] = true;
    for (i= 0; i<k; i++){
        if (!Visit[Edges[pos][i]]){
            thisChild = dfs(Edges[pos][i]);
            fromCh[pos][i] = thisChild;
            if (thisChild != -1) a[pos].upMax += thisChild;
        }
    }
    if (a[pos].bw) a[pos].upMax++;
    else a[pos].upMax--;
    return a[pos].upMax;
};



int dfs2(int pos,int fP){
 
    int i, k;
    k = Edges[pos].size();
    Visit[pos] = true;
    
    if (fP!= -1) a[pos].ans = a[pos].upMax + fP;
    else  a[pos].ans = a[pos].upMax;
    
    for (i= 0; i<k; i++){
        if (!Visit[Edges[pos][i]]){
            if (fromCh[pos][i] == -1) dfs2(Edges[pos][i], a[pos].ans);
            else dfs2(Edges[pos][i],a[pos].ans - fromCh[pos][i]);
        }
    }
    return 0;
};

int main(){
    
    int n, p, q;
    int i;
    
    scanf("%d", &n);
    for (i = 1; i<=n; i++){
        scanf("%d", &(a[i].bw));
    }
    for (i = 1; i<n; i++){
        scanf("%d %d", &p,&q);
        Edges[p].push_back(q);
        Edges[q].push_back(p);
        fromCh[p].push_back(0);
        fromCh[q].push_back(0);
    }
//#Visit[0] = true;
    dfs(1);
    for (i = 1; i<=n; i++) Visit[i]=0;
    dfs2(1,0);
    for (i =1; i<=n; i++){
       printf("%d\n", a[i].ans);
    }
    
    
    return 0;
}
