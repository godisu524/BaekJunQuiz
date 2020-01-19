numbers=[0]*10001
def d(x):
    if x > 10000 :
        return None
    
    new_x=0
    for a in str(x):
        new_x+=int(a)
    new_x+=int (x)
    try:
        numbers[new_x]=1
    except:
        None
    
    
    


num=1
while (num<10000):
    
    d(num)
    num+=1


for n,a in enumerate(numbers):
    if a ==0:
        if n != 0:
            print(n)
