A= int (input())

A_list= list(map(int,input().split()))
result = [[] for _ in range(A)]

#순방향 돌려주기
for i in range(A):
    if i == 0 :
        result[i].append(A_list[i])
        print("1 0"+ str(result))
    else:
        for j in range(0,i):
            if result[j][-1] < A_list[i]:
                if len(result[i]) -1 <len (result[j]):
                    result[i] = result[j] + [A_list[i]]
                    print(result)
        if not result[i]:
            result[i].append(A_list[i])
            print("00"+str(result))
    


A_list_reversed = list(reversed(A_list))
result_reversed =[[] for _ in range(A)]

for i in range(A):
    if i == 0 :
        result_reversed[i].append(A_list_reversed[i])
        print("2 0"+ str(result_reversed))
    else:
        for j in range(0,i):
            if result_reversed[j][-1] < A_list_reversed[i]:
                if len(result_reversed[i]) -1 <len (result_reversed[j]):
                    result_reversed[i] = result_reversed[j] + [A_list_reversed[i]]
                    print(result_reversed)
        if not result_reversed[i]:
            result_reversed[i].append(A_list_reversed[i])
            print("11"+str(result_reversed))

answer= 0
for i in range(A):
    answer = max(answer, len(result[i])+len(result_reversed[-i-1]))

print (answer-1)
