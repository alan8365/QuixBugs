
def quicksort(arr):
    if not arr:
        return []

    pivot = arr[len(arr) // 2]
    lesser = quicksort([x for x in arr if x < pivot])
    greater = quicksort([x for x in arr if x > pivot])
    return lesser + [pivot] + greater