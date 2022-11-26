a = [8, 2, 56, 76, 3, 2, 0, 89]

print(a)


def bubble_sort(list):
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i] < a[j]:
                a[i], a[j] = a[j], a[i]
                break

    return list


print(bubble_sort(a))
