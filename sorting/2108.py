numbers = int(input())
number_list = list(map(int, input().split()))

max_num = number_list[0]
min_num = number_list[0]
for num in number_list:
    
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num

print(min_num, max_num)