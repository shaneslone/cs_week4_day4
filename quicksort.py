def quicksort(a):
    if len(a) <= 1:
        return a
    pivot = a[0]
    left = []
    right = [] 
    for i in range(1, len(a)):
        if a[i] > pivot:
            right.append(a[i])
        else:
            left.append(a[i])

    left = quicksort(left)
    right = quicksort(right)

    return left + [pivot] + right

print(quicksort([4, 3, 5, 1, 2]))