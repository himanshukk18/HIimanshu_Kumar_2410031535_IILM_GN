
def kth_smallest(arr, k):
    """
    Returns kth smallest element.
    Time Complexity: O(n log n)
    """
    sorted_array = sorted(arr)
    return sorted_array[k - 1]


# Driver Code
arr3 = [10, 5, 4, 3, 48, 6, 2, 33, 53, 10]
k = 4
print("Kth Smallest Element:", kth_smallest(arr3, k))