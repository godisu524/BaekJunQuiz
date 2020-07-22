import heapq
def solution(operations):
    answer = []
    real_answer=[]
    for operation in operations:
        if operation.startswith("I"):
            heapq.heappush(answer,int(operation.split(" ")[1]))
        else:
            if operation == "D -1":
                try:
                    answer.pop(0)
                except:
                    pass
            elif operation == "D 1":
                try:
                    answer.pop()
                except:
                    pass
    if len(answer)==0:
        real_answer = [0,0]
    else:
        real_answer.append(max(answer))
        real_answer.append(min(answer))

    

    return real_answer

print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))