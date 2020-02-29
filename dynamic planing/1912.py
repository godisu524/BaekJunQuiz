N= int(input())
n_list=[0]
n_list+=list(map(int,input().split()))
dp=[0 for _ in range(N+1)]
#print(dp)
#애초에 최대값이 음수일수 있다...
Max=-1000000
for i in range(1,N+1):
    dp[i]=max(dp[i-1]+n_list[i],n_list[i])
    Max=max(dp[i],Max)

print(Max)     



