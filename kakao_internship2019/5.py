def check(rocks,n,k):
    cnt= 0
    for i in rocks:
        if i <n:
            cnt+=1
            if cnt >=k:
                return n-1
        else:
            cnt=0
    return n

def solution(rocks,k) :
    mn, mx = 1, max(rocks)
    while mn < mx:
        mid = (mn+mx) //2
        n= check(rocks, mid, k)
        if n<mid:
            mx = n
        else:
            if mn == mid:
                return check(rocks,mx, k)
            mn = mid
    return mn

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1],3))




        
