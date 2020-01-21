times=input()
results=[]
for a in range(int(times)):
    N=input()
    string=""
    for a in N.split(' ')[1]:
        string+=a*(int(N.split(' ')[0]))
    results.append(string)
for a in results:
    print(a)