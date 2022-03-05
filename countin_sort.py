# This a special sort algorithm, but is a little bit inestable, this gives you linear sorting in some cases
# That dependes on the range of elementss but the mos affected is the size of memory...
# Is Perfect for sort strings, it works by counting the number of objects having disctinct key values (kind hashing). then doing some arithmetic to calculate the position of each object
# For simplicity, consider the data in the range 0 to 9.
#Input data: 1, 4, 1, 2, 7, 5, 2
#  1) Take a count array to store the count of each unique object.
#  Index:     0  1  2  3  4  5  6  7  8  9
#  Count:     0  2  2  0   1  1  0  1  0  0

#  2) Modify the count array such that each element at each index
#  stores the sum of previous counts.
#  Index:     0  1  2  3  4  5  6  7  8  9
#  Count:     0  2  4  4  5  6  6  7  7  7

#The modified count array indicates the position of each object in
#the output sequence.
#
#  3) Rotate the array clockwise for one time.
#   Index:     0 1 2 3 4 5 6 7 8 9
#   Count:     0 0 2 4 4 5 6 6 7 7
#
#  4) Output each object from the input sequence followed by
#  increasing its count by 1.
#  Process the input data: 1, 4, 1, 2, 7, 5, 2. Position of 1 is 0.
#  Put data 1 at index 0 in output. Increase count by 1 to place
#  next data 1 at an index 1 greater than this index.

# Sorting Strings...

def count_sort(arr):

    output = [0 for i in range(len(arr))] ## 0 of each item in the array
    count = [0 for i in range(256)] # Always 256 cause is the max number in charactars on unicode
    ans = ["" for _ in arr] # Return array

    # Store count of each char
    for i in arr:
        count[ord(i)] += 1

    # sum count[i] + count[i+1] this give the actual position in the output array

    for i in range(256):
        count[i] += count[i-1]

    # Build the output array

    for i in range(len(arr)):
        output[count[ord(arr[i])]-1] = arr[i]
        count[ord(arr[i])] -= 1

    for i in range(len(arr)):
        ans[i] = output[i]

    print("".join(ans))

# This algorithm always will be linear O(n) cause the range is the same so is very useful for this cases...
arr = "hellohowareyou"
count_sort(arr)

# Sort for numbers

def count_sort_numbers(arr):
    # Max element in the array
    max_element = int(max(arr))
    # Min element in the array
    min_element = int(min(arr))
    # Range between max and min
    range_of_elements = max_element - min_element + 1
    # Count array 0 for each range of numbers in range_of_elements
    count = [0 for i in range(range_of_elements)]
    # Output range of n
    output = [0 for i in range(len(arr))]

    for i in range(0, len(arr)):
        count[arr[i]-min_element] += 1

    # Actual position of the array index sum n[i] whit n[i+1] that's return the actual position
    for i in range(1, len(count)):
        count[i] += count[i-1]

    #Build the output

    for i in range(len(arr)-1,-1,-1):
        output[count[arr[i] - min_element]-1] = arr[i]
        count[arr[i] - min_element] -= 1

    for i in range(0, len(arr)):
        arr[i] = output[i]

    return arr


arr = [1, 3, 2, 5, 10, 2]

print(count_sort_numbers(arr))
