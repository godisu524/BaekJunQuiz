n=int(input())
sets=[]
for a in range(n):
    n_set=list(map(int,input().split(" ")))
    sets.append(n_set)
sets.sort(key=lambda x: (x[0], x[1]))

for a in sets:
    print(a[0],a[1])
