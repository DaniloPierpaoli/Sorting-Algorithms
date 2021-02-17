def selection_sort(array):
    
    # This function scans an array trying to find the smallest element, and then swapping this item for the one in the first position.
    target = 0
    while target < len(array)-1:
        position = target
        pointer = target + 1
        while pointer < len(array):
            if array[pointer] < array[position]:
                position = pointer  
            pointer += 1
         
        array[target], array[position] = array[position], array[target]
        target += 1
                
        
    return array
    
    
def bubble_sort(array):
    #The simplest sorting algorithm. Not very efficient, though. It uses two nested loops
    while True:
        counter = len(array)
        i = 0
        while i < len(array)-1:
            if array[i] > array[i+1]:
                array[i],array[i+1] = array[i+1], array[i]
                counter -=1
            i += 1   
        if counter == len(array):
            break
            
        
    return array    
