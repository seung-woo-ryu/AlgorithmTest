def solution(nums):
    return len(set(nums)) if len(set(nums)) <= len(nums)/2 else len(nums)/2

print(solution([3,3,3,2,2,4]))