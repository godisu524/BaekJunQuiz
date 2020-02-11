a= int(input())

zeros=[1,0,1]
ones= [0,1,1]

def fibofibo(num):
    length=len(zeros)
    if length<=num:
        for i in range(length,num+1):
            zeros.append(zeros[i-1]+zeros[i-2])
            ones.append(ones[i-1]+ones[i-2])    
    print("%d %d"%(zeros[num],ones[num]))

for i in range(a):
    k=int(input())
    fibofibo(k)
