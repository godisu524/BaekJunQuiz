def solution(bridge_length, max_weight, truck_weights):
    # FIFO 문제.
    bridge = [0]*bridge_length
    curr_weight = 0
    ans = 0
    while len(truck_weights) > 0:
        print(bridge)
        ans += 1
        ar = bridge.pop(0) #popleft
        curr_weight -= ar
        if curr_weight + truck_weights[0] > max_weight:
            bridge.append(0)            
        else:
            truck = truck_weights.pop(0)
            bridge.append(truck)
            curr_weight += truck
    while curr_weight > 0:
        print(bridge)
        ans += 1
        ar = bridge.pop(0)
        curr_weight -= ar
    return ans

print(solution(2,	10,	[7,4,5,6]))