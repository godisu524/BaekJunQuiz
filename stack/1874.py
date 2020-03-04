n=int(input())
nlist=[]
temp=[]
answer=[]
for _ in range(n):
    nlist.append(int(input()))
nlist.reverse()
for a in range(1,n+1):
    temp.append(a)
    answer.append('+')
    while(True):
        if a == nlist[-1]:
            answer.append('-')
            temp.pop(-1)
            nlist.pop(-1)
            if len(temp)==0:
                break
            try:
                a=temp[-1]
            except:
                None
        else:
            break
if len(temp)==0:
    for a in answer:
        print(a)
else:
    print('NO')

        