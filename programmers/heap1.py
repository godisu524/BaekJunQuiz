import heapq
#요놈이 넣고 뺄때 정렬해준대 오웅 쓋!
def solution(scoville, K):
    answer = 0
    heap=[]
    for num in scoville:
        heapq.heappush(heap,num)
    
    while(heap[0]<K):
        try:
            heapq.heappush(heap, heapq.heappop(heap)+(heapq.heappop(heap)*2))
        except IndexError:
            return -1
        answer+=1


    return answer


print(solution([1, 2, 3, 9, 10, 12],7))