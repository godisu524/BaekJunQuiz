import sys
input = sys.stdin.readline
from collections import deque

numbers = deque([_ for _ in range(1,int(input().strip())+1)])



while (len(numbers)!=1):
    
    numbers.popleft()
    numbers.rotate(-1)
    

print(numbers[0])


