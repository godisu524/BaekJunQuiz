#시작지점을 주어주고
#그다음 갈수있는 것들중에 작은값들을 찾아서 이동. n값이 0 이 되면 리턴 
#첨에 솔팅을 해주었기 때문에 따로 안에 내용을 확인할 필요없음.
def solution(n, costs):
    answer = 0
    used=[]
    costs.sort(key=lambda x:x[2])
    #print(costs)
    start = costs.pop(0)
    #1번째꺼 두번째꺼 사용
    used.append(start[0])
    used.append(start[1])
    answer+=start[2]
    n-=2
    
    #print(used)
    while(n):
        #print(n)
        for m,cost in enumerate(costs):
            #print(used)
            if cost[0] in used and cost[1] not in used:
                used.append(cost[1])
                costs.pop(m)
                answer+=cost[2]
                n-=1
                break
            elif cost[1] in used and cost[0] not in used:
                used.append(cost[0])
                costs.pop(m)
                answer+=cost[2]
                n-=1
                break
    #print(used)
    return answer


print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))