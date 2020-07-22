from itertools import permutations
import math

def check(n):
    k = math.sqrt(n)
    if n < 2: 
        return False

    for i in range(2, int(k)+1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    answer = []
    for k in range(1, len(numbers)+1):
        #permutation 에 숫자를 넣어서 몇개를 할건지 정하룻 있다,
        perlist = list(map(''.join, permutations(list(numbers), k)))
        for i in list(set(perlist)):
            if check(int(i)):
                answer.append(int(i))

    answer = len(set(answer))

    return answer