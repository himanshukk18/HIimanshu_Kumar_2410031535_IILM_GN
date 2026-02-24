def kth_smallest(arr, k):
    arr.sort()
    return arr[k - 1]


arr3 = [10, 5, 4, 3, 48, 6, 2, 33, 53, 10]
print(kth_smallest(arr3, 4))