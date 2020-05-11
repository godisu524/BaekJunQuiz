from collections import deque
import sys
input= sys.stdin.readline

M,N=map(int,input().strip().split())
answer =0

num_list= deque([_ for _ in range(1,M+1)])
find_list=list(map(int,input().strip().split()))


for a in find_list:

    if num_list.index(a) > len(num_list)//2:

        while(True):
            if(num_list[0]==a):
                break
            num_list.rotate(1)
            answer+=1
        num_list.popleft()
    else:

        while(True):
            if(num_list[0]==a):
                break
            num_list.rotate(-1)
            answer+=1
        num_list.popleft()
print(answer)
    

