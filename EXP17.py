def maximum_subarray_sum(arr):
    current_sum = arr[0]
    maximum_sum = arr[0]

    for i in range(1, len(arr)):
        if current_sum + arr[i] > arr[i]:
            current_sum = current_sum + arr[i]
        else:
            current_sum = arr[i]

        if current_sum > maximum_sum:
            maximum_sum = current_sum

    return maximum_sum


arr7 = [2, 3, -8, 7, -1, 2, 3]
print(maximum_subarray_sum(arr7))