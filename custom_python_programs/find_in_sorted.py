
def find_in_sorted(arr, x):
    def binsearch(start, end):
        if start > end:  # The condition should be changed to start > end
            return -1
        mid = start + (end - start) // 2
        if x < arr[mid]:
            return binsearch(start, mid - 1)  # The end should be mid - 1, not mid
        elif x > arr[mid]:
            return binsearch(mid + 1, end)  # The start should be mid + 1, not mid
        else:
            return mid

    return binsearch(0, len(arr) - 1)  # The upper bound should be len(arr) - 1