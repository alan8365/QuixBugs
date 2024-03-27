

def knapsack(capacity, items):
    from collections import defaultdict
    memo = defaultdict(int)

    for i in range(len(items)):
        weight, value = items[i]

        for j in range(capacity, weight - 1, -1):
            memo[i, j] = memo[i - 1, j]

            if weight < j:
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items) - 1, capacity]


