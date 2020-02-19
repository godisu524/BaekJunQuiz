n=int(input())
wine_list=[int(input()) for i in range(n)]

dp=[0]
dp.append(wine_list[0])
dp.append(wine_list[0]+wine_list[1])

for i in range(3,n+1):
    case1= wine_list[i-1]+dp[i-2]
    case2= wine_list[i-1]+wine_list[i-2]+dp[i-3]
    case3= dp[i-1]

    dp.append(max(case1,case2,case3))
print(dp[n])