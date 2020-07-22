def solution(numbers):
    numbers = list(map(str, numbers))
    print(numbers)
    numbers=["666","101010","222"]
    numbers.sort(key=lambda x: x*3, reverse=False)
    
    print(numbers)

    return str(int(''.join(numbers)))





print(solution([6, 10, 2]))