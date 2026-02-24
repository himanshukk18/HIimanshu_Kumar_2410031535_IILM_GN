def find_min_max(arr):
    """
    Finds minimum and maximum element in array.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    minimum = arr[0]
    maximum = arr[0]

    for i in range(1, len(arr)):
        if arr[i] < minimum:
            minimum = arr[i]

        if arr[i] > maximum:
            maximum = arr[i]

    return minimum, maximum


# Driver Code
arr2 = [1, 4, 3, 5, 8, 6]
mn, mx = find_min_max(arr2)
print("Minimum:", mn)
print("Maximum:", mx)