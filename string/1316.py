N=int(input())

words=[]
count=0

for a in range(N):
    words.append(input())
for a in words:
    count_flag=True
    collected_char=[]
    last_char=""
    for b in a:
        if b!=last_char:
            if b in collected_char:
                count_flag=False
                break
            else:
                collected_char.append(b)
        last_char=b
        
        
            
    if count_flag ==True:
        if a !=" ":
            count+=1
            
print(count)
        
                

