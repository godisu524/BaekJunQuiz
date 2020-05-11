from collections import deque
import sys
input=sys.stdin.readline

N=int(input().strip())
R_count=0
for _ in range(N):
    error=False
    string=input().strip()
    num=int(input().strip())
    temp=input().strip()
    num_list=deque()
    
    for a in temp.split(','):
        try:
            num_list.append(int(a))
        except:
            None
    for a in string:
        print(num_list)
        if a =="R":
            R_count+=1
            
            
        elif a == "D":
            if len(num_list)==0:
                error=True
                break
            if R_count % 2 ==0:
                num_list.popleft()
            else:
                num_list.pop()
    if error==False:
        if R_count %2 ==0:
            answer=str(list(num_list))
            answer=answer.replace(', ',',')
            print(answer)
        else:
            answer=str(list(reversed(num_list)))
            answer=answer.replace(', ',',')
            print(answer)
    else:
        print('error')



