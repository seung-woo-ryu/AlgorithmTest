def solution(priorities, location):
    pi_list = [(p, i) for i, p in enumerate(priorities)]
    waiting_q = []
    while pi_list:
        pi = pi_list.pop(0)
        priority = pi[0]
        p_list = [priority for priority, idx in pi_list]
        if p_list:
            max_p = max(p_list)
        if priority >= max_p:
            waiting_q.append(pi)
        else:
            pi_list.append(pi)
    for i, item in enumerate(waiting_q):
        if item[1] == location:
            return i + 1

solution([2,1,3,2],2)