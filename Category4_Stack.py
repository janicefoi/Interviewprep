# ============================================================
# Category 4: Stack — BASE PROBLEMS + EXHAUSTIVE VARIANTS
# Core pattern: LIFO for pattern matching, or monotonic stack
# ============================================================

from collections import deque

# ============================================================
# PROBLEM 1: VALID PARENTHESES
# ============================================================
# What it solves: Check if brackets are properly balanced and nested
# Example: "({[]})" is valid, "({[}])" is invalid (mismatch order)
# Why stack: LIFO ensures inner brackets close before outer ones
# Interview angle: Often asked with follow-ups about minimum edits

# BASE: Check if balanced
def is_valid_parentheses(s):
    """Base: check if brackets balanced and properly nested"""
    pairs = {'(': ')', '[': ']', '{': '}'}
    stack = []
    for char in s:
        if char in pairs:
            stack.append(char)
        else:
            if not stack or pairs[stack.pop()] != char:
                return False
    return len(stack) == 0

# VARIANT 1A: Return score (1 per pair, double when nested)
def score_parentheses(s):
    """Variant A: score = 1 per pair, 2x when nested. E.g., '(())' = 4"""
    stack = [0]
    for char in s:
        if char == '(':
            stack.append(0)
        else:
            v = stack.pop()
            stack[-1] += max(1, 2 * v)
    return stack[0]

# VARIANT 1B: Minimum removals to make valid
def min_removals_to_valid(s):
    """Variant B: min chars to remove to make valid. E.g., '()(()'→ remove 1"""
    open_count = 0
    removals = 0
    for char in s:
        if char == '(':
            open_count += 1
        elif char == ')':
            if open_count > 0:
                open_count -= 1
            else:
                removals += 1
    return removals + open_count

# VARIANT 1C: Minimum insertions to make valid
def min_insertions_to_valid(s):
    """Variant C: min chars to INSERT to make valid"""
    open_needed = 0
    close_needed = 0
    for char in s:
        if char == '(':
            close_needed += 1
        elif char == ')':
            if close_needed > 0:
                close_needed -= 1
            else:
                open_needed += 1
    return open_needed + close_needed

# VARIANT 1D: Minimum swaps to make valid (THIS IS THE ONE YOU MENTIONED!)
def min_swaps_to_valid(s):
    """Variant D: min SWAPS to balance. Only '(' and ')' allowed.
    Key insight: we can only swap adjacent mismatched pairs.
    Count imbalance, each 2 imbalance needs 1 swap."""
    if len(s) % 2 == 1:
        return -1
    open_count = 0
    imbalance = 0
    for char in s:
        if char == '(':
            open_count += 1
        else:
            open_count -= 1
            if open_count < 0:
                imbalance += 1
                open_count = 1
    return (imbalance + 1) // 2

# VARIANT 1E: Longest valid parentheses substring
def longest_valid_parentheses(s):
    """Variant E: length of longest valid substring. E.g., '()(()'→ 2"""
    stack = [-1]
    max_len = 0
    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                max_len = max(max_len, i - stack[-1])
    return max_len

# VARIANT 1F: Find indices of unmatched brackets
def find_unmatched_indices(s):
    """Variant F: return indices of unmatched brackets"""
    stack = []
    matched = set()
    for i, char in enumerate(s):
        if char in '([{':
            stack.append(i)
        elif char in ')]}':
            if stack:
                matched.add(stack.pop())
                matched.add(i)
    return [i for i in range(len(s)) if i not in matched]

print("=== PROBLEM 1: VALID PARENTHESES ===")
print("BASE:", is_valid_parentheses('({[]})'))
print("VARIANT 1A (score):", score_parentheses('(())'))
print("VARIANT 1B (min removals):", min_removals_to_valid('())('))
print("VARIANT 1C (min insertions):", min_insertions_to_valid('())(('))
print("VARIANT 1D (min swaps):", min_swaps_to_valid('))(('))
print("VARIANT 1E (longest valid):", longest_valid_parentheses('()(()')))
print("VARIANT 1F (unmatched indices):", find_unmatched_indices('(]'))
print()


# ============================================================
# PROBLEM 2: REMOVE ADJACENT DUPLICATES
# ============================================================
# What it solves: Collapse adjacent matching characters recursively
# Example: "abbaca" → "aa" → "" (first b's cancel, then a's)
# Why stack: Simulates the cascading removal process
# Interview angle: Often followed by "what if you can only remove K"

# BASE: Remove adjacent duplicates
def remove_adjacent_duplicates(s):
    """Base: collapse adjacent matching chars"""
    stack = []
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    return ''.join(stack)

# VARIANT 2A: Remove duplicates appearing > K times
def remove_duplicates_k_times(s, k):
    """Variant A: collapse when char appears >= k consecutive times"""
    stack = []
    for char in s:
        if len(stack) >= k - 1 and all(c == char for c in stack[-(k-1):]) and stack and stack[-1] == char:
            for _ in range(k - 1):
                stack.pop()
        else:
            stack.append(char)
    return ''.join(stack)

# VARIANT 2B: Collect all removed pairs
def collect_removed_pairs(s):
    """Variant B: return list of pairs that were removed"""
    stack = []
    pairs = []
    for char in s:
        if stack and stack[-1] == char:
            pairs.append((stack.pop(), char))
        else:
            stack.append(char)
    return pairs

# VARIANT 2C: With custom removal rule (not adjacent)
def custom_removal_rule(s, rule):
    """Variant C: remove based on custom function rule(prev, curr)"""
    stack = []
    for char in s:
        if stack and rule(stack[-1], char):
            stack.pop()
        else:
            stack.append(char)
    return ''.join(stack)

print("=== PROBLEM 2: REMOVE ADJACENT DUPLICATES ===")
print("BASE:", remove_adjacent_duplicates('abbaca'))
print("VARIANT 2A (remove >= 2):", remove_duplicates_k_times('aabbcc', 2))
print("VARIANT 2B (collect pairs):", collect_removed_pairs('abbaca'))
print("VARIANT 2C (custom: vowel-consonant):", custom_removal_rule('aebdc', lambda p, c: (p in 'aeiou') != (c in 'aeiou')))
print()


# ============================================================
# PROBLEM 3: MINSTACK
# ============================================================
# What it solves: Stack with O(1) access to minimum value
# Use case: When you need both push/pop/top AND min at any time
# Strategy: Dual stack (one for values, one for mins)
# Interview angle: Extend to also track max? K-th largest?

# BASE: Stack with O(1) min
class MinStack:
    """Base: stack with O(1) get_min"""
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        val = self.stack.pop()
        if val == self.min_stack[-1]:
            self.min_stack.pop()
        return val

    def top(self):
        return self.stack[-1]

    def get_min(self):
        return self.min_stack[-1]

# VARIANT 3A: MaxStack (parallel to MinStack)
class MaxStack:
    """Variant A: stack with O(1) get_max"""
    def __init__(self):
        self.stack = []
        self.max_stack = []

    def push(self, val):
        self.stack.append(val)
        if not self.max_stack or val >= self.max_stack[-1]:
            self.max_stack.append(val)

    def pop(self):
        val = self.stack.pop()
        if val == self.max_stack[-1]:
            self.max_stack.pop()
        return val

    def top(self):
        return self.stack[-1]

    def get_max(self):
        return self.max_stack[-1]

# VARIANT 3B: Get K-th largest
class KthLargestStack:
    """Variant B: track K largest values"""
    def __init__(self, k):
        self.stack = []
        self.k_largest = []
        self.k = k

    def push(self, val):
        self.stack.append(val)
        import heapq
        if len(self.k_largest) < self.k:
            heapq.heappush(self.k_largest, val)
        elif val > self.k_largest[0]:
            heapq.heapreplace(self.k_largest, val)

    def pop(self):
        return self.stack.pop()

    def get_kth_largest(self):
        return self.k_largest[0] if len(self.k_largest) == self.k else None

# VARIANT 3C: Range min/max queries
class RangeStackQueries:
    """Variant C: query min/max over ranges"""
    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        return self.stack.pop()

    def range_min(self, start, end):
        return min(self.stack[start:end+1]) if start <= end < len(self.stack) else None

    def range_max(self, start, end):
        return max(self.stack[start:end+1]) if start <= end < len(self.stack) else None

ms = MinStack()
for v in [3, 1, 4, 1, 5]:
    ms.push(v)
print("=== PROBLEM 3: MINSTACK ===")
print("BASE MinStack: top =", ms.top(), ", min =", ms.get_min())

ms2 = MaxStack()
for v in [3, 1, 4, 1, 5]:
    ms2.push(v)
print("VARIANT 3A MaxStack: top =", ms2.top(), ", max =", ms2.get_max())
print()


# ============================================================
# PROBLEM 4: NEXT GREATER ELEMENT
# ============================================================
# What it solves: For each element, find next larger to the right
# Naive: O(n²) nested loops. Optimal: O(n) monotonic stack
# Key insight: Maintain decreasing order, pop when larger found
# Interview angle: Left instead of right? Circular array?

# BASE: Next greater to the right
def next_greater_element(nums):
    """Base: for each element, next greater to the right"""
    result = [-1] * len(nums)
    stack = []
    for i in range(len(nums) - 1, -1, -1):
        while stack and stack[-1] <= nums[i]:
            stack.pop()
        if stack:
            result[i] = stack[-1]
        stack.append(nums[i])
    return result

# VARIANT 4A: Previous greater (to the left)
def previous_greater_element(nums):
    """Variant A: previous greater element to the left"""
    result = [-1] * len(nums)
    stack = []
    for i in range(len(nums)):
        while stack and stack[-1] <= nums[i]:
            stack.pop()
        if stack:
            result[i] = stack[-1]
        stack.append(nums[i])
    return result

# VARIANT 4B: Circular array (wraps around)
def next_greater_circular(nums):
    """Variant B: next greater in circular array"""
    n = len(nums)
    result = [-1] * n
    stack = []
    for i in range(2 * n):
        while stack and nums[stack[-1]] < nums[i % n]:
            result[stack.pop()] = nums[i % n]
        stack.append(i % n)
    return result

# VARIANT 4C: Distance to next greater
def distance_to_next_greater(nums):
    """Variant C: distance (index difference) to next greater"""
    result = [-1] * len(nums)
    stack = []
    for i in range(len(nums) - 1, -1, -1):
        while stack and nums[stack[-1]] <= nums[i]:
            stack.pop()
        if stack:
            result[i] = stack[-1] - i
        stack.append(i)
    return result

print("=== PROBLEM 4: NEXT GREATER ELEMENT ===")
print("BASE:", next_greater_element([1, 3, 2, 4]))
print("VARIANT 4A (previous):", previous_greater_element([1, 3, 2, 4]))
print("VARIANT 4B (circular):", next_greater_circular([1, 2, 1]))
print("VARIANT 4C (distance):", distance_to_next_greater([1, 3, 2, 4]))
print()


# ============================================================
# PROBLEM 5: DAILY TEMPERATURES
# ============================================================
# What it solves: Days until warmer temperature for each day
# Example: [73, 74, 75, 71] → [1, 1, 2, 0] (wait 1, 1, 2, never days)
# Similar to next greater but tracking distances
# Interview angle: Cooler instead? Multiple thresholds?

# BASE: Days until warmer
def daily_temperatures(temps):
    """Base: days until warmer temp for each day"""
    result = [0] * len(temps)
    stack = []
    for i, t in enumerate(temps):
        while stack and temps[stack[-1]] < t:
            result[stack.pop()] = i - stack[-1]
        stack.append(i)
    return result

# VARIANT 5A: Days until cooler
def daily_cooler(temps):
    """Variant A: days until cooler temp"""
    result = [0] * len(temps)
    stack = []
    for i, t in enumerate(temps):
        while stack and temps[stack[-1]] > t:
            result[stack.pop()] = i - stack[-1]
        stack.append(i)
    return result

# VARIANT 5B: Return actual temperatures (not distances)
def next_warmer_temps(temps):
    """Variant B: next warmer temperature (not distance)"""
    result = [-1] * len(temps)
    stack = []
    for i, t in enumerate(temps):
        while stack and temps[stack[-1]] < t:
            result[stack.pop()] = t
        stack.append(i)
    return result

# VARIANT 5C: Multiple temp thresholds
def days_until_threshold(temps, threshold):
    """Variant C: days until temp >= threshold"""
    result = [0] * len(temps)
    for i in range(len(temps)):
        for j in range(i + 1, len(temps)):
            if temps[j] >= threshold:
                result[i] = j - i
                break
    return result

print("=== PROBLEM 5: DAILY TEMPERATURES ===")
print("BASE:", daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]))
print("VARIANT 5A (cooler):", daily_cooler([73, 74, 75, 71, 69, 72, 76, 73]))
print("VARIANT 5B (next temp):", next_warmer_temps([73, 74, 75, 71, 69, 72, 76, 73]))
print()

print("=" * 70)
print("CATEGORY 4: STACK PATTERN MASTERY")
print("=" * 70)
print("Pattern 1: Pattern matching (parentheses, adjacent duplicates)")
print("Pattern 2: Monotonic stack (next greater, daily temps)")
print("Pattern 3: Dual tracking (min/max stack)")
print("=" * 70)
