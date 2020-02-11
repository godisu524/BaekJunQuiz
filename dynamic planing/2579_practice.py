n=int(input())
sum_of_stairs=[]
sum_of_stairs.append(0)
scores_of_stairs=[]
scores_of_stairs.append(0)
for _ in range(n):
    scores_of_stairs.append(int(input()))

sum_of_stairs.append(scores_of_stairs[1])
sum_of_stairs.append(scores_of_stairs[1]+scores_of_stairs[2])
sum_of_stairs.append(max(scores_of_stairs[1]+scores_of_stairs[3],scores_of_stairs[2]+scores_of_stairs[3]))


for i in range(4,n+1):
    sum_of_stairs.append(max(scores_of_stairs[i]+sum_of_stairs[i-2],scores_of_stairs[i]+scores_of_stairs[i-1]+sum_of_stairs[i-3]))
print(sum_of_stairs[-1])





