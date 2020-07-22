from collections import Counter
from functools import reduce
def solution(clothes):
    return(reduce(lambda x,y:x*y,[a+1 for a in Counter([x[1] for x in clothes]).values()]))-1
    




print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))