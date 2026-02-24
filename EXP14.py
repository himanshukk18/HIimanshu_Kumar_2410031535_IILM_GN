def union_of_arrays(a, b):
    union_set = set()

    for element in a:
        union_set.add(element)

    for element in b:
        union_set.add(element)

    return list(union_set)


a = [1, 2, 3, 2, 1]
b = [3, 2, 2, 3, 3, 2]
print(sorted(union_of_arrays(a, b)))