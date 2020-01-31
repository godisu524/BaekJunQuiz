count = int(input())
n1=0
n2=1

def Pibonach(n1,n2,n_count):
    if n_count== count:
        return n2
    if count ==0:
        return 0
    if count==1:
        return n1
    elif count== 2:
        return n2
    else:
        return Pibonach(n2,n1+n2,n_count+1)
        
print(Pibonach(n1,n2,1))