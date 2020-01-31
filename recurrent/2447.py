def stars(n):
    matrix=[]
    ##len(n) =3
    for i in range(3 * len(n)):
        if i // len(n) == 1:
            
            matrix.append(n[i % len(n)] + " " * len(n) + n[i % len(n)])
        else:
            matrix.append(n[i % len(n)] * 3)
    return(list(matrix))

star = ["***","* *","***"]

n = int(input())
k = 0

#3의 몇승인지 아는거임..
while n != 3:
    n = int(n / 3)
    k += 1

    
for i in range(1):
    star = stars(star)
    print("########")
for i in star:
    print(i)