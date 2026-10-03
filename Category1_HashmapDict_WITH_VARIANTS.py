# ============================================================
# Category 1: Hashmap / Dict Problems — WITH VARIANTS
# Core pattern: "check + remember" via dict/set
# Each problem shows BASE + multiple VARIANTS
# ============================================================


# ============================================================
# PROBLEM 1: TWO SUM
# ============================================================

# BASE: Two Sum (find the pair)
# QUESTION: Given a list and target, return TWO numbers that sum to target
# TIME/SPACE: O(n) time, O(n) space
def two_sum(numbers, target):
    """Base problem: return any one pair"""
    seen = {}
    for number in numbers:
        needed = target - number
        if needed in seen:
            return [needed, number]
        seen[number] = True
    return None

print("=== TWO SUM VARIANTS ===")
print("BASE - two_sum([2, 7, 11, 15], 9):", two_sum([2, 7, 11, 15], 9))
print()


# VARIANT 1A: Two Sum — Count the pairs (not return them)
# QUESTION: How many DIFFERENT pairs sum to target?
# E.g., [1, 1, 2, 3] with target=3 → pairs: (1,2) appears once → count = 1
# KEY CHANGE: Instead of returning the pair, count how many valid pairs exist
# TIME/SPACE: O(n) time, O(n) space
def count_pairs_summing_to(numbers, target):
    """Variant: count distinct pairs"""
    seen = set()
    count = 0
    for number in numbers:
        needed = target - number
        if needed in seen and needed != number:  # avoid double-counting
            count += 1
        seen.add(number)
    return count

print("VARIANT 1A - count_pairs_summing_to([1, 5, 7, -1, 5], 6):", count_pairs_summing_to([1, 5, 7, -1, 5], 6))
# Pairs: (1,5) twice, (7,-1) once → but (1,5) is one PAIR type → careful with duplicates
print()


# VARIANT 1B: Two Sum — Return all pairs (not just one)
# QUESTION: Return ALL unique pairs (no duplicates) that sum to target
# E.g., [1, 0, -1, 0, -2, 2] with target=0 → [[-2,2], [-1,1], [0,0]]
# KEY CHANGE: Don't stop at first pair; collect all, deduplicate
# TIME/SPACE: O(n log n) time (sorting for dedup), O(n) space
def all_pairs_summing_to(numbers, target):
    """Variant: return all unique pairs"""
    seen = set()
    pairs = set()
    for number in numbers:
        needed = target - number
        if needed in seen:
            pair = tuple(sorted([number, needed]))
            pairs.add(pair)
        seen.add(number)
    return [list(p) for p in pairs]

print("VARIANT 1B - all_pairs_summing_to([1, 0, -1, 0, -2, 2], 0):", all_pairs_summing_to([1, 0, -1, 0, -2, 2], 0))
print()


# VARIANT 1C: Two Sum — With sorted array and O(1) space (two-pointer instead of hashmap)
# QUESTION: Find pair in SORTED array using O(1) space (no hashmap)
# KEY CHANGE: Use two pointers instead of hashmap
# WHY: Shows the same problem solved differently based on input constraint
# TIME/SPACE: O(n) time, O(1) space
def two_sum_sorted(numbers, target):
    """Variant: sorted array → two-pointer for O(1) space"""
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

print("VARIANT 1C - two_sum_sorted([2, 7, 11, 15], 9):", two_sum_sorted([2, 7, 11, 15], 9))
print()


# ============================================================
# PROBLEM 2: THREE SUM (Extension of Two Sum)
# ============================================================

# BASE: Three Sum (find triplets summing to target, usually 0)
# QUESTION: Find all unique triplets that sum to 0
# KEY INSIGHT: For each number, reduce to "two sum" subproblem on remainder
# E.g., [-1, 0, 1, 2, -1, -4] → [[-1,-1,2], [-1,0,1]]
# TIME/SPACE: O(n²) time (n for outer, n for two-pointer), O(1) space (excluding output)
def three_sum(numbers):
    """Base: return all unique triplets summing to 0"""
    numbers.sort()
    result = []
    for i in range(len(numbers) - 2):
        if i > 0 and numbers[i] == numbers[i - 1]:
            continue  # skip duplicates
        target = -numbers[i]
        left, right = i + 1, len(numbers) - 1
        while left < right:
            s = numbers[left] + numbers[right]
            if s == target:
                result.append([numbers[i], numbers[left], numbers[right]])
                while left < right and numbers[left] == numbers[left + 1]:
                    left += 1
                while left < right and numbers[right] == numbers[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif s < target:
                left += 1
            else:
                right -= 1
    return result

print("=== THREE SUM VARIANTS ===")
print("BASE - three_sum([-1, 0, 1, 2, -1, -4]):", three_sum([-1, 0, 1, 2, -1, -4]))
print()


# VARIANT 2A: Four Sum (K-Sum generalization)
# QUESTION: Find all unique 4-tuples that sum to target (not just 0)
# KEY CHANGE: Outer loop twice, then two-pointer on remainder
# WHY: Shows how two-sum generalizes to k-sum (nested loops)
# TIME/SPACE: O(n³) time, O(1) space
def four_sum(numbers, target):
    """Variant: generalize to 4 numbers with custom target"""
    numbers.sort()
    result = []
    n = len(numbers)
    for i in range(n - 3):
        if i > 0 and numbers[i] == numbers[i - 1]:
            continue
        for j in range(i + 1, n - 2):
            if j > i + 1 and numbers[j] == numbers[j - 1]:
                continue
            left, right = j + 1, n - 1
            while left < right:
                s = numbers[i] + numbers[j] + numbers[left] + numbers[right]
                if s == target:
                    result.append([numbers[i], numbers[j], numbers[left], numbers[right]])
                    while left < right and numbers[left] == numbers[left + 1]:
                        left += 1
                    while left < right and numbers[right] == numbers[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif s < target:
                    left += 1
                else:
                    right -= 1
    return result

print("VARIANT 2A - four_sum([1, 0, -1, 0, -2, 2], 0):", four_sum([1, 0, -1, 0, -2, 2], 0))
print()


# VARIANT 2B: Three Sum Closest
# QUESTION: Find triplet whose sum is CLOSEST to target (not exactly equal)
# E.g., [-1, 2, 1, -4] with target=1 → closest is [-1, 2, 1] = 2 (distance 1 from target)
# KEY CHANGE: Track minimum distance, update best triplet
# WHY: Shows how to adapt three-sum from "equals" to "closest"
# TIME/SPACE: O(n²) time, O(1) space
def three_sum_closest(numbers, target):
    """Variant: find triplet CLOSEST to target, not exactly equal"""
    numbers.sort()
    best_sum = numbers[0] + numbers[1] + numbers[2]
    for i in range(len(numbers) - 2):
        left, right = i + 1, len(numbers) - 1
        while left < right:
            s = numbers[i] + numbers[left] + numbers[right]
            if abs(s - target) < abs(best_sum - target):
                best_sum = s
            if s < target:
                left += 1
            else:
                right -= 1
    return best_sum

print("VARIANT 2B - three_sum_closest([-1, 2, 1, -4], 1):", three_sum_closest([-1, 2, 1, -4], 1))
print()


# ============================================================
# PROBLEM 3: CONTAINS DUPLICATE (Variants)
# ============================================================

# BASE: Contains Duplicate
def contains_duplicate(numbers):
    """Base: any duplicate?"""
    seen = set()
    for number in numbers:
        if number in seen:
            return True
        seen.add(number)
    return False

print("=== CONTAINS DUPLICATE VARIANTS ===")
print("BASE - contains_duplicate([1, 2, 3, 2]):", contains_duplicate([1, 2, 3, 2]))
print()


# VARIANT 3A: Contains Duplicate Within Distance K
# QUESTION: Are there two identical numbers within distance k in array?
# E.g., [99, 99] with k=2 → True (distance 1 < 2)
#       [1, 0, 1, 1] with k=1 → False (closest 1's are distance 2 apart)
# KEY CHANGE: Use sliding window of size k, check for duplicates in window
# WHY: Combines set idea with sliding window
# TIME/SPACE: O(n*k) time worst case, O(min(n, k)) space
def contains_duplicate_within_distance_k(numbers, k):
    """Variant: duplicates must be within distance k"""
    seen = set()
    for i, num in enumerate(numbers):
        if num in seen:
            return True
        seen.add(num)
        if len(seen) > k:
            seen.remove(numbers[i - k])
    return False

print("VARIANT 3A - contains_duplicate_within_distance_k([99, 99], 2):", contains_duplicate_within_distance_k([99, 99], 2))
print("VARIANT 3A - contains_duplicate_within_distance_k([1, 0, 1, 1], 1):", contains_duplicate_within_distance_k([1, 0, 1, 1], 1))
print()


# VARIANT 3B: First Duplicate (not just boolean, return the value)
# QUESTION: Return the first duplicate found, or None if none exists
# E.g., [4, 1, 2, 1, 3] → 1 (first duplicate encountered)
# KEY CHANGE: Return the value, not boolean
# WHY: Small change to output, same algorithm
# TIME/SPACE: O(n) time, O(n) space
def first_duplicate(numbers):
    """Variant: return first duplicate value, not boolean"""
    seen = set()
    for number in numbers:
        if number in seen:
            return number
        seen.add(number)
    return None

print("VARIANT 3B - first_duplicate([4, 1, 2, 1, 3]):", first_duplicate([4, 1, 2, 1, 3]))
print()


# ============================================================
# PROBLEM 4: COUNT ALL (Frequency Map) — Variants
# ============================================================

# BASE: Count All
def count_all(numbers):
    """Base: frequency map of all values"""
    counts = {}
    for number in numbers:
        counts[number] = counts.get(number, 0) + 1
    return counts

print("=== COUNT ALL VARIANTS ===")
print("BASE - count_all([1, 2, 2, 3, 2, 1]):", count_all([1, 2, 2, 3, 2, 1]))
print()


# VARIANT 4A: Count with minimum threshold
# QUESTION: Return only values that appear at least K times
# E.g., count_at_least_k([1, 1, 2, 2, 2, 3], k=2) → {1: 2, 2: 3}
# KEY CHANGE: Filter the frequency map after building it
# WHY: Shows filtering/post-processing after counting
# TIME/SPACE: O(n + k) time (k = size of result), O(n) space
def count_at_least_k(numbers, k):
    """Variant: only values appearing >= k times"""
    counts = count_all(numbers)
    return {v: c for v, c in counts.items() if c >= k}

print("VARIANT 4A - count_at_least_k([1, 1, 2, 2, 2, 3], 2):", count_at_least_k([1, 1, 2, 2, 2, 3], 2))
print()


# VARIANT 4B: Top K Frequent Elements
# QUESTION: Return K most frequent values (not their counts)
# E.g., top_k_frequent([1, 1, 1, 2, 2, 3], k=2) → [1, 2]
# KEY CHANGE: Sort by frequency, take top k
# WHY: Introduces heap/sorting after frequency counting
# TIME/SPACE: O(n log k) time (using heap), O(n) space
def top_k_frequent(numbers, k):
    """Variant: return K most frequent values"""
    counts = count_all(numbers)
    import heapq
    return [v for v, _ in heapq.nlargest(k, counts.items(), key=lambda x: x[1])]

print("VARIANT 4B - top_k_frequent([1, 1, 1, 2, 2, 3], 2):", top_k_frequent([1, 1, 1, 2, 2, 3], 2))
print()


# VARIANT 4C: Group by frequency
# QUESTION: Group values by their frequency
# E.g., [1, 1, 1, 2, 2, 3] → {1: [2, 3], 2: [1, 2, 2, 2], 3: [1]}
# Wait, that's wrong. Should be: frequency -> values
# {3: [1], 2: [2], 1: [3]} (3 appears 3 times, 2 appears 2 times, etc.)
# KEY CHANGE: Invert the map (frequency is key, values are grouped)
# WHY: Shows different grouping strategies
# TIME/SPACE: O(n) time, O(n) space
def group_by_frequency(numbers):
    """Variant: group values by their frequency"""
    counts = count_all(numbers)
    freq_map = {}
    for value, count in counts.items():
        if count not in freq_map:
            freq_map[count] = []
        freq_map[count].append(value)
    return freq_map

print("VARIANT 4C - group_by_frequency([1, 1, 1, 2, 2, 3]):", group_by_frequency([1, 1, 1, 2, 2, 3]))
print()


# ============================================================
# SUMMARY: How to Apply Variants
# ============================================================
print("=" * 60)
print("VARIANT PATTERN SUMMARY")
print("=" * 60)
print("""
Each problem type can be extended:

1. TWO SUM variants:
   - Count pairs (not return)
   - Return all pairs (not just one)
   - Different data structure (sorted → two-pointer)
   - EXTEND TO: Three Sum, Four Sum, K-Sum

2. DUPLICATES variants:
   - Boolean (any duplicate?) → First duplicate value
   - Add constraint (within distance k)
   - Return count vs. return value

3. FREQUENCY variants:
   - Full map → Filtered map
   - Top K → Group by frequency
   - Add constraints (minimum threshold)

KEY INSIGHT:
The core "check + remember" pattern stays the same.
Variants change:
  - Output format (boolean → value → count → all)
  - Constraints (distance, frequency threshold)
  - Data structure (dict → heap → sorted)
  - Generalization (2-sum → 3-sum → k-sum)

INTERVIEW TIP:
When a problem seems "similar but different", it's usually
one of these variants. Recognize the core pattern first,
then adapt it to the new constraint.
""")
