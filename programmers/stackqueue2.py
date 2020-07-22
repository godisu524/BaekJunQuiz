from collections import deque

def solution(heights):
    answer = []

    for i in range(len(heights)-1,-1,-1):
        temp=0
        for j in range(i-1,-1,-1):
  #          print(i,j)
            if heights[i]<heights[j]:
                temp=j+1
                break
        answer.append(temp)
    answer.reverse()
 #   print(answer)

    return answer
#[0,0,2,2,4]




print(solution([3,9,9,3,5,7,2]))