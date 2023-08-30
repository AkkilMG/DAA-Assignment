def heapify(a, n, i):
    largest = i
    left = 2*i + 1
    right = 2*i + 2
    if left < n and a[i] < a[left]:
        largest = left
    if right < n and a[largest] < a[right]:
        largest = right
    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        heapify(a, n, largest)


def heapSort(a):
    n = len(a)
    for i in range(n // 2 - 1, -1, -1):
        heapify(a, n, i)
    for i in range(n - 1, 0, -1):
        a[i], a[0] = a[0], a[i]
        heapify(a, i, 0)
a = [int(i) for i in input().split()] # 12 11 13 5 6 7
heapSort(a)
print(f"Sorted array is: {a}")
