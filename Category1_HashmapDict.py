# ============================================================
# Category 1: Hashmap / Dict Problems
# Core pattern: "check + remember" via dict/set
# ============================================================


# ---- PROBLEM 1: Two Sum ----
# QUESTION:
#   Given a list of numbers and a target sum, return ANY two numbers
#   that add up to the target. Assume exactly one valid pair exists.
#
# EXPLANATION:
#   This is the FOUNDATION of the "check + remember" pattern. Before
#   hashing, you'd check every pair (O(n²)). With a hashmap:
#   - As you loop through, compute what number would "complete" the pair
#   - Check if that complement is already in your "seen" set
#   - If yes, you found it. If no, remember THIS number for later.
#
# WHEN YOU'D SEE THIS:
#   - Classic warm-up problem
#   - Variants: two sum in sorted array (two-pointer), k-sum (nested loops)
#   - Shows up as a sub-problem in many medium questions
#
# TIME/SPACE: O(n) time, O(n) space
def two_sum(numbers, target):
    seen = {}
    for number in numbers:
        needed = target - number
        if needed in seen:
            return [needed, number]
        seen[number] = True
    return None

print("two_sum([2, 7, 11, 15], 9):", two_sum([2, 7, 11, 15], 9))
print()


# ---- PROBLEM 2: Contains Duplicate ----
# QUESTION:
#   Given a list of numbers, return True if any value appears more than
#   once (a duplicate exists), False if all unique.
#
# EXPLANATION:
#   This teaches the most basic "check + remember": as you scan through,
#   check if you've already seen this number. If yes, it's a duplicate.
#   If no, remember it. The hashset is a perfect tool because membership
#   checking (`in seen`) is O(1).
#   Compare to sorting (O(n log n)) or nested loop (O(n²)).
#
# WHEN YOU'D SEE THIS:
#   - Standalone warm-up, OR
#   - As part of a larger problem ("is there a duplicate within k positions?")
#
# TIME/SPACE: O(n) time, O(n) space
def contains_duplicate(numbers):
    seen = set()
    for number in numbers:
        if number in seen:
            return True
        seen.add(number)
    return False

print("contains_duplicate([1, 2, 3, 2]):", contains_duplicate([1, 2, 3, 2]))
print()


# ---- PROBLEM 3: Valid Anagram ----
# QUESTION:
#   Given two strings, return True if the second is an anagram of the first
#   (same letters, same counts, any order). E.g., "listen" and "silent".
#
# EXPLANATION:
#   Anagrams have matching letter counts. Build a frequency dict for the
#   first string, then verify the second string "consumes" exactly those
#   frequencies. This extends "check + remember" to counting.
#   Alternative (cleaner) approach: sort both and compare, but that's O(n log n).
#   Dictionary approach is O(n).
#
# WHEN YOU'D SEE THIS:
#   - Standalone or as a helper in a larger problem
#   - Often paired with "group all anagrams together" (Problem 4)
#
# TIME/SPACE: O(n + m) time, O(n) space
def is_anagram(s, t):
    if len(s) != len(t):
        return False
    counts_s = {}
    for c in s:
        counts_s[c] = counts_s.get(c, 0) + 1
    for c in t:
        if c not in counts_s:
            return False
        counts_s[c] -= 1
        if counts_s[c] < 0:
            return False
    return True

print("is_anagram('listen', 'silent'):", is_anagram('listen', 'silent'))
print()


# ---- PROBLEM 4: Group Anagrams ----
# QUESTION:
#   Given a list of strings, return groups of anagrams together.
#   E.g., ['eat', 'tea', 'ate', 'nat', 'tan', 'bat'] → [['eat','tea','ate'], ['nat','tan'], ['bat']]
#
# EXPLANATION:
#   The KEY insight: if two words are anagrams, they have the same SORTED
#   form. Use sorted form as a hashmap key to group them. This combines
#   "check + remember" with grouping.
#   Example: sorted('listen') = 'eilnst', sorted('silent') = 'eilnst' → same key!
#
# WHEN YOU'D SEE THIS:
#   - Common medium problem
#   - Tests "use a hashmap as a grouper" pattern
#
# TIME/SPACE: O(n*k log k) time (k = avg word length, sorting dominates)
#            O(n*k) space
def group_anagrams(words):
    groups = {}
    for word in words:
        key = ''.join(sorted(word))  # sorted form is the grouping key
        if key not in groups:
            groups[key] = []
        groups[key].append(word)
    return list(groups.values())

print("group_anagrams(['eat', 'tea', 'ate', 'nat', 'tan']):", group_anagrams(['eat', 'tea', 'ate', 'nat', 'tan']))
print()


# ---- PROBLEM 5: Count All (Frequency Map) ----
# QUESTION:
#   Given a list of numbers, build a dictionary showing how many times
#   each unique number appears.
#   E.g., [1, 2, 2, 3, 2, 1] → {1: 2, 2: 3, 3: 1}
#
# EXPLANATION:
#   This is the pure "accumulator" version of "check + remember".
#   For each element, increment its count. The result is a frequency map
#   used by many other problems (most_frequent, least_frequent, etc.).
#
# WHEN YOU'D SEE THIS:
#   - Rarely standalone, but constantly as a helper function
#   - Interview trick: "build this first, THEN answer the question"
#
# TIME/SPACE: O(n) time, O(k) space (k = distinct values)
def count_all(numbers):
    counts = {}
    for number in numbers:
        counts[number] = counts.get(number, 0) + 1
    return counts

print("count_all([1, 2, 2, 3, 2, 1]):", count_all([1, 2, 2, 3, 2, 1]))
print()


# ---- PROBLEM 6: Most Frequent ----
# QUESTION:
#   Given a list of numbers, return the number that appears most often.
#   (If tie, return any one.)
#
# EXPLANATION:
#   Build the frequency map (Problem 5), then scan it for the highest count.
#   This is a two-step pattern:
#     Step 1: "check + remember" → build frequency dict
#     Step 2: "best-so-far" → scan for the max
#   Many interview problems use this two-step approach.
#
# WHEN YOU'D SEE THIS:
#   - Warm-up or component of larger problems
#   - Variant: "k most frequent" (use a heap)
#
# TIME/SPACE: O(n) time, O(n) space
def most_frequent(numbers):
    counts = count_all(numbers)
    best_value = None
    best_count = 0
    for value, count in counts.items():
        if count > best_count:
            best_value = value
            best_count = count
    return best_value

print("most_frequent([1, 2, 2, 3, 2, 1]):", most_frequent([1, 2, 2, 3, 2, 1]))
print()


# ---- PROBLEM 7: Two Sum (Sorted Array, Two-Pointer Variant) ----
# QUESTION:
#   Given a SORTED list of numbers and a target, return two numbers
#   that sum to the target. (Same as Problem 1, but input is sorted.)
#
# EXPLANATION:
#   When the array is SORTED, you can use TWO POINTERS instead of hashmap!
#   Start with left at beginning, right at end:
#     - If sum is too small, move left pointer right (increase sum)
#     - If sum is too big, move right pointer left (decrease sum)
#   This is O(n) time but O(1) space (no extra hashmap).
#   KEY LEARNING: Sorting can enable different, sometimes better algorithms.
#
# WHEN YOU'D SEE THIS:
#   - Follow-up to Problem 1: "your solution uses O(n) space.
#     What if the array is sorted and you must use O(1) space?"
#   - Teaches the "two-pointer" mindset (Category 3)
#
# TIME/SPACE: O(n) time, O(1) space (if you don't count the sort)
def two_sum_sorted(numbers, target):
    left, right = 0, len(numbers) - 1
    while left < right:
        s = numbers[left] + numbers[right]
        if s == target:
            return [numbers[left], numbers[right]]
        elif s < target:
            left += 1
        else:
            right -= 1
    return None

print("two_sum_sorted([2, 7, 11, 15], 9):", two_sum_sorted([2, 7, 11, 15], 9))
print()


# ---- PROBLEM 8: Has Pair Summing To ----
# QUESTION:
#   Given a list of numbers and a target, return True if ANY two numbers
#   (distinct positions, but value can repeat) sum to the target.
#   Return False if no such pair exists.
#
# EXPLANATION:
#   This is "check + remember" with a boolean outcome instead of returning
#   the pair. It's the same algorithm as Problem 1 but tests whether you
#   can adapt the pattern to different return types.
#   Also commonly phrased as "can we make the target?" or "does a pair exist?"
#
# WHEN YOU'D SEE THIS:
#   - Slightly different framing than Problem 1 (True/False vs return the pair)
#   - Tests "can you adapt the pattern?"
#
# TIME/SPACE: O(n) time, O(n) space
def has_pair_summing_to(numbers, target):
    seen = set()
    for number in numbers:
        needed = target - number
        if needed in seen:
            return True
        seen.add(number)
    return False

print("has_pair_summing_to([20, 30, 15], 50):", has_pair_summing_to([20, 30, 15], 50))
print()


# ---- PROBLEM 9: Common Elements (Set Intersection) ----
# QUESTION:
#   Given two lists, return a new list of elements that appear in BOTH lists.
#   E.g., [1, 2, 3, 4] and [3, 4, 5, 6] → [3, 4]
#
# EXPLANATION:
#   Use the first list to build a "seen" set. Then loop through the second
#   list and collect anything that's in "seen". This is "check + remember"
#   but specifically for finding intersection (common elements).
#   Alternative: use Python's set intersection operator (`set(list1) & set(list2)`),
#   but the manual approach teaches the pattern.
#
# WHEN YOU'D SEE THIS:
#   - Warm-up or component of graph/matching problems
#   - Variant: "unique common elements" (dedup the result)
#
# TIME/SPACE: O(n + m) time, O(min(n, m)) space
def common_elements(list1, list2):
    seen = set(list1)
    result = []
    for number in list2:
        if number in seen:
            result.append(number)
    return result

print("common_elements([1, 2, 3, 4], [3, 4, 5, 6]):", common_elements([1, 2, 3, 4], [3, 4, 5, 6]))
print()


# ---- PROBLEM 10: Least Frequent ----
# QUESTION:
#   Given a list of numbers, return the number that appears LEAST often
#   (fewest times). (If tie, return any one.)
#
# EXPLANATION:
#   This is the inverse of "most_frequent" (Problem 6). Same two-step pattern:
#     Step 1: Build frequency map
#     Step 2: Scan for the MINIMUM count
#   The only difference is the comparison (`<` instead of `>`).
#   GOTCHA: Initialize best_count to None, not 0, because some counts might
#   be less than 0 (which shouldn't happen with frequencies, but the pattern
#   shows up in other problems).
#
# WHEN YOU'D SEE THIS:
#   - Parallel to "most_frequent"
#   - Tests whether you can flip the comparison
#
# TIME/SPACE: O(n) time, O(n) space
def least_frequent(numbers):
    counts = count_all(numbers)
    best_value = None
    best_count = None
    for value, count in counts.items():
        if best_count is None or count < best_count:
            best_value = value
            best_count = count
    return best_value

print("least_frequent([1, 1, 2, 3, 3, 3]):", least_frequent([1, 1, 2, 3, 3, 3]))
