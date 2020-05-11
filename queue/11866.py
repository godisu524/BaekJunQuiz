import sys
from collections import deque

input = sys.stdin.readline

N,K= input().split()
N=int(N)
K=int(K)

round_list=deque([_ for _ in range(1,N+1)])

answer=[]
round_list.rotate(-K+1)
answer.append(round_list[0])

round_list.popleft()
round_list.rotate(-K+1)

while(len(round_list)!=0):
    answer.append(round_list[0])
    round_list.popleft()
    round_list.rotate(-K+1)

answer_str='<'
for a in answer:
    answer_str+=str(a)+', '
answer_str=answer_str.strip(', ')
answer_str+='>'

print(answer_str)