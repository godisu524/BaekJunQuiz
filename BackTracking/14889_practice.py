from itertools import combinations as cm
import math

n = int(input())
#datas = [list(map(int,input().split())) for _ in range(n)]
datas=[
    [0, 5, 4, 5, 4,5, 4, 5],
[4, 0, 5, 1, 2, 3, 4, 5],
[9, 8, 0, 1, 2, 3, 1, 2],
[9, 9, 9, 0, 9, 9, 9, 9],
[1, 1, 1, 1, 0, 1, 1, 1],
[8, 7, 6, 5, 4, 0, 3, 2],
[9, 1, 9, 1, 9, 1, 0, 9],
[6, 5, 4, 3, 2, 1, 9, 0]
]
min_ans=math.inf	# 정답

for case in cm(range(1,n+1),n//2):	# 두 팀으로 나눌 수 있는 경우의 수
    s1 = s2 = 0
    
    for i in case:	# 1팀 점수
        for j in case:
            s1+=datas[i-1][j-1]

    res = set(range(1, n + 1)) - set(case)	# 2팀 점수
    for i in res:
        for j in res:
            s2+=datas[i-1][j-1]
    min_ans=min(min_ans,abs(s1-s2))
print(min_ans)