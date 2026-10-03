# ============================================================
# Category 2: Sliding Window — BASE PROBLEMS + VARIANTS
# Core pattern: maintain a window, expand/shrink based on constraint
# ============================================================

# ============================================================
# PROBLEM 1: Max Sum Subarray (Fixed Window)
# ============================================================

# BASE: Max sum of k consecutive elements
def max_sum_subarray(numbers, k):
    """Base: max sum of k consecutive elements"""
    window_sum = sum(numbers[:k])
    best = window_sum
    for i in range(k, len(numbers)):
        window_sum += numbers[i] - numbers[i - k]
        best = max(best, window_sum)
    return best

# VARIANT 1A: Max product instead of sum
def max_sum_subarray_product(numbers, k):
    """Variant A: max PRODUCT instead of sum"""
    window_prod = 1
    for i in range(k):
        window_prod *= numbers[i]
    best = window_prod
    for i in range(k, len(numbers)):
        if numbers[i - k] != 0:
            window_prod = (window_prod // numbers[i - k]) * numbers[i]
        else:
            window_prod = 1
            for j in range(i - k + 1, i + 1):
                window_prod *= numbers[j]
        best = max(best, window_prod)
    return best

# VARIANT 1B: Count windows with sum >= threshold
def count_subarray_sum_k(numbers, k):
    """Variant B: COUNT how many k-windows have sum >= target"""
    count = 0
    target = sum(numbers[:k])
    if target >= k:
        count += 1
    for i in range(k, len(numbers)):
        s = sum(numbers[i-k+1:i+1])
        if s >= k:
            count += 1
    return count

# VARIANT 1C: Return all k-windows with sum >= target
def all_subarrays_sum_k(numbers, k):
    """Variant C: RETURN ALL k-windows with sum >= target"""
    window_sum = sum(numbers[:k])
    result = []
    if window_sum >= k:
        result.append(numbers[:k])
    for i in range(k, len(numbers)):
        window_sum += numbers[i] - numbers[i - k]
        if window_sum >= k:
            result.append(numbers[i-k+1:i+1])
    return result

print("=== PROBLEM 1: MAX SUM SUBARRAY ===")
print("BASE:", max_sum_subarray([2, 1, 5, 1, 3, 2], 3))
print("VARIANT 1A:", max_sum_subarray_product([2, 1, 5, 1, 3, 2], 3))
print("VARIANT 1B:", count_subarray_sum_k([2, 1, 5, 1, 3, 2], 6))
print("VARIANT 1C:", all_subarrays_sum_k([2, 1, 5, 1, 3, 2], 6))
print()


# ============================================================
# PROBLEM 2: Longest Substring Without Repeating
# ============================================================

# BASE: Length of longest substring with no repeats
def length_of_longest_substring(s):
    """Base: length of longest substring with no repeats"""
    last_seen = {}
    left = best = 0
    for right, char in enumerate(s):
        if char in last_seen and last_seen[char] >= left:
            left = last_seen[char] + 1
        last_seen[char] = right
        best = max(best, right - left + 1)
    return best

# VARIANT 2A: Longest with at least one repeat (inverse)
def longest_substring_with_repeats(s):
    """Variant A: longest with AT LEAST one repeat"""
    if len(set(s)) == len(s):
        return 0
    last_seen = {}
    left = 0
    best = 0
    for right, char in enumerate(s):
        if char in last_seen:
            best = max(best, right - left + 1)
        last_seen[char] = right
    return best

# VARIANT 2B: Count substrings with no repeats
def count_substrings_no_repeats(s):
    """Variant B: COUNT how many substrings have no repeats"""
    count = 0
    n = len(s)
    for i in range(n):
        seen = set()
        for j in range(i, n):
            if s[j] in seen:
                break
            seen.add(s[j])
            count += 1
    return count

# VARIANT 2C: Longest with at most k distinct chars
def longest_substring_k_distinct(s, k):
    """Variant C: longest with AT MOST k distinct chars"""
    counts = {}
    left = best = 0
    for right, char in enumerate(s):
        counts[char] = counts.get(char, 0) + 1
        while len(counts) > k:
            counts[s[left]] -= 1
            if counts[s[left]] == 0:
                del counts[s[left]]
            left += 1
        best = max(best, right - left + 1)
    return best

print("=== PROBLEM 2: LONGEST SUBSTRING ===")
print("BASE:", length_of_longest_substring('abcabcbb'))
print("VARIANT 2A:", longest_substring_with_repeats('abcabcbb'))
print("VARIANT 2B:", count_substrings_no_repeats('abc'))
print("VARIANT 2C:", longest_substring_k_distinct('eceba', 2))
print()


# ============================================================
# PROBLEM 3: Shortest Window with Sum >= Threshold
# ============================================================

# BASE: Shortest window with sum >= threshold
def shortest_burst(errors, threshold):
    """Base: shortest window with sum >= threshold"""
    left = total = 0
    best = len(errors) + 1
    for right in range(len(errors)):
        total += errors[right]
        while total >= threshold:
            best = min(best, right - left + 1)
            total -= errors[left]
            left += 1
    return 0 if best == len(errors) + 1 else best

# VARIANT 3A: Window with sum exactly equal to target
def shortest_burst_exact(errors, target):
    """Variant A: window with sum EXACTLY equal to target"""
    left = total = 0
    best = len(errors) + 1
    for right in range(len(errors)):
        total += errors[right]
        while total > target and left <= right:
            total -= errors[left]
            left += 1
        if total == target:
            best = min(best, right - left + 1)
    return best if best != len(errors) + 1 else -1

# VARIANT 3B: Count windows with sum >= threshold
def count_burst_windows(errors, threshold):
    """Variant B: COUNT how many windows sum >= threshold"""
    count = 0
    for i in range(len(errors)):
        s = 0
        for j in range(i, len(errors)):
            s += errors[j]
            if s >= threshold:
                count += 1
    return count

# VARIANT 3C: Longest window with sum >= threshold
def longest_burst(errors, threshold):
    """Variant C: LONGEST window (inverse of shortest)"""
    left = total = 0
    best = 0
    for right in range(len(errors)):
        total += errors[right]
        while total >= threshold:
            best = max(best, right - left + 1)
            total -= errors[left]
            left += 1
    return best

print("=== PROBLEM 3: SHORTEST WINDOW ===")
print("BASE:", shortest_burst([2, 3, 1, 2, 4, 3], 7))
print("VARIANT 3A:", shortest_burst_exact([2, 3, 1, 2, 4, 3], 7))
print("VARIANT 3B:", count_burst_windows([2, 3, 1, 2, 4, 3], 7))
print("VARIANT 3C:", longest_burst([2, 3, 1, 2, 4, 3], 7))
print()


# ============================================================
# PROBLEM 4: Min Window Substring
# ============================================================

# BASE: Shortest substring containing all chars in t
def min_window_substring(s, t):
    """Base: shortest substring containing all chars in t"""
    if not t or not s:
        return ""
    need = {}
    for c in t:
        need[c] = need.get(c, 0) + 1
    missing = len(t)
    have = {}
    left = 0
    best = None
    for right, c in enumerate(s):
        if c in need:
            have[c] = have.get(c, 0) + 1
            if have[c] <= need[c]:
                missing -= 1
        while missing == 0:
            if best is None or right - left + 1 < len(best):
                best = s[left:right + 1]
            c = s[left]
            if c in need:
                have[c] -= 1
                if have[c] < need[c]:
                    missing += 1
            left += 1
    return "" if best is None else best

# VARIANT 4A: Return length instead of substring
def min_window_length(s, t):
    """Variant A: return LENGTH instead of substring"""
    result = min_window_substring(s, t)
    return len(result) if result else 0

# VARIANT 4B: Return all valid windows
def all_windows_containing(s, t):
    """Variant B: return ALL valid windows"""
    if not t or not s:
        return []
    need = {}
    for c in t:
        need[c] = need.get(c, 0) + 1
    result = []
    for i in range(len(s)):
        have = {}
        for j in range(i, len(s)):
            if s[j] in need:
                have[s[j]] = have.get(s[j], 0) + 1
            if all(have.get(c, 0) >= need[c] for c in need):
                result.append(s[i:j+1])
                break
    return result

# VARIANT 4C: Count windows containing all chars
def count_windows_containing(s, t):
    """Variant C: COUNT how many windows contain all chars in t"""
    count = 0
    for i in range(len(s)):
        have = {}
        for j in range(i, len(s)):
            if s[j] in t:
                have[s[j]] = have.get(s[j], 0) + 1
            if all(have.get(c, 0) >= t.count(c) for c in set(t)):
                count += 1
    return count

print("=== PROBLEM 4: MIN WINDOW ===")
print("BASE:", min_window_substring('ADOBECODEBANC', 'ABC'))
print("VARIANT 4A:", min_window_length('ADOBECODEBANC', 'ABC'))
print("VARIANT 4B:", all_windows_containing('ADOBECODEBANC', 'ABC'))
print("VARIANT 4C:", count_windows_containing('ADOBECODEBANC', 'ABC'))
print()


# ============================================================
# PROBLEM 5: Best Time to Buy and Sell Stock
# ============================================================

# BASE: Max profit from one buy-sell transaction
def best_time_buy_sell(prices):
    """Base: max profit from buy then sell"""
    if not prices or len(prices) < 2:
        return 0
    min_price = prices[0]
    max_profit = 0
    for price in prices[1:]:
        max_profit = max(max_profit, price - min_price)
        min_price = min(min_price, price)
    return max_profit

# VARIANT 5A: Multiple transactions allowed
def best_time_multiple_transactions(prices):
    """Variant A: multiple buy-sell transactions allowed"""
    if not prices or len(prices) < 2:
        return 0
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            profit += prices[i] - prices[i-1]
    return profit

# VARIANT 5B: With cooldown (can't trade consecutive days)
def best_time_with_cooldown(prices):
    """Variant B: with cooldown between transactions"""
    if not prices or len(prices) < 2:
        return 0
    n = len(prices)
    buy = [-prices[0], -prices[0]]
    sell = [0, 0]
    for i in range(1, n):
        buy[1] = max(buy[0], sell[0] - prices[i])
        sell[1] = max(sell[0], buy[0] + prices[i])
        buy[0], sell[0] = buy[1], sell[1]
    return sell[1]

# VARIANT 5C: With transaction fee
def best_time_with_fee(prices, fee):
    """Variant C: with transaction fee"""
    if not prices or len(prices) < 2:
        return 0
    hold = -prices[0]
    cash = 0
    for price in prices[1:]:
        hold = max(hold, cash - price)
        cash = max(cash, hold + price - fee)
    return cash

print("=== PROBLEM 5: BEST TIME BUY/SELL ===")
print("BASE:", best_time_buy_sell([7, 1, 5, 3, 6, 4]))
print("VARIANT 5A:", best_time_multiple_transactions([7, 1, 5, 3, 6, 4]))
print("VARIANT 5B:", best_time_with_cooldown([3, 3, 5, 0, 0, 3, 1, 4]))
print("VARIANT 5C:", best_time_with_fee([1, 3, 2, 8, 4, 9], 2))
print()


# ============================================================
# PROBLEM 6: Longest Repeating Character Replacement
# ============================================================

# BASE: Replace at most k chars to make all same
def longest_repeating_character_replacement(s, k):
    """Base: longest substring where replace <=k chars to make all same"""
    count = {}
    left = 0
    best = 0
    for right, char in enumerate(s):
        count[char] = count.get(char, 0) + 1
        window_len = right - left + 1
        most_frequent = max(count.values())
        chars_to_replace = window_len - most_frequent
        if chars_to_replace > k:
            count[s[left]] -= 1
            left += 1
        else:
            best = max(best, window_len)
    return best

# VARIANT 6A: Return the actual substring
def longest_repeating_character_replacement_str(s, k):
    """Variant A: return the actual substring (not length)"""
    count = {}
    left = 0
    best_len = 0
    best_start = 0
    for right, char in enumerate(s):
        count[char] = count.get(char, 0) + 1
        window_len = right - left + 1
        most_frequent = max(count.values()) if count else 0
        chars_to_replace = window_len - most_frequent
        if chars_to_replace > k:
            count[s[left]] -= 1
            left += 1
        else:
            if window_len > best_len:
                best_len = window_len
                best_start = left
    return s[best_start:best_start + best_len]

# VARIANT 6B: Minimum chars to replace (not maximum window)
def min_chars_to_replace(s, k):
    """Variant B: minimum chars to replace (inverse)"""
    return len(s) - longest_repeating_character_replacement(s, k)

# VARIANT 6C: Multiple target characters
def longest_repeating_multi_target(s, k, targets):
    """Variant C: multiple different target characters allowed"""
    count = {}
    left = 0
    best = 0
    for right, char in enumerate(s):
        count[char] = count.get(char, 0) + 1
        window_len = right - left + 1
        most_frequent = max((count[c] for c in targets if c in count), default=0)
        chars_to_replace = window_len - most_frequent
        if chars_to_replace > k:
            count[s[left]] -= 1
            left += 1
        else:
            best = max(best, window_len)
    return best

print("=== PROBLEM 6: LONGEST REPEATING CHAR ===")
print("BASE:", longest_repeating_character_replacement('ABAB', 2))
print("VARIANT 6A:", longest_repeating_character_replacement_str('ABAB', 2))
print("VARIANT 6B:", min_chars_to_replace('ABAB', 2))
print("VARIANT 6C:", longest_repeating_multi_target('ABAB', 2, ['A', 'B']))
print()

print("=" * 60)
print("CATEGORY 2: SLIDING WINDOW PATTERN MASTERY")
print("=" * 60)
print("Core: Fixed vs variable window, threshold-based vs exact")
print("Variants: output format, constraint changes, direction")
print("=" * 60)
