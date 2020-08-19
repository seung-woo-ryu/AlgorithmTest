'''
    numbers 원소 길이: 0이상, 1000이하

    길이가 같을 경우: 자릿수 비교로 정렬하면 됨.   
        ..... 으아 말로 정리가 안 됌.
'''
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key= lambda x: x*3, reverse=True)
    
    return str(int(''.join(numbers)))