

def max_sublist_sum(arr):
    max_ending_here = 0
    max_so_far = float('-inf')

    for x in arr:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far



