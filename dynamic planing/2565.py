A = int(input())
A_list = []
for a in range(A):
    A_list.append(list(map(int, input().split())))
result = [[] for _ in range(A)]
Max=0

A_list.sort()
#print(A_list)
#순방향 돌려주기
for i in range(A):
    if i == 0:
        result[i].append(A_list[i])
    else:
        for j in range(0, i):
            if result[j][-1][-1] < A_list[i][-1]: #이전 수열의 마지막 숫자가 나보다 작은가?
                if len(result[i]) - 1 < len(result[j]): #수열의 길이가 현재값보다 작은가?
                    result[i] = result[j] + [A_list[i]]
        if not result[i]:
            result[i].append(A_list[i]) #자신이 지금까지 최소값일 경우
    if len(result[i])>Max:
        Max= len(result[i])
        

#print(result)
#print(Max)
print(A-Max)

