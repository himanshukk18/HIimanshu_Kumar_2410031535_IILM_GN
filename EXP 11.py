def reverse_array(arr):
    """
    Reverses the array in-place.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    left = 0
    right = len(arr) - 1

    while left < right:
        temp = arr[left]
        arr[left] = arr[right]
        arr[right] = temp

        left += 1
        right -= 1

    return arr


# Driver Code
arr1 = [1, 4, 3, 2, 6, 5]
print("Reversed Array:", reverse_array(arr1))