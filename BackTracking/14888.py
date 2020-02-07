from itertools import permutations as pm

n = int(input())
nums = list(map(int,input().split()))
opers = list(map(int,input().split()))

# 입력받은 명령어 저장
op=''
for idx,oper in enumerate(opers):
    op+=str(idx)*oper

op=list(map(int,op))
res_list=[]
for now_op in set(pm(op,len(op))):	# 경우의 수(중복 제거)
    res = nums[0]
    for idx in range(n-1):
        if now_op[idx] == 0:
            res+= nums[idx + 1]
        elif now_op[idx] == 1:
            res-= nums[idx + 1]
        elif now_op[idx] == 2:
            res *=nums[idx + 1]
        elif now_op[idx] == 3:
            res = res//nums[idx + 1] if res>0 else ((res*-1)//nums[idx+1])*-1	# 음수 나누기 조심
    res_list.append(res)

print(max(res_list))
print(min(res_list))