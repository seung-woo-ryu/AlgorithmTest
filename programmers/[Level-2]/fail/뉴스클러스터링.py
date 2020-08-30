def solution(str1, str2):
    str1 = str1.upper()
    str2 = str2.upper()
    li1 = list()
    li2 = list()
    
    for i in range(len(str1)-1):
        if str.isalpha(str1[i:i+2]):
            li1.append(str1[i:i+2])
    n1 = len(li1)
    for i in range(len(str2)-1):
        if str.isalpha(str2[i:i+2]):
            li2.append(str2[i:i+2])
    n2 = len(li2)
    n3 = 0
    print(li1,li2)
    for ch in li1:
        for idx,ch2 in enumerate(li2):
            if ch2 == ch:
                n3 += 1
                del li2[idx]
    
    print(n1,n2,n3)
    return int((n3 /(n1+n2-n3))*65536)

print(solution("aa1+aa2", "AAAA12"))