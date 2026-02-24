def two_sum(nums, target):
    index_map = {}

    for i in range(len(nums)):
        complement = target - nums[i]

        if complement in index_map:
            return index_map[complement], i

        index_map[nums[i]] = i

    return -1


nums9 = [2, 7, 11, 15]
print(two_sum(nums9, 9))