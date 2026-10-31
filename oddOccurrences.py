sampleArray = [-1,-3]
#specfically target the only value that doesn't come with pair 
def unpairSorter(userArray): 
    emptyArray = [] #Holds every value that is still waiting for its pair 
    for i in range(len(userArray)): #loop through each index of the input array 
        if userArray[i] in emptyArray: #this value was seen before so it just found its pair 
            emptyArray.remove(userArray[i]) #pair complete, so take it out of the waiting list 
        else: 
            emptyArray.append(userArray[i]) #first time seeing this value, so add it to the waiting list 
     
    return emptyArray[0]#only the unpaired value is left, so it sits at index 0 


print(unpairSorter(sampleArray))
        
    
