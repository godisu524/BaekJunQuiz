N = int(input())
students=[]
students_2=[]
for a in range (N):
    students.append(list(map(int,input().split(' '))))
for a in students:
    students_2.append(a)
#students.sort(key = lambda x: (x[0], x[1]))
for n,a in enumerate(students):
    count=1
    for i,b in enumerate(students): 
        if i == n:
            continue
        #print(a,b)
        if a[0] <b[0]:
            if a[1]<b[1]:
                count+=1
        
    print(count)


