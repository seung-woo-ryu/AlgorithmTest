def solution(bridge_length, weight, truck_weights):
    queue = list()
    last_start_time = 0
    last_pop_time = 0
    ATW = 0
    answer = 0
    
    for x in truck_weights:
        while ATW + x > weight:
            ATW -= queue[0][0]
            last_pop_time = queue[0][1] + bridge_length - 1
            queue.pop(0)
        ATW += x
        if last_pop_time <= last_start_time:
            last_start_time += 1     
        else:
            last_start_time = last_pop_time + 1
        queue.append((x,last_start_time))
    
    answer = queue[-1][1] + bridge_length
    return answer