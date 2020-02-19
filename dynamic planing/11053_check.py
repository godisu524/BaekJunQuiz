def _11053():
    N = int(input())
    dp = [0] * (N)
    A = list(map(int, input().split(' ')))
    Max = 0

    for i in range(0, N):
        min = 0
        for j in range(0, i):
            #전에 꺼 보다 크면 전에꺼랑 이어나가고 +1 작업. 신기하네 ㅇㅋㅇㅋ
            if A[i] > A[j] :
                if min < dp[j]:
                    min = dp[j]
        dp[i] = min + 1
        if Max < dp[i]:
            Max = dp[i]
    print(max(dp))

_11053()