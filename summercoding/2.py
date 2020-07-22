import random

def solution(n):
    ans=0
    
    count = 0
    answers=[]
    for a in range(n+1):
    
        temp = 0
        temp_ans= 0
        temp_ans = pow(3,a)
        answers.append(temp_ans)
        count+=1
        now=[]
        now2=[]
        while(temp < a):
            if temp_ans + pow(3,temp) not in now:
                now.append(pow(3,temp))
            temp+=1
        for b in now:
            answers.append(b+temp_ans)
            for c in now2:
                answers.append(b+c)
            now2.append(b+temp_ans)
        
            
    
    
    return answers[n-1]


print(solution(11))