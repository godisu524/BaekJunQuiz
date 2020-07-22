def solution(n, lost, reserve):
    answer = 0
    
    for a in lost:
        if a in reserve:
            reserve.remove(a)
            lost.remove(a)
    ("그냥 이과정에서 뭔가 이상한게 분명하다")
    #set 이걸 활용잘하자
    
    n-=len(lost)
    
    for a in reserve:
        if a-1 in lost:
            lost.remove(a-1)
            n+=1
        elif a+1 in lost:
            lost.remove(a+1)
            n+=1
    

    return n
