n=int(input())

numbers=list(map(int,input().split()))
numbers.sort()
answer=0
temp=0
for a in numbers:
    temp+=a
    answer+=temp
    
print(answer)
     