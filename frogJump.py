def solution(x,y,d): 
    jumps = 0 
    while x <= y:
        x += d
        jumps+= 1
    return jumps 

print(solution(50,100, 20))