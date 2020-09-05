def solution(n, money):
    money.sort()
    
    table = {}
    for m in money:
        table[m] = [1] + [0] * n
    
    for i in range(n + 1):
        table[money[0]][i] = 1 if i % money[0] == 0 else 0
    
    for y in range(1,len(money)):
        for x in range(1,n+1):
            if x - money[y] >= 0:
                table[money[y]][x] = table[money[y-1]][x] + table[money[y]][x-money[y]]
            else:
                table[money[y]][x] = table[money[y-1]][x]
    
    return table[money[-1]][n] % 1000000007