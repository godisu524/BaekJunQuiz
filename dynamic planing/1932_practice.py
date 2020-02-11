N=int(input())

triangle=[list(map(int,input().split())) for _ in range(N)]
dp=triangle.copy()
for i in range(N-1):
    for j in range(len(triangle[i+1])):
        if j ==0:
            dp[i+1][j]=dp[i][j]+dp[i+1][j]
        elif j==(len(dp[i+1])-1):
            dp[i+1][-1]=dp[i][-1]+dp[i+1][j]
        else:
            #j 자체가 한개 이미 오른쪽인상황
            dp[i+1][j]=max(dp[i][j-1]+dp[i+1][j],dp[i][j]+dp[i+1][j])
print(max(dp[-1]))
