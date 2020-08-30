def solution(n, words):
    relay = {}
    order = 0
    last_ch = words[0][0]
    
    for idx, word in enumerate(words):
        if not idx % n:
            order += 1
        if word not in relay and last_ch == word[0]:
            relay[word] = 1
            last_ch = word[-1]
        else:
            return [idx % n + 1,order]
    return [0,0]