# Sorting-Algorithms

Collection of different types of sorting algorithms.
Merge sort uses a recursive function: when it's called the array gets splitted into two arrays (left and right), the merge function is returned containing the recursive function of those two arrays as arguments. This creates a tree of log base 2 len(array) levels. When one array will have only one value, this array gets returned and the merge function will start merging, and the call stacks will free up.
