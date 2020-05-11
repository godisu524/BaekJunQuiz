from collections import deque
n=int(input())
for i in range(n):
    N,M=map(int,input().split())
    u_list=deque(list(map(int,input().split())))
    index_list=deque([_ for _ in range(N)])
    answer=0
    while(len(u_list)!=0):
        if u_list[0] == max(u_list):
            u_list.popleft()
            answer+=1
            if index_list[0]==M:
                print(answer)
                break
            index_list.popleft()
        else:
            u_list.rotate(-1)
            index_list.rotate(-1)
        


