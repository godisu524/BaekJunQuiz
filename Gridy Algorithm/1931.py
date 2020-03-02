schedules=[]

end=answer=0

for _ in range(int(input())):
    schedules.append(list(map(int,input().split())))
schedules.sort(key = lambda schedules:(schedules[1],schedules[0]))
usage=[]

for i in schedules:
    if end<=i[0]:
        end=i[1]
        answer+=1
#print(usage)

print(answer)
