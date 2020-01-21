N= int(input())
h_num=0
for a in range(1,N+1):
    if a <=99:
        h_num+=1

    else:
        nums= list(map(int,str(a)))
        if nums[0]-nums[1] == nums[1] -nums[2]:
            h_num+=1

print(h_num)
