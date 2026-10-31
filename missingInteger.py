a = [1, 3, 6, 4, 1, 2]

def solution(a): 
    maxVal = max(a) #Takes the max and min from the array 
    minVal = 1
    while minVal <= maxVal: #iterates using the max and min values 
        if minVal not in a: #proceeds to take the lowest value that is NOT in a a[minVal] does not work because a[minVal] is essentially already in a 
            return minVal
        minVal +=1
    return minVal

print(solution(a))  