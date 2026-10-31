from InputExtensions import * 
def solution(a, b, k): 
    if a >= b: 
        return 'Invalid Parameters'
    else: 
        count = 0 
        while a <= b: 
            if (a % k) == 0: 
                count += 1 
            a += 1 
        return count 
print(solution(6,11,2))