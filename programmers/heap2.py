import heapq

def solution(stock, dates, supplies, k):
    answer = 0
    idx =0
    h= []
    while(stock<k):
        for i in range(idx, len(dates)):
            if dates[i]<=stock:
                heapq.heappush(h,(-supplies[i],supplies[i]))
                #print(h)
                idx=i+1
            else:
                break
        stock+=heapq.heappop(h)[1]
        #print(stock)
        answer+=1

    return answer



print(solution(4,[4,10,15],[20,5,10],30))