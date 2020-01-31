n=int(input())
words=[]
for a in range(n):
    word=input()
    if word not in words:
        words.append(word)
words.sort()
words.sort(key=len)

for a in words:
    print(a)