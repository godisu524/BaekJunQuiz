#include <cstdio>
#include <vector>
#include <stdio.h>

using namespace std;

vector<int> Edges[200005];
bool Visit[200005];


class node{ 
    public:
    int cnt, dist;
    bool operator< (const node& a) const{
        return dist - cnt< a.dist - a.cnt;
    }
}a[200005];


int dfs(int pos){
    //a[pos].dist <--known
    //Edges[pos][0]
    int i, k;
    k = Edges[pos].size();
    int count = 0;
    Visit[pos] = true;
    for (i= 0; i<k; i++){
        if (!Visit[Edges[pos][i]]){
            a[Edges[pos][i]].dist = a[pos].dist+1;
            
            count += dfs(Edges[pos][i]);
        }
    }
    a[pos].cnt = count;
    return count+1;
};
int main(){
    long long ans;
    int n, k, p, q;
    int i, j;
    
    scanf("%d %d", &n, &k);
    for (i = 1; i<n; i++){
        scanf("%d %d", &p, &q);
        Edges[p].push_back(q);
        Edges[q].push_back(p);
    }
//#Visit[0] = true;
    dfs(1);
    a[1].dist = 0;
    sort(a+1,a+n+1);
    ans=0;
    for (j= n; j>n - k;j--){
        ans+=a[j].dist- a[j].cnt;
    }
    printf("%lld\n",ans);
    
    return 0;
}
