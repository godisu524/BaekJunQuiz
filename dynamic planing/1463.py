n=int(input())
def cal(a):
    _list=[]
    for n in a:
        _list.append(n-1)
        if n%2==0:
            _list.append(n/2)
        if n%3 ==0:
            _list.append(n/3)
    return _list

minimum=[n]
count=0
while(True):
    if n == 1:
        print(count)
        break
    temp=minimum[:]
    minimum=[]
    minimum=cal(temp)
    count+=1
    if min(minimum)==1:
        print(count)
        break
        

    


