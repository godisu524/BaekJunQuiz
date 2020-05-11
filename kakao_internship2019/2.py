s="{{3},{4,3},{5,2,3,4},{2,3,4}}"
_list = []
s= s.replace("{{",'{',1)
s= s.replace("}}",'}',1)
s= s.replace("},{",'}.{')
n_s = []
for a in s.split('.') :
    temp= []
    a=a.replace("{",'')
    a=a.replace("}",'')
    for b in a.split(','):
        temp.append(int(b))
    n_s.append(temp)
n_s.sort(key = len)
answer = []

for a in n_s:
    if len(a) == 1:
        answer.append(a[0])
    else:
        for i in a:
            if i not in answer:
                answer.append(i)

           
        


    
print(answer)
#print(answer)
#print(list(answer))
