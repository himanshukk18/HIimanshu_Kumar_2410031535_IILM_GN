def union_of_arrays(a, b):
    result = set()

    for i in a:
        result.add(i)

    for i in b:
        result.add(i)

    return list(result)


a = [1, 2, 3, 2, 1]
b = [3, 2, 2, 3, 3, 2]
print(sorted(union_of_arrays(a, b)))