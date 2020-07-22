from collections import deque

def solution(progresses, speeds):
    answer = []

    q=deque(progresses)
    p=deque(speeds)
    while(q):
        #print(p,q)
        temp_progress=q.popleft()
        temp_speed=p.popleft()
        day =0
        p_count=1
        while(temp_progress<100):
            temp_progress+=temp_speed
            day+=1
        while(q):
        #for i in range(len(q)):
            #print(i)
            if (q[0]+p[0]*day) >=100:
                p_count+=1
                q.popleft()
                p.popleft()
            #    i-=1
            else:
                break
        for i in range(len(q)):
            q[i]+=p[i]*day
        answer.append(p_count)


            
        
        

    return answer



print(solution([93,30,55],[1,30,5]))