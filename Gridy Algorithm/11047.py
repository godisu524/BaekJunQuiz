n,m = map(int,input().split())
coins=[]
count=0
for a in range(n):
    coins.append(int(input()))

while(True):
    for i in range(n,0,-1):
        #print(coins,i)
        if (m//coins[i-1]) != 0:
            count+= m//coins[i-1]
            #print(m)
            m-=(coins[i-1]*(m//coins[i-1]))
            #print(m)
        if m==0:
            print(count)
            break

    break