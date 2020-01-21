num_list=[]
for a in range(9):
    num_list.append(input())
max_num=num_list[0]
max_index=0
for n,a in enumerate(num_list):
    if a > max_num:
        max_num= a
        max_index=n
print (max_num)
print(max_index+1)