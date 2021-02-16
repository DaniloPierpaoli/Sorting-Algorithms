def merge_sort(array):
    
    #Recursive function that gets called everytime the array and subarrays get splitted.
    #When the array has only one element, the recursion ends and it returns the array 
    if len(array) == 1:
        return array

    right = array[len(array)//2:]
    left = array[:len(array)//2]
   
  
    return  merge(merge_sort(right),merge_sort(left))

def merge(left,right):
    
    # Function that merged two ordered arrays into one ordered array. 
    # It keep checking the first elements of each array, until one of the two arrays runs out,
    # or all the values of one array are smaller than all the values of the other.
    
    merged =[] 
    while True:
        
        # Scenario all the elements of the left array are smaller than the elements of the other,
        # or the right array has run out of values.
        if comparison(left[0],right) and comparison(left[-1],right) or len(right) == 0:
            merged.extend(left)
            if len(right) > 0:
                merged.extend(right)
            return merged
        
        # Scenario all the elements of the right array are smaller than the elements of the other,
        # or the left array has run out of values.
        elif comparison(right[0],left) and comparison(right[-1],left) or len(left) == 0: 
            merged.extend(right)
            if len(left) > 0:
                merged.extend(left)
                
            return merged

        #Comparison between the first (smallest) elements of the two arrays:   
        else:
            if left[0] > right[0]:
                merged.append(right[0])
                right.pop(0)
            elif right[0]>left[0]:
                merged.append(left[0])
                left.pop(0)
            else:
                merged.append(right[0])
                right.pop(0)
                merged.append(left[0])
                left.pop(0)
                

def comparison(item,array):
    #Function that compares one value with all the values of an array.
    #It returns True all the values of the array are lower than the target value.
    for i in array:
        if item > i:
            return False
        
    return True     
        
