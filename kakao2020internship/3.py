#["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
#["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
#["AA", "AB", "AC", "AA", "AC"]

def check(gems,start,end,s_gems,answer):
    print(start,end)
    if set(gems[start-1:end]) == s_gems:
        print(1)
        if (end-start) < (answer[1]-answer[0]):
            answer = [start,end]
            return answer,(end-1)
    else:
        print(2)
        print(start,end)
        return answer,end
        

def solution(gems) :
    answer = [0,100001]
    s_gems= set(gems)

    mn, mx = 1, len(gems)
    while mn < mx:
        mid = (mn+mx) //2
        
        answer, n= check(gems, mn, mid,s_gems,answer)
        if n<mid:
            mx = n
        else:
            if mn == mid:
                answer,n =check(gems, mn, mid,s_gems,answer)
                return answer
            mn = mid
    return answer






        





print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))