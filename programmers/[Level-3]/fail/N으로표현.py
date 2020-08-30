def solution(N, number):
    s = [set() for x in range(9)]
    
    for idx, x in enumerate(s):
        if idx:
            x.add(int(str(N)*idx))
    
    for i in range(2,9):
        for j in range(1,i):
            for x in s[j]:
                for y in s[i-j]:
                    s[i].add(x+y)
                    s[i].add(x-y)
                    s[i].add(x*y)
                    if y:
                        s[i].add(x//y)

    for idx in range(1,9):
        if number in s[idx]:
            return idx
    
    return -1
