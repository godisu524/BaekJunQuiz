//
//  4-1_painting.cpp
//  Algorithm_practice
//
//  Created by 1thefull on 2020/04/30.
//  Copyright © 2020 1thefull. All rights reserved.
//


#include <stdio.h>

int a[5005];

int solve(int i, int j){
    int k, vans, hans, mini, s, t ;
    vans = j-i +1;
    mini = a[i];
    for (k= i+1; k<=j; k++){
        if (mini >a[k])
            mini = a[k];
    }
    for(k=i; k<=j; k++) a[k] -= mini;
    hans = mini;
    for (k = i; k<=j ;){
        if (a[k] == 0 && k <= j) {k++;}
        else{
            s = k;
            t = s;
            while( a[t] !=0 && t <=j)
                t++;
            hans += solve(s, t-1);
            k = t;
            
        }
      
    }
    if (vans<hans) return vans;
    else return hans;
    
};


int main()
{
    int n,i;
    int ans;
    scanf("%d",&n);
    for (i=1; i<=n; i++)
        scanf("%d", &a[i]);
    ans = solve(1,n);
    printf("%d\n",ans);
    
}

