n=int(input())
cost_per_home=[]
for _ in range(n):
    cost_per_home.append(list(map(int,input().split())))

dp=[cost_per_home[0]]
for i in range(1,n):
    color_cost=[]
    Red=min(dp[i-1][1],dp[i-1][2])
    color_cost.append(Red+cost_per_home[i][0])
    Blue=min(dp[i-1][0],dp[i-1][2])
    color_cost.append(Blue+cost_per_home[i][1])
    Green=min(dp[i-1][0],dp[i-1][1])
    color_cost.append(Green+cost_per_home[i][2])

    dp.append(color_cost)
print(min(dp[n-1]))
