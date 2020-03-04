#eval 은 012 같은거는 처리를 못함.

minus_list=list(map(str,input().split('-')))

#print(eval(line))
answer=0
for i,a in enumerate(minus_list):
    temp=sum(list(map(int,a.split('+'))))
    if i==0:
        answer+=temp
    else:
        answer-=temp
print(answer)