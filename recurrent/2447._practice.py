star =["***","* *", "***"]
def stars(n):
    matrix=[]
    for a in range(3*len(n)):
        if a//len(n) ==1:
            matrix.append(n[a%len(n)] + " "*len(n) + n[a%len(n)])
        else:
            matrix.append(n[a%len(n)]*3)
    return list(matrix)
n= int(input())
k=0
while n!=3:
    n=int(n/3)
    k+=1
for a in range(k):
    star=stars(star)
for a in star:
    print(a)






