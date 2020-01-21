numbers=[]
range_num=int(input())
for a in range(range_num):
    numbers.append(int(input()))

for i in range(len(numbers)) : 
    for j in range(len(numbers)) : 
        if numbers[i] < numbers[j] : 
            numbers[i], numbers[j] = numbers[j], numbers[i]


for a in numbers:
    print(a)




