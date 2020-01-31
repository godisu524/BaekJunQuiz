def hanoi (plate,start,mid,end):
    if plate==1:
        print(start,end)
    else:
        hanoi(plate-1,start,end,mid)
        print(start,end)
        hanoi(plate-1,mid,start,end)
total_movement=0
n=int(input())
for a in range(n):
    total_movement=total_movement*2
    total_movement+=1
print(total_movement)
hanoi(n,1,2,3)
