from itertools import combinations
##combination // permutation 다른적 알아두기
#이거는 맞는데 시간복잡도에서 ㅆㅎㅌㅊ
def solution2(number, k):
    answer = ''
    Allnumber = list(map(''.join, combinations(number,len(number)-k)))
    
    
                    
    answer=max(Allnumber)
    return answer







def solution(number, k):
    collected = []  
    for i, num in enumerate(number):
        print(collected)
        while len(collected) > 0 and collected[-1] < num and k > 0:
            print(collected)
            collected.pop() 
            k -= 1
        if k == 0:
            collected += list(number[i:])
            print(list(number[i:]))
            print(i)
            print(collected)
            break
        collected.append(num)
    collected = collected[:-k] if k > 0 else collected
  
    answer = ''.join(collected)
    return answer


print(solution("4177252841",4))