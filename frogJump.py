def solution(x,y,d): 
    jumps = 0 
    while x <= y:
        x += d #Adding incrementation on x 
        jumps+= 1 #Increases sum of frog jumps per loop 
    return jumps 

print(solution(50,100, 20))
