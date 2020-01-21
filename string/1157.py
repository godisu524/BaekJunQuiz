N= input()
N=N.upper()
alphapet=""
for a in range(ord('A'),ord('Z')+1):
    alphapet+=chr(a)

max_string=""
max_count=-1
max_flag=False

for a in alphapet:
    
    
    if N.count(a) >max_count and a != max_string:
        max_count=N.count(a)
        
        max_string= a
        max_flag=False
        
    elif N.count(a) == max_count and a != max_string:
        max_flag=True
        
if max_flag==True:
    print("?")
else:
    print(max_string)