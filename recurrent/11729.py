def hanoi(disk, start, mid, end):
    print("disk:"+str(disk) ,"start:"+str(start),'mid:'+str(mid),"end:"+str(end))
    if disk == 1:
        print("disk==1 and end")
        print(start, end)
    else:
        
        hanoi(disk - 1, start, end, mid)
        print("returned)""disk:"+str(disk) ,"start:"+str(start),'mid:'+str(mid),"end:"+str(end))
        print(start, end)
        print("its going to end with no return")
        hanoi(disk - 1, mid, start, end)

total_disk = int(input())
total_mvmt = 0


#movement = 2^n -1
for disk in range(total_disk):
    total_mvmt = total_mvmt * 2
    total_mvmt += 1

print(total_mvmt)
hanoi(total_disk, 1, 2, 3)