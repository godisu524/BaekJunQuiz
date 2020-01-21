dial_numbers=["ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"]
word=input()
time=0
for a in word:
    for n,b in enumerate(dial_numbers):
        if a in b:
            time+=n+3
print(time)