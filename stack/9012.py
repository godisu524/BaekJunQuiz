import sys
input=sys.stdin.readline

n=int(input().strip())

line=[]

for _ in range(n):
    a=input().strip()

    temp=[]
    answer="YES"
    for b in a:
        if b=="(":
            temp.append("(")
        else:
            try:
                if temp[-1]=="(":
                    temp.pop(-1)
                else:
                    answer='NO'
                    break
            except:
                answer='NO'
                break
    if len(temp)!=0:
        answer='NO'
    print(answer)
    