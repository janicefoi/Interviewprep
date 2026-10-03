# ============================================================
# Category 1: Hashmap / Dict — BASE PROBLEMS + VARIANTS
# Core pattern: "check + remember" via dict/set for O(1) lookups
# ============================================================

# ============================================================
# PROBLEM 1: TWO SUM
# ============================================================

# BASE: Find any pair summing to target
def two_sum(numbers, target):
    """Base: return any one pair"""
    seen = {}
    for number in numbers:
        needed = target - number
        if needed in seen:
            return [needed, number]
        seen[number] = True
    return None

# VARIANT 1A: Count distinct pairs
def count_pairs_summing_to(numbers, target):
    """Variant A: count distinct pairs"""
    seen = set()
    count = 0
    for number in numbers:
        needed = target - number
        if needed in seen and needed != number:
            count += 1
        seen.add(number)
    return count

# VARIANT 1B: Return all pairs
def all_pairs_summing_to(numbers, target):
    """Variant B: return all unique pairs"""
    seen = set()
    pairs = set()
    for number in numbers:
        needed = target - number
        if needed in seen:
            pair = tuple(sorted([number, needed]))
            pairs.add(pair)
        seen.add(number)
    return [list(p) for p in pairs]

# VARIANT 1C: Sorted array two-pointer
def two_sum_sorted(numbers, target):
    """Variant C: sorted array → two-pointer for O(1) space"""
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

print("=== PROBLEM 1: TWO SUM ===")
print("BASE:", two_sum([2, 7, 11, 15], 9))
print("VARIANT 1A:", count_pairs_summing_to([1, 5, 7, -1, 5], 6))
print("VARIANT 1B:", all_pairs_summing_to([1, 0, -1, 0, -2, 2], 0))
print("VARIANT 1C:", two_sum_sorted([2, 7, 11, 15], 9))
print()


# ============================================================
# PROBLEM 2: THREE SUM
# ============================================================

# BASE: Find all unique triplets summing to 0
def three_sum(numbers):
    """Base: return all unique triplets summing to 0"""
    numbers.sort()
    result = []
    for i in range(len(numbers) - 2):
        if i > 0 and numbers[i] == numbers[i - 1]:
            continue
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

# VARIANT 2A: Four Sum
def four_sum(numbers, target):
    """Variant A: generalize to 4 numbers with custom target"""
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

# VARIANT 2B: Three Sum Closest
def three_sum_closest(numbers, target):
    """Variant B: find triplet CLOSEST to target, not exactly equal"""
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

print("=== PROBLEM 2: THREE SUM ===")
print("BASE:", three_sum([-1, 0, 1, 2, -1, -4]))
print("VARIANT 2A:", four_sum([1, 0, -1, 0, -2, 2], 0))
print("VARIANT 2B:", three_sum_closest([-1, 2, 1, -4], 1))
print()


# ============================================================
# PROBLEM 3: CONTAINS DUPLICATE
# ============================================================

# BASE: Any value appears twice?
def contains_duplicate(numbers):
    """Base: any duplicate?"""
    seen = set()
    for number in numbers:
        if number in seen:
            return True
        seen.add(number)
    return False

# VARIANT 3A: Duplicates within distance K
def contains_duplicate_within_distance_k(numbers, k):
    """Variant A: duplicates must be within distance k"""
    seen = set()
    for i, num in enumerate(numbers):
        if num in seen:
            return True
        seen.add(num)
        if len(seen) > k:
            seen.remove(numbers[i - k])
    return False

# VARIANT 3B: First duplicate value
def first_duplicate(numbers):
    """Variant B: return first duplicate value, not boolean"""
    seen = set()
    for number in numbers:
        if number in seen:
            return number
        seen.add(number)
    return None

# VARIANT 3C: All duplicate values
def all_duplicates(numbers):
    """Variant C: return all duplicate values"""
    seen = set()
    duplicates = set()
    for number in numbers:
        if number in seen:
            duplicates.add(number)
        seen.add(number)
    return list(duplicates)

print("=== PROBLEM 3: CONTAINS DUPLICATE ===")
print("BASE:", contains_duplicate([1, 2, 3, 2]))
print("VARIANT 3A:", contains_duplicate_within_distance_k([99, 99], 2))
print("VARIANT 3B:", first_duplicate([4, 1, 2, 1, 3]))
print("VARIANT 3C:", all_duplicates([4, 1, 2, 1, 3, 2]))
print()


# ============================================================
# PROBLEM 4: COUNT ALL (Frequency Map)
# ============================================================

# BASE: Build frequency dict for all values
def count_all(numbers):
    """Base: frequency map of all values"""
    counts = {}
    for number in numbers:
        counts[number] = counts.get(number, 0) + 1
    return counts

# VARIANT 4A: Count with minimum threshold
def count_at_least_k(numbers, k):
    """Variant A: only values appearing >= k times"""
    counts = count_all(numbers)
    return {v: c for v, c in counts.items() if c >= k}

# VARIANT 4B: Top K frequent elements
def top_k_frequent(numbers, k):
    """Variant B: return K most frequent values"""
    counts = count_all(numbers)
    import heapq
    return [v for v, _ in heapq.nlargest(k, counts.items(), key=lambda x: x[1])]

# VARIANT 4C: Group by frequency
def group_by_frequency(numbers):
    """Variant C: group values by their frequency"""
    counts = count_all(numbers)
    freq_map = {}
    for value, count in counts.items():
        if count not in freq_map:
            freq_map[count] = []
        freq_map[count].append(value)
    return freq_map

print("=== PROBLEM 4: COUNT ALL ===")
print("BASE:", count_all([1, 2, 2, 3, 2, 1]))
print("VARIANT 4A:", count_at_least_k([1, 1, 2, 2, 2, 3], 2))
print("VARIANT 4B:", top_k_frequent([1, 1, 1, 2, 2, 3], 2))
print("VARIANT 4C:", group_by_frequency([1, 1, 1, 2, 2, 3]))
print()


# ============================================================
# PROBLEM 5: GROUP ANAGRAMS
# ============================================================

# BASE: Group strings that are anagrams
def group_anagrams(strings):
    """Base: group strings that are anagrams"""
    groups = {}
    for s in strings:
        key = ''.join(sorted(s))
        if key not in groups:
            groups[key] = []
        groups[key].append(s)
    return list(groups.values())

# VARIANT 5A: Return only groups with size >= K
def group_anagrams_min_size(strings, k):
    """Variant A: return only groups with size >= k"""
    groups = {}
    for s in strings:
        key = ''.join(sorted(s))
        if key not in groups:
            groups[key] = []
        groups[key].append(s)
    return [g for g in groups.values() if len(g) >= k]

# VARIANT 5B: Find largest anagram group
def largest_anagram_group(strings):
    """Variant B: find largest anagram group"""
    groups = {}
    for s in strings:
        key = ''.join(sorted(s))
        if key not in groups:
            groups[key] = []
        groups[key].append(s)
    return max(groups.values(), key=len) if groups else []

# VARIANT 5C: Count total anagram groups
def count_anagram_groups(strings):
    """Variant C: count total anagram groups"""
    groups = {}
    for s in strings:
        key = ''.join(sorted(s))
        if key not in groups:
            groups[key] = 0
        groups[key] += 1
    return len(groups)

print("=== PROBLEM 5: GROUP ANAGRAMS ===")
print("BASE:", group_anagrams(['eat', 'tea', 'ate', 'tan', 'nat']))
print("VARIANT 5A:", group_anagrams_min_size(['eat', 'tea', 'ate', 'tan'], 2))
print("VARIANT 5B:", largest_anagram_group(['eat', 'tea', 'ate', 'tan', 'nat']))
print("VARIANT 5C:", count_anagram_groups(['eat', 'tea', 'ate', 'tan', 'nat']))
print()


# ============================================================
# PROBLEM 6: MOST/LEAST FREQUENT
# ============================================================

# BASE: Return value with highest count
def most_frequent(numbers):
    """Base: return value with highest count"""
    counts = count_all(numbers)
    return max(counts, key=counts.get)

# VARIANT 6A: Return all values at max frequency
def all_most_frequent(numbers):
    """Variant A: return all values at max frequency"""
    counts = count_all(numbers)
    max_count = max(counts.values())
    return [v for v, c in counts.items() if c == max_count]

# VARIANT 6B: Top K frequencies
def top_k_frequencies(numbers, k):
    """Variant B: return top K frequencies"""
    counts = count_all(numbers)
    import heapq
    return heapq.nlargest(k, set(counts.values()))

# VARIANT 6C: Values with exact frequency F
def values_with_frequency(numbers, f):
    """Variant C: return values with exact frequency f"""
    counts = count_all(numbers)
    return [v for v, c in counts.items() if c == f]

print("=== PROBLEM 6: MOST FREQUENT ===")
print("BASE:", most_frequent([1, 1, 1, 2, 2, 3]))
print("VARIANT 6A:", all_most_frequent([1, 1, 1, 2, 2, 3]))
print("VARIANT 6B:", top_k_frequencies([1, 1, 1, 2, 2, 3], 2))
print("VARIANT 6C:", values_with_frequency([1, 1, 1, 2, 2, 3], 2))
print()


# ============================================================
# PROBLEM 7: COMMON ELEMENTS (Intersection)
# ============================================================

# BASE: Find intersection of two lists
def common_elements(list1, list2):
    """Base: find intersection"""
    set2 = set(list2)
    return [x for x in list1 if x in set2]

# VARIANT 7A: Union
def union_elements(list1, list2):
    """Variant A: find union"""
    return list(set(list1) | set(list2))

# VARIANT 7B: Symmetric difference
def symmetric_difference(list1, list2):
    """Variant B: find symmetric difference"""
    set1, set2 = set(list1), set(list2)
    return list(set1 ^ set2)

# VARIANT 7C: Intersection with frequency
def common_elements_freq(list1, list2):
    """Variant C: intersection preserving frequency"""
    count1 = count_all(list1)
    count2 = count_all(list2)
    result = []
    for val in count1:
        if val in count2:
            result.extend([val] * min(count1[val], count2[val]))
    return result

print("=== PROBLEM 7: COMMON ELEMENTS ===")
print("BASE:", common_elements([1, 2, 3, 4], [3, 4, 5, 6]))
print("VARIANT 7A:", sorted(union_elements([1, 2, 3], [3, 4, 5])))
print("VARIANT 7B:", sorted(symmetric_difference([1, 2, 3], [3, 4, 5])))
print("VARIANT 7C:", sorted(common_elements_freq([1, 2, 2, 3], [2, 3, 3, 4])))
print()


# ============================================================
# PROBLEM 8: IS ANAGRAM
# ============================================================

# BASE: Check if two strings are anagrams
def is_anagram(s1, s2):
    """Base: check if two strings are anagrams"""
    return sorted(s1) == sorted(s2)

# VARIANT 8A: After removing K chars
def is_anagram_after_removing_k(s1, s2, k):
    """Variant A: anagrams after removing k chars"""
    if abs(len(s1) - len(s2)) > k:
        return False
    count1 = count_all(list(s1))
    count2 = count_all(list(s2))
    diff = 0
    for c in count1:
        if count1[c] > count2.get(c, 0):
            diff += count1[c] - count2.get(c, 0)
    for c in count2:
        if count2[c] > count1.get(c, 0):
            diff += count2[c] - count1.get(c, 0)
    return diff <= k

# VARIANT 8B: Minimum chars to remove
def min_chars_to_remove_for_anagram(s1, s2):
    """Variant B: minimum chars to remove to make anagrams"""
    count1 = count_all(list(s1))
    count2 = count_all(list(s2))
    total = len(s1) + len(s2)
    for c in set(count1.keys()) | set(count2.keys()):
        total -= 2 * min(count1.get(c, 0), count2.get(c, 0))
    return total

# VARIANT 8C: Anagrams by edits
def min_edits_for_anagram(s1, s2):
    """Variant C: minimum edits (insert/delete) to make anagrams"""
    count1 = count_all(list(s1))
    count2 = count_all(list(s2))
    edits = 0
    for c in set(count1.keys()) | set(count2.keys()):
        edits += abs(count1.get(c, 0) - count2.get(c, 0))
    return edits

print("=== PROBLEM 8: IS ANAGRAM ===")
print("BASE:", is_anagram('listen', 'silent'))
print("VARIANT 8A:", is_anagram_after_removing_k('abcd', 'bd', 2))
print("VARIANT 8B:", min_chars_to_remove_for_anagram('abcd', 'bd'))
print("VARIANT 8C:", min_edits_for_anagram('abcd', 'bd'))
print()

print("=" * 60)
print("CATEGORY 1: HASHMAP/DICT PATTERN MASTERY")
print("=" * 60)
print("Core: 'Check + Remember' — hashmap/set for O(1) lookups")
print("Variants: output format, constraints, data structures")
print("=" * 60)
