N, M = map(int, input().split())
card = list(map(int,input().split(' ')))
answer = 0
for i in range(0, N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            if (card[i]+card[j]+card[k]) <= M and M - (card[i]+card[j]+card[k]) < M - answer:
                answer = card[i]+card[j]+card[k]
print(answer)
