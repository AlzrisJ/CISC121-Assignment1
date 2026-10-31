sampleArray = [-1,-3]
#specfically target the only value that doesn't come with pair 
def unpairSorter(userArray): 
    emptyArray = []
    for i in range(len(userArray)):
        if userArray[i] in emptyArray:
            emptyArray.remove(userArray[i])
        else: 
            emptyArray.append(userArray[i])
     
    return emptyArray[0]


print(unpairSorter(sampleArray))
        
    