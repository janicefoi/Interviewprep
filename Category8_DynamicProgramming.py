# ============================================================
# Category 8: Dynamic Programming Problems
# Core pattern: memoization, bottom-up table building
# ============================================================

# O(n) time, O(n) space
def climb_stairs(n):
    if n <= 2:
        return n
    dp = [0] * (n + 1)
    dp[1], dp[2] = 1, 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

print("climb_stairs(5):", climb_stairs(5))


# O(n) time, O(1) space (optimized)
def fib_memo(n, memo=None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]

print("fib_memo(10):", fib_memo(10))


# O(n) time, O(n) space
def max_subarray(numbers):
    if not numbers:
        return 0
    dp = [0] * len(numbers)
    dp[0] = numbers[0]
    for i in range(1, len(numbers)):
        dp[i] = max(numbers[i], dp[i - 1] + numbers[i])
    return max(dp)

print("max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]):", max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))


# O(amount * len(coins)) time, O(amount) space
def coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for curr in range(coin, amount + 1):
            dp[curr] = min(dp[curr], dp[curr - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1

print("coin_change([1, 2, 5], 5):", coin_change([1, 2, 5], 5))


# O(amount * len(coins)) time, O(amount) space
def coin_change_ways(coins, amount):
    dp = [0] * (amount + 1)
    dp[0] = 1
    for coin in coins:
        for curr in range(coin, amount + 1):
            dp[curr] += dp[curr - coin]
    return dp[amount]

print("coin_change_ways([1, 2, 5], 5):", coin_change_ways([1, 2, 5], 5))


# O(n * m) time, O(n * m) space
def longest_common_subsequence(text1, text2):
    n, m = len(text1), len(text2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[n][m]

print("longest_common_subsequence('abcde', 'ace'):", longest_common_subsequence('abcde', 'ace'))


# O(n * m) time, O(n * m) space
def edit_distance(word1, word2):
    n, m = len(word1), len(word2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = i
    for j in range(m + 1):
        dp[0][j] = j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
    return dp[n][m]

print("edit_distance('horse', 'ros'):", edit_distance('horse', 'ros'))


# O(n²) time, O(n) space
def longest_increasing_subsequence(numbers):
    if not numbers:
        return 0
    n = len(numbers)
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if numbers[j] < numbers[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

print("longest_increasing_subsequence([10, 9, 2, 5, 3, 7, 101, 18]):", longest_increasing_subsequence([10, 9, 2, 5, 3, 7, 101, 18]))


# O(n * capacity) time, O(n * capacity) space  [MIXED: DP + hashmap reasoning]
def knapsack_01(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for cap in range(capacity + 1):
            dp[i][cap] = dp[i - 1][cap]
            if weights[i - 1] <= cap:
                dp[i][cap] = max(dp[i][cap], dp[i - 1][cap - weights[i - 1]] + values[i - 1])
    return dp[n][capacity]

print("knapsack_01([1, 3, 4, 5], [1, 4, 5, 7], 7):", knapsack_01([1, 3, 4, 5], [1, 4, 5, 7], 7))
