
def arrayRotation(arrayObject, numRotations): 
    newArray = []
    for i in range(numRotations): #for in range of the rotations proposed 
        for x in range(len(arrayObject)): #range has to be in integer format 
            if x == 0:
                newArray.append(arrayObject[-1])
            else: 
                newArray.append(arrayObject[x -1]) #.append adds a new object into the array 
        arrayObject = newArray
    
    return arrayObject
    

a = [1,2,3,4,5,6,7,8]

print(arrayRotation(a,1)) 

