def union_arrays(a, b):
    union_set = set()

    for num in a:
        union_set.add(num)

    for num in b:
        union_set.add(num)

    return list(union_set)


# Example
a = [1, 2, 3, 2, 1]
b = [3, 2, 2, 3, 3, 2]
print(sorted(union_arrays(a, b)))