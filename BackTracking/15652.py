N, M = map(int, input().split())

num_list = [i + 1 for i in range(N)]
check_list = [False] * N

arr = []


def dfs(cnt):
    print_flag=True
    # 주어진 개수만큼 채워지면 출력한다
    if(cnt == M):
        if cnt>1:
            if arr[0]==min(arr):
                for a in range(0,cnt-1):
                    if arr[a]>arr[a+1]:
                        #print(num_list[a],num_list[a+1])
                        print_flag=False
                if print_flag==True:
                    print(*arr)
                else:
                    print_flag=True
                
        else:
            print(*arr)
        
        return
    
    for i in range(0, N):
        
        
        # i번째는 거쳐갈거라서 True로 바꾼다.
        check_list[i] = True
        arr.append(num_list[i])
        # 현재의 i를 기준으로 가지치기 시작
        dfs(cnt + 1)
        # 이 부분은
        #print(arr)
        arr.pop()
        # 여기서 print(arr)을 해보면 작동원리를 알 수 있다.
        #print(arr)
        #print(check_list)
        for j in range(i+1,N):
            check_list[j]=False
        
        
dfs(0)