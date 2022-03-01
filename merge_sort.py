def merge_sort(arr):
    # Complexity: T(n) = 2T(n/2) + 0(n) or O(nLogn)
    # If the array have more than 1 element
    if len(arr) > 1:

        # Find the mid of the array
        mid = len(arr)//2
        
        # Left side
        l = arr[:mid]

        # Right side
        r = arr[mid:]
        
        # Recursive function to left and right side
        merge_sort(l)
        merge_sort(r)


        # All variables to 0
        i = j = k = 0

        # While until j and i is greater than the lenght of the arr part
        while i < len(l) and j < len(r):
            # Compare same index of the two arrays
            if l[i] < r[j]:
                arr[k] = l[i]
                i += 1
            else:
                arr[k] = r[j]
                j += 1
            
            # Plus 1 to k
            k += 1
            

        # Check if any element was left
        while i < len(l):
            arr[k] = l[i]
            i += 1
            k += 1

        while j < len(r):
            arr[k] = r[j]
            j += 1
            k += 1
        
        # Return the sorted array 
        return arr


# Code runner 
arr = [5, 4, 2, 1, 4]
print(merge_sort(arr))
            

