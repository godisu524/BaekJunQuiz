def solution(p):
    answer = 0
    answer = p+1

    

    while True:
        if len(set(list(str(answer)))) == len(str(answer)):
            return answer
        else:
            answer +=1

print(solution(2016))