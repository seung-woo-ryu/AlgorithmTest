def solution(operations):
    li = []
    for x in operations:
        if x[0] == "I":
            li.append(int(x[2:]))
        elif x[2:] == '1':
            if len(li):
                li.sort()
                li.pop(-1)
        else:
            if len(li):
                li.sort()
                li.pop(0)
    li.sort()
    if len(li) == 0:
        return [0,0]
    else:
        return[li[-1],li[0]]