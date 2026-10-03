# ============================================================
# Category 8: Dynamic Programming — BASE PROBLEMS + EXHAUSTIVE VARIANTS
# Core pattern: Break into subproblems, memoize/tabulate
# Key: Identify state, transition, base case
# ============================================================

# ============================================================
# PROBLEM 1: CLIMB STAIRS
# ============================================================
# What it solves: Ways to climb n stairs if you take 1 or 2 steps at a time
# Recurrence: f(n) = f(n-1) + f(n-2)  (Fibonacci!)
# Base case: f(1)=1, f(2)=2
# Interview angle: With obstacle positions? 3-step option?

# BASE: Ways to climb n stairs (1 or 2 steps)
def climb_stairs(n):
    """Base: count ways to climb n stairs (1 or 2 steps per move)"""
    if n <= 2:
        return n
    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b

# VARIANT 1A: With custom step sizes
def climb_stairs_custom_steps(n, steps):
    """Variant A: climb n stairs with custom step options"""
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        for step in steps:
            if i >= step:
                dp[i] += dp[i - step]
    return dp[n]

# VARIANT 1B: Return actual paths (not count)
def climb_stairs_return_paths(n):
    """Variant B: return all possible paths (list of ways)"""
    result = []
    def backtrack(remaining, path):
        if remaining == 0:
            result.append(path)
            return
        for step in [1, 2]:
            if step <= remaining:
                backtrack(remaining - step, path + [step])
    backtrack(n, [])
    return result

# VARIANT 1C: With obstacle positions
def climb_stairs_with_obstacles(n, obstacles):
    """Variant C: climb n stairs avoiding specific positions"""
    blocked = set(obstacles)
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        if i not in blocked:
            if i >= 1:
                dp[i] += dp[i - 1]
            if i >= 2:
                dp[i] += dp[i - 2]
    return dp[n]

# VARIANT 1D: Minimum steps (not ways, but min steps to reach n)
def min_steps_to_n(n, max_step):
    """Variant D: minimum steps needed to reach n (greedy jumps)"""
    if n == 0:
        return 0
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    for i in range(1, n + 1):
        for step in range(1, min(max_step, i) + 1):
            dp[i] = min(dp[i], dp[i - step] + 1)
    return dp[n]

print("=== PROBLEM 1: CLIMB STAIRS ===")
print("BASE (n=5):", climb_stairs(5))
print("VARIANT 1A (steps=[1,2,3]):", climb_stairs_custom_steps(5, [1, 2, 3]))
print("VARIANT 1B (paths for 3):", climb_stairs_return_paths(3))
print("VARIANT 1C (with obstacles):", climb_stairs_with_obstacles(5, [2]))
print()


# ============================================================
# PROBLEM 2: COIN CHANGE
# ============================================================
# What it solves: Minimum coins to make amount (unbounded)
# State: dp[i] = min coins to make amount i
# Transition: dp[i] = min(dp[i], dp[i - coin] + 1) for each coin
# Interview angle: Count ways? Return actual coins? Limited coins?

# BASE: Minimum coins to make amount
def coin_change(coins, amount):
    """Base: minimum coins needed to make amount"""
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1

# VARIANT 2A: Count ways to make amount (coin combinations)
def coin_change_ways(coins, amount):
    """Variant A: count WAYS to make amount (combinations, not permutations)"""
    dp = [0] * (amount + 1)
    dp[0] = 1
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]
    return dp[amount]

# VARIANT 2B: Return actual coins (not just count)
def coin_change_return_coins(coins, amount):
    """Variant B: return which coins to use (actual selection)"""
    dp = [float('inf')] * (amount + 1)
    parent = [-1] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                parent[i] = coin

    if dp[amount] == float('inf'):
        return []
    result = []
    curr = amount
    while curr > 0:
        coin = parent[curr]
        result.append(coin)
        curr -= coin
    return result

# VARIANT 2C: Limited coins (each coin used at most once)
def coin_change_limited(coins, amount):
    """Variant C: minimum coins where each coin used at most once (0/1 knapsack)"""
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for i in range(amount, coin - 1, -1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1

# VARIANT 2D: Maximum coins allowed per type
def coin_change_max_per_coin(coins, amount, max_per_coin):
    """Variant D: minimum coins with max uses per coin type"""
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        new_dp = dp[:]
        for count in range(1, max_per_coin + 1):
            for i in range(amount, coin * count - 1, -1):
                if dp[i - coin * count] != float('inf'):
                    new_dp[i] = min(new_dp[i], dp[i - coin * count] + count)
        dp = new_dp
    return dp[amount] if dp[amount] != float('inf') else -1

print("=== PROBLEM 2: COIN CHANGE ===")
print("BASE (amount=5, coins=[1,2,5]):", coin_change([1, 2, 5], 5))
print("VARIANT 2A (count ways):", coin_change_ways([1, 2, 5], 5))
print("VARIANT 2B (actual coins):", coin_change_return_coins([1, 2, 5], 5))
print("VARIANT 2C (limited coins):", coin_change_limited([1, 2, 5], 5))
print()


# ============================================================
# PROBLEM 3: LONGEST COMMON SUBSEQUENCE (LCS)
# ============================================================
# What it solves: Find length of longest common subsequence
# Key: 2D DP where dp[i][j] = LCS of s1[0:i] and s2[0:j]
# Interview angle: Return actual LCS? Print alignment?

# BASE: LCS length
def longest_common_subsequence(s1, s2):
    """Base: length of longest common subsequence"""
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]

# VARIANT 3A: Return actual LCS string
def lcs_string(s1, s2):
    """Variant A: return the actual LCS string"""
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    result = []
    i, j = m, n
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            result.append(s1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    return ''.join(reversed(result))

# VARIANT 3B: LCS of 3+ strings (not just 2)
def lcs_k_strings(strings):
    """Variant B: LCS of multiple strings"""
    if not strings:
        return 0
    n = len(strings[0])
    dp = [0] * n
    for i in range(n):
        dp[i] = strings[0][i]
    for s in strings[1:]:
        new_lcs = longest_common_subsequence(dp, list(s))
        # This is simplified; full implementation would need 3D DP
    return longest_common_subsequence(strings[0], strings[1]) if len(strings) > 1 else 0

# VARIANT 3C: Count distinct LCS
def count_lcs(s1, s2):
    """Variant C: count how many distinct LCS exist"""
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    count = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        count[i][0] = 1
    for j in range(n + 1):
        count[0][j] = 1

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                count[i][j] = count[i - 1][j - 1]
            else:
                if dp[i - 1][j] > dp[i][j - 1]:
                    dp[i][j] = dp[i - 1][j]
                    count[i][j] = count[i - 1][j]
                elif dp[i - 1][j] < dp[i][j - 1]:
                    dp[i][j] = dp[i][j - 1]
                    count[i][j] = count[i][j - 1]
                else:
                    dp[i][j] = dp[i - 1][j]
                    count[i][j] = count[i - 1][j] + count[i][j - 1]
    return count[m][n]

print("=== PROBLEM 3: LCS ===")
print("BASE:", longest_common_subsequence("abcde", "ace"))
print("VARIANT 3A (string):", lcs_string("abcde", "ace"))
print()


# ============================================================
# PROBLEM 4: EDIT DISTANCE (LEVENSHTEIN)
# ============================================================
# What it solves: Min edits (insert/delete/replace) to transform s1 to s2
# State: dp[i][j] = edits needed for s1[0:i] to s2[0:j]
# Interview angle: Return edits? With costs?

# BASE: Edit distance
def edit_distance(s1, s2):
    """Base: minimum edits to transform s1 to s2"""
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
    return dp[m][n]

# VARIANT 4A: Return actual edits
def edit_distance_with_ops(s1, s2):
    """Variant A: return list of operations"""
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

    ops = []
    i, j = m, n
    while i > 0 or j > 0:
        if i > 0 and j > 0 and s1[i - 1] == s2[j - 1]:
            i -= 1
            j -= 1
        elif i > 0 and j > 0 and dp[i - 1][j - 1] == dp[i][j] - 1:
            ops.append(('replace', s1[i - 1], s2[j - 1]))
            i -= 1
            j -= 1
        elif j > 0 and dp[i][j - 1] == dp[i][j] - 1:
            ops.append(('insert', s2[j - 1]))
            j -= 1
        elif i > 0 and dp[i - 1][j] == dp[i][j] - 1:
            ops.append(('delete', s1[i - 1]))
            i -= 1
    return list(reversed(ops))

# VARIANT 4B: Only insert/delete (no replace)
def edit_distance_no_replace(s1, s2):
    """Variant B: edits with only insert/delete (no replace)"""
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]

# VARIANT 4C: With custom costs per operation
def edit_distance_custom_cost(s1, s2, insert_cost=1, delete_cost=1, replace_cost=1):
    """Variant C: edits with custom costs"""
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i * delete_cost
    for j in range(n + 1):
        dp[0][j] = j * insert_cost

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(
                    dp[i - 1][j] + delete_cost,
                    dp[i][j - 1] + insert_cost,
                    dp[i - 1][j - 1] + replace_cost
                )
    return dp[m][n]

print("=== PROBLEM 4: EDIT DISTANCE ===")
print("BASE:", edit_distance("horse", "ros"))
print("VARIANT 4C (custom cost):", edit_distance_custom_cost("horse", "ros", 1, 1, 2))
print()

print("=" * 70)
print("CATEGORY 8: DYNAMIC PROGRAMMING PATTERN MASTERY")
print("=" * 70)
print("Pattern 1: 1D DP (unbounded items, sequences)")
print("Pattern 2: 2D DP (matching, alignment, distance)")
print("Pattern 3: State = problem constraints, Transition = problem logic")
print("=" * 70)
