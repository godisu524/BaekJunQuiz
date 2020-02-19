A = int(input())
A_list = list(map(int, input().split()))
result = [[] for _ in range(A)]


#순방향 돌려주기
for i in range(A):
    if i == 0:
        result[i].append(A_list[i])
    else:
        for j in range(0, i):
            if result[j][-1] < A_list[i]: #이전 수열의 마지막 숫자가 나보다 작은가?
                if len(result[i]) - 1 < len(result[j]): #수열의 길이가 현재값보다 작은가?
                    result[i] = result[j] + [A_list[i]]
        if not result[i]:
            result[i].append(A_list[i]) #자신이 지금까지 최소값일 경우

#역방향 돌려주기
A_list_reversed = list(reversed(A_list))
result_reversed = [[] for _ in range(A)]

for i in range(A):
    if i == 0:
        result_reversed[i].append(A_list_reversed[i])
    else:
        for j in range(0, i):
            if result_reversed[j][-1] < A_list_reversed[i]:
                if len(result_reversed[i]) - 1 < len(result_reversed[j]):
                    result_reversed[i] = result_reversed[j] + [A_list_reversed[i]]
        if not result_reversed[i]:
            result_reversed[i].append(A_list_reversed[i])


#합산해서 가장 큰 숫자 산출
answer = 0
for i in range(A):
    answer = max(answer, len(result[i]) + len(result_reversed[-i-1]))

    
print(answer - 1) #가운데 숫자는 두 번 더해지므로 -1