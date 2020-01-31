N=(input())
n= list(map(int,N))
N=int(N)


answer=0
for a in range(N):
    sum=a
    for b in list(map(int,str(a))):
        sum+=b
    if sum==N:
        answer=a
        break
print(answer)
    
        
    
    

    

