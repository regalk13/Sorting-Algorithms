# This method for sort need two functions heapify, heap_sort... This method
# Use a heap tree, so use heap_sort to build a max heap - so this node is greater >= that his childs
# and Heapify correct a single violation of the heap property of a subtree root

#      30(0)                 
#     /    \         
#    70(1) 50(2)

#Child (70(1)) is greater than the parent (30(0))

#Swap Child (70(1)) with the parent (30(0))

#      70(0)                 
#      /   \         
#    30(1)  50(2)

# Discard node n from heap - decrement heap size, so new root may violete max heap, create again max-heap
# Complexity O(nLogn) In some thimes this is not stable...

def heapify(arr, n, i):
    largest = i # Init largest as root
    l = 2 * i + 1 # Left
    r = 2 * i + 2 # Right 


    # See if left child of root exists and is greater than root
    if l < n and arr[largest] < arr[l]:
        largest = l
    
    # See if right child of root exists and is greater than root 
    if r < n and arr[largest] < arr[r]:
        largest = r

    # Change root, if needed 
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i] # Swap 
        
        # This is the fix if have a violation
        heapify(arr, n, largest)
    

def heap_sort(arr):
    n = len(arr)
    
    # Build a maxheap
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)

    # Return sorted array
    return arr

# Driver code 
arr = [12, 10, 3, 4, 1]
print(heap_sort(arr))

