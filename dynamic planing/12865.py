N,K = map(int, input().split())

storage=[[0,0]]
knapsack = [[0 for _ in range(K+1)] for _ in range(N+1)]

for _ in range(N):
    storage.append(list(map(int, input().split())))


for i in range(1,N+1):
    for j in range(1,K+1):
        weight=storage[i][0]
        price=storage[i][1]

        if j<weight :
            knapsack[i][j]=knapsack[i-1][j]
        else:
            #이전 가방의 이전가치 , 이전 가방의 현재가치 
            knapsack[i][j]=max(price+knapsack[i-1][j-weight],knapsack[i-1][j])
print(knapsack[N][K])


