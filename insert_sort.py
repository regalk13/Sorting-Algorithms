def insert_sort(arr):
    # Input arr...
    # Return sorted arr ->>
    # Complexity = O(n^2) // 'cause for = O(n) and the comparations and swaps O(n) 
    # // Best Case O(n) == All items are the same

    # Loop through the array
    for i in range(1, len(arr)):
        k = arr[i] # If arr = [2, 3, ....m-1], k = 3
        j = i-1 # and j = 2

        # While, if while is true:
        # arr = [4, 3] -> arr = [3, 4]
        while j>=0 and k < arr[j]:
            arr[j+1] = arr[j]
            j -= 1

        # Key still greater than J
        arr[j+1] = k
    
    # Return the array 
    return arr

# Running Code
arr = [2, 1, 5, 6, 10, 3]
print(insert_sort(arr))

