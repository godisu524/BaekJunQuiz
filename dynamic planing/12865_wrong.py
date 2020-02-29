user_input=list(map(int,input().split()))
n,m =user_input[0],user_input[1]

dp=[[0] for _ in range(n)]
#print(dp)
storage=[]

for _ in range(n):
    storage.append(list(map(int,input().split())))
#test_list.sort(key = lambda test_list: test_list[1])
storage.sort(key= lambda storage: storage[1])
#print(storage)
Max=0
for i in range(n):
    
    weight=0
    for _ in range(n):
        dp[i].append(storage[i].copy())
    #print(dp,i)
    #print(storage,i)
    for j in range(1,n+1):

        if (j-1)==i:
            continue
        #print("dp",dp[i][j][0])
        #print("storage",storage[j-1][0])
        if (dp[i][j][0]+storage[j-1][0])<=m:
            dp[i][j][1]+=storage[j-1][1]
            dp[i][j][0]+=storage[j-1][0]
        #print(dp)
        if Max <dp[i][j][1]:
            Max= dp[i][j][1]
    
        
    
print(Max)

    
