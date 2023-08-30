def optimal_bst(keys, freq):
    n = len(keys)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n):
        dp[i][i + 1] = freq[i]
    for length in range(2, n + 1):
        for i in range(n - length + 2):
            j = i + length - 1
            dp[i][j] = float('inf')
            for r in range(i, j + 1):
                cost = sum(freq[i:j + 1]) + (dp[i][r - 1] if r > i else 0) + (dp[r + 1][j] if r < j else 0)
                if cost < dp[i][j]:
                    dp[i][j] = cost
    return dp[0][n - 1]

keys = [int(i) for i in input().split()] # [10, 12, 20, 40]
freq = [int(i) for i in input().split()] # [34, 8, 50, 23]

print("Minimum expected cost: ", optimal_bst(keys, freq))