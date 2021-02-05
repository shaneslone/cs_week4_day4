def insertion_sort(a, key=None):
    for i in range(len(a)):
        num = a[i]
        for j in range(i, -1, -1):
            if j == 0:
                a[0] = num
            else:
                comp_n0 = a[j] if key is None else key(a[j])
                comp_n1 = a[j-1] if key is None else key(a[j-1])
                if comp_n0 < comp_n1:
                    a[j], a[j-1] = a [j-1], a[j]
                else:
                    break
    return a

print(insertion_sort([1]))
print(insertion_sort([3, 2, 1]))
print(insertion_sort(["cat", "apple", "zebra", "dog"]))
print(insertion_sort([1, 4, 3, 2.2, 100, "!", "cat"], key=lambda e: str(e)))