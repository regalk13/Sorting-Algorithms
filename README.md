# Sorting Algorithms

Why sorting? because the problems become easy whit sorted elements. Example: Find media, Graphics, AI, etc...

So how what is the best way to sort? the asnwer is depends, that depends what you want sort and for that exists a large quantity of algorithms as I will show here only some...

## Comparison

- **Insert Sort:** Insertion sort is a simple sorting algorithm that works similar to the way you sort playing cards in your hands. The array is virtually split into a sorted and an unsorted part. Values from the unsorted part are picked and placed at the correct position in the sorted part
  - Time Complexity: O(n^2) 
  - Auxiliary Space: O(1)
  - Boundary Cases: Insertion sort takes maximum time to sort if elements are sorted in reverse order. And it takes minimum time (Order of n) when elements are already sorted.
  - Algorithmic Paradigm: Incremental Approach
  - Sorting In Place: Yes
  - Stable: Yes
  - Online: Yes
  - Uses: Insertion sort is used when number of elements is small. It can also be useful when input array is almost sorted, only few elements are misplaced in complete big array.

- **Merge Sort:** Like QuickSort, Merge Sort is a Divide and Conquer algorithm. It divides the input array into two halves, calls itself for the two halves, and then merges the two sorted halves. The merge() function is used for merging two halves. The merge(arr, l, m, r) is a key process that assumes that arr[l..m] and arr[m+1..r] are sorted and merges the two sorted sub-arrays into one. See the following C implementation for details.
  - Time Complexity: Sorting arrays on different machines. Merge Sort is a recursive algorithm and time complexity can be expressed as following recurrence relation. 
T(n) = 2T(n/2) + θ(n)
The above recurrence can be solved either using the Recurrence Tree method or the Master method. It falls in case II of Master Method and the solution of the recurrence is θ(nLogn). Time complexity of Merge Sort is  θ(nLogn) in all 3 cases (worst, average and best) as merge sort always divides the array into two halves and takes linear time to merge two halves.
  - Auxiliary Space: O(n)
  - Algorithmic Paradigm: Divide and Conquer
  - Sorting In Place: No in a typical implementation
  - Stable: Yes

- **Heap Sort:** Heap sort is a comparison-based sorting technique based on Binary Heap data structure. It is similar to selection sort where we first find the minimum element and place the minimum element at the beginning. We repeat the same process for the remaining elements.

  - Time Complexity: Time complexity of heapify is O(Logn). Time complexity of createAndBuildHeap() is O(n) and the overall time complexity of Heap Sort is O(nLogn).

  - Advantages of heapsort:

    - Efficiency –  The time required to perform Heap sort increases logarithmically while other algorithms may grow exponentially slower as the number of items to sort increases. This sorting algorithm is very efficient.
     - Memory Usage – Memory usage is minimal because apart from what is necessary to hold the initial list of items to be sorted, it needs no additional memory space to work
    - Simplicity –  It is simpler to understand than other equally efficient sorting algorithms because it does not use advanced computer science concepts such as recursion 

- **Counting Sort:** Counting sort is a sorting technique based on keys between a specific range. It works by counting the number of objects having distinct key values (kind of hashing). Then doing some arithmetic to calculate the position of each object in the output sequence.
  - Time Complexity: O(n+k) where n is the number of elements in input array and k is the range of input. 
  - Auxiliary Space: O(n+k)
- **Radix Sort:** The lower bound for Comparison based sorting algorithm (Merge Sort, Heap Sort, Quick-Sort .. etc) is Ω(nLogn), i.e., they cannot do better than nLogn. Counting sort is a linear time sorting algorithm that sort in O(n+k) time when elements are in the range from 1 to k.


## Contribute 

You can add more sort algorithms or version in other languages, just open a pull-request.

## Thanks to...

- Algorithms MIT [Course](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/index.htm).
- Geeks for Geeks. [here](https://www.geeksforgeeks.org/)
