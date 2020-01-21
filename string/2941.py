words=["c=",'c-','dz=','d-','lj','nj','s=','z=']


n=input()
w_count=0
for a in words:
    if a in n:
        w_count+=n.count(a)
        n=n.replace(a,"/",n.count(a))
n=n.replace("/","")        
w_count+=len(n)
print(w_count)
