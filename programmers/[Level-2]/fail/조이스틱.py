def solution(name):
    li = []
    answer = 0
    Lp = Rp = 0
    Lp2 = Rp2 = 0
    for num in name:
        tmp = ord(num) - ord('A') if (ord(num) - ord('A')) < 14 else 26 - (ord(num) - ord('A'))
        li.append(tmp)
        answer += tmp

    
    for i in range(1, len(li)):
        if li[i] !=0 and Lp == 0:
            Lp = i
        elif li[i] != 0 and Lp != 0 and Lp2 == 0:
            Lp2 = i
        if li[-i] != 0 and Rp == 0:
            Rp = i
        elif li[-i] != 0 and Rp != 0 and Rp2 == 0:
            Rp2 = i
    
    a = 2*Rp + len(li) - Rp2
    b = Lp*2 + len(li) - Lp2
    Rp = len(li) - Rp
    Lp = len(li) - Lp

    tmp = Lp if Lp < Rp else Rp
    a = a if a< b else b
    answer += tmp if tmp < a else a

    return answer