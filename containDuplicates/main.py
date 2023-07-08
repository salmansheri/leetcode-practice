def contains_duplicate(arr):
    hashSet = set()

    for i in arr:
        if i in hashSet:
            return True

        hashSet.add(i)

    return False


arr = [1, 1, 2, 3]
print(contains_duplicate(arr))
