import sys
input= sys.stdin.readline
n=int(input().strip())
numbers=[]
for _ in range(n):
    m=int(input().strip())
    if m == 0:
        numbers.pop(-1)
    else:
        numbers.append(m)
print(sum(numbers))