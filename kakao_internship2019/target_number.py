def solution(numbers, target):
    answer = 0
    
    def operator(numbers, target, index=0):
        if index < len(numbers):
            numbers[index] *= 1
            operator(numbers,target, index+1)

            numbers[index] *= -1
            operator(numbers,target, index+1)

        elif sum(numbers) == target:
            nonlocal answer
            answer+=1
    operator(numbers,target)


    return answer

        






print(solution([1, 1, 1, 1, 1],	3))