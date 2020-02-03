N, M = map(int, input().split())

num_list = [i + 1 for i in range(N)]
check_list = [False] * N

arr = []

def dfs(cnt):
    if(cnt == M):
        print(*arr)
        return
    
    for i in range(0, N):
        if(check_list[i]):
            continue
        arr.append(num_list[i])
        dfs(cnt + 1)
        check_list[i] = True
        arr.pop()
        
        for j in range(i + 1, N):
            check_list[j] = False
        
dfs(0)