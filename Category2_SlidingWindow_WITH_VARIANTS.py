# ============================================================
# Category 2: Sliding Window — WITH VARIANTS
# ============================================================

# PROBLEM 1: Max Sum Subarray (Fixed Window)
def max_sum_subarray(numbers, k):
    """BASE: max sum of k consecutive elements"""
    window_sum = sum(numbers[:k])
    best = window_sum
    for i in range(k, len(numbers)):
        window_sum += numbers[i] - numbers[i - k]
        best = max(best, window_sum)
    return best

def max_sum_subarray_product(numbers, k):
    """VARIANT A: max PRODUCT instead of sum"""
    window_prod = 1
    for i in range(k):
        window_prod *= numbers[i]
    best = window_prod
    for i in range(k, len(numbers)):
        window_prod = (window_prod // numbers[i - k]) * numbers[i]
        best = max(best, window_prod)
    return best

def count_subarray_sum_k(numbers, k):
    """VARIANT B: COUNT how many k-windows have sum >= target (not max sum)"""
    count = 0
    target = sum(numbers[:k])
    if target >= k:
        count += 1
    for i in range(k, len(numbers)):
        s = sum(numbers[i-k+1:i+1])
        if s >= k:
            count += 1
    return count

def all_subarrays_sum_k(numbers, k):
    """VARIANT C: RETURN ALL k-windows with sum >= target"""
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
print("VARIANT A (product):", max_sum_subarray_product([2, 1, 5, 1, 3, 2], 3))
print("VARIANT B (count >= k):", count_subarray_sum_k([2, 1, 5, 1, 3, 2], 6))
print("VARIANT C (return all):", all_subarrays_sum_k([2, 1, 5, 1, 3, 2], 6))
print()


# PROBLEM 2: Longest Substring Without Repeating
def length_of_longest_substring(s):
    """BASE: length of longest substring with no repeats"""
    last_seen = {}
    left = best = 0
    for right, char in enumerate(s):
        if char in last_seen and last_seen[char] >= left:
            left = last_seen[char] + 1
        last_seen[char] = right
        best = max(best, right - left + 1)
    return best

def longest_substring_with_repeats(s):
    """VARIANT A: longest with AT LEAST one repeat (inverse constraint)"""
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

def count_substrings_no_repeats(s):
    """VARIANT B: COUNT how many substrings have no repeats"""
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

def longest_substring_k_distinct(s, k):
    """VARIANT C: longest with AT MOST k distinct chars"""
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
print("VARIANT A (with repeats):", longest_substring_with_repeats('abcabcbb'))
print("VARIANT B (count):", count_substrings_no_repeats('abc'))
print("VARIANT C (k distinct):", longest_substring_k_distinct('eceba', 2))
print()


# PROBLEM 3: Shortest Burst (At-Least-Threshold)
def shortest_burst(errors, threshold):
    """BASE: shortest window with sum >= threshold"""
    left = total = 0
    best = len(errors) + 1
    for right in range(len(errors)):
        total += errors[right]
        while total >= threshold:
            best = min(best, right - left + 1)
            total -= errors[left]
            left += 1
    return 0 if best == len(errors) + 1 else best

def shortest_burst_exact(errors, target):
    """VARIANT A: window with sum EXACTLY equal to target"""
    count = 0
    left = total = 0
    best = len(errors) + 1
    for right in range(len(errors)):
        total += errors[right]
        while total > target and left <= right:
            total -= errors[left]
            left += 1
        if total == target:
            best = min(best, right - left + 1)
            count += 1
    return best if best != len(errors) + 1 else -1

def count_burst_windows(errors, threshold):
    """VARIANT B: COUNT how many windows sum >= threshold"""
    count = 0
    for i in range(len(errors)):
        s = 0
        for j in range(i, len(errors)):
            s += errors[j]
            if s >= threshold:
                count += 1
    return count

def longest_burst(errors, threshold):
    """VARIANT C: LONGEST window (inverse of shortest)"""
    left = total = 0
    best = 0
    for right in range(len(errors)):
        total += errors[right]
        while total >= threshold:
            best = max(best, right - left + 1)
            total -= errors[left]
            left += 1
    return best

print("=== PROBLEM 3: SHORTEST BURST ===")
print("BASE:", shortest_burst([2, 3, 1, 2, 4, 3], 7))
print("VARIANT A (exact):", shortest_burst_exact([2, 3, 1, 2, 4, 3], 7))
print("VARIANT B (count):", count_burst_windows([2, 3, 1, 2, 4, 3], 7))
print("VARIANT C (longest):", longest_burst([2, 3, 1, 2, 4, 3], 7))
print()


# PROBLEM 4: Min Window Substring
def min_window_substring(s, t):
    """BASE: shortest substring containing all chars in t"""
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

def min_window_length(s, t):
    """VARIANT A: return LENGTH instead of substring"""
    result = min_window_substring(s, t)
    return len(result) if result else 0

def all_windows_containing(s, t):
    """VARIANT B: return ALL valid windows (not just shortest)"""
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

def count_windows_containing(s, t):
    """VARIANT C: COUNT how many windows contain all chars in t"""
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
print("VARIANT A (length):", min_window_length('ADOBECODEBANC', 'ABC'))
print("VARIANT B (all):", all_windows_containing('ADOBECODEBANC', 'ABC'))
print("VARIANT C (count):", count_windows_containing('ADOBECODEBANC', 'ABC'))
print()

print("=" * 60)
print("SLIDING WINDOW VARIANT PATTERNS:")
print("- Max → Count → Return all")
print("- Fixed window → Variable window")
print("- Substring → Contiguous array")
print("- Threshold (>=) → Exact (==) → Range")
print("=" * 60)
