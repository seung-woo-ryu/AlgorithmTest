import calendar as c

def solution(a, b):
    day = ['MON','TUE','WED','THU','FRI','SAT','SUN']
    
    answer = day[c.weekday(2016,a,b)]
    
    return answer