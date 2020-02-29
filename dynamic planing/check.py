n=int(input())
origin=[0]
origin+=list(map(int,input().split()))
temp=[0 for _ in range(n+1)]
result=-1001

for i in range(1,n+1):
    temp[i]=max(temp[i-1]+origin[i], origin[i])
    result=max(result,temp[i])
print(result)
