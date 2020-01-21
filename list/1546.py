N= int(input())

numbers=input()
num_list=list(map(int,numbers.split(" ")))
sum=0
max=0
for a in num_list:
    if a > max:
        max =a
    sum+=a
print((sum/max*100)/N)
