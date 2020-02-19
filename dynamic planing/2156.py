import itertools 
N=int(input())

wine_list=[]
max_wine=0
for _ in range(N):
    wine_list.append(int(input()))

dp=[0]
dp.append(wine_list[0])
if(N > 1):
    dp.append(wine_list[0]+wine_list[1])

for i in range(3,N+1):
    case_1= wine_list[i-1]+dp[i-2]
    case_2= wine_list[i-1]+wine_list[i-2]+dp[i-3]
    case_3= dp[i-1]

    max_value = max(case_1,case_2,case_3)
  


    dp.append(max_value)
    #print(dp)
print(dp[N])





