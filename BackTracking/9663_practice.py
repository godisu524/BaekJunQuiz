n,ans=int(input()),0
a,b,c= [False]* n, [False]* (2*n-1),[False]* (2*n-1)

def dfs(i):
    global ans
    if i==n:
        ans+=1
        return
    for j in range(n):
        if not(a[j] or b[i+j] or c[i-j+n-1]):
            a[j]=b[i+j]=c[i-j+n-1]=True
            dfs(i+1)
            a[j]=b[i+j]=c[i-j+n-1]=False
dfs(0)
print(ans)

