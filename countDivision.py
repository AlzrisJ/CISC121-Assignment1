from InputExtensions import * 
def solution(a, b, k): 
    if a >= b: 
        return 'Invalid Parameters' #Returns invalid paremetrs if a>= b 
    else: 
        count = 0 
        while a <= b: 
            if (a % k) == 0: #Finding remainders 
                count += 1 #add to count 
            a += 1 
        return count 
print(solution(6,11,2))
