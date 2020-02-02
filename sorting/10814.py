N = int(input())
users=[]
for _ in range(N):
    users.append(list(map(str,input().split(' '))))
users.sort(key= lambda x: [int(x[0])])
for a in users:

    print (a[0]+" "+ a[1])
