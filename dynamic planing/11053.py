N=int(input())
dp=[0]*N
numbers=list(map(int,input().split()))

for i in range(N):
    min=0
    for j in range(i):
        if numbers[i]>numbers[j]:
            if min <dp[j]:
                min=dp[j]
    dp[i]=min+1

print(dp[-1])