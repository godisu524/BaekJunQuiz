num_list=[]
for a in range(3):
    num_list.append(int(input()))
mult=1
for a in num_list:
    mult *=a
mult=list(str(mult))
for a in range(10):
    print((mult).count(str(a)))
    
