def solution(brown, yellow):
    answer = []
    new_b=brown+4
    for i in range(2,new_b//2):
        print(i)
        a,b = i,new_b//2-i
        print(a,b)
        if (a-2)*(b-2) == yellow:
            answer = [a,b]
            break
    answer.sort(reverse=True)
    return answer


print(solution(10,2))