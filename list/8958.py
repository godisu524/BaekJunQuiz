N= int(input())
ox_list=[]
for a in range(N):
    ox_list.append(input())
for a in ox_list:
    o_count=0
    score=0
    for b in a:
        
        if b=="O":
            o_count+=1
            score+=o_count
        else:
            o_count=0
    print(score)
