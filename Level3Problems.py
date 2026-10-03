# ---- Group A: "Have I seen this?" ----

# O(n) time, O(n) space
def has_duplicates(numbers):
    seen = set()
    for number in numbers:
        if number in seen:
            return True
        seen.add(number)
    return False
print('has_duplicates:', has_duplicates([1, 2, 3, 2, 5]) )

# O(n) time, O(n) space
def first_duplicate(numbers):
    seen = set()
    for number in numbers:
        if number in seen:
            return number
        seen.add(number)
    return None
print('first_duplicate:', first_duplicate([4, 1, 2, 1, 3]))

# O(n) time, O(n) space
def remove_duplicates(numbers):
    seen = set()
    result = []
    for number in numbers:
        if number not in seen:
            result.append(number)
            seen.add(number)
    return result  
print('remove_duplicates:', remove_duplicates([1, 2, 2, 3, 1, 4]))


# ---- Group B: "Does a match exist elsewhere?" ----

# O(n + m) time, O(n + m) space
def common_elements(list1, list2):
    seen = set(list1)
    result = []
    for number in list2:
        if number in seen:
            result.append(number)
    return result
print('common_elements:', common_elements([1,2,3,4,5], [3,4,5,6,7]))

# O(n + m) time, O(n + m) space
def unique_to_first(list1, list2):
    seen = set(list2)
    result = []
    for number in list1:
        if number not in seen:
            result.append(number)
    return result
print('unique_to_first:', unique_to_first([1,2,3,4,5], [3,4,5,6,7]))


# ---- Group C: Dict for counting ----

# O(n) time, O(k) space -- k = number of distinct values, bounded by n
def count_all(numbers):
    counts = {}
    for number in numbers:
        if number not in counts:
            counts[number] = 0
        counts[number] += 1
    return counts

print('count_all:', count_all([1, 2, 2, 3, 2, 1]))

# O(n) time, O(n) space
def most_frequent(numbers):
    counts = count_all(numbers)
    best_value = None
    best_count = 0
    for value, count in counts.items():
        if count > best_count:
            best_value = value
            best_count = count
    return best_value
print('most_frequent:', most_frequent([1, 2, 2, 3, 2, 1]))


# ---- Group D: Two Sum, slow vs. fast ----

# O(n^2) time, O(1) extra space -- checks every pair directly, no hashmap
def two_sum_slow(numbers, target):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return [numbers[i], numbers[j]]
    return None
print('two_sum_slow:', two_sum_slow([2, 7, 11, 15], 9))

# O(n) time, O(n) space
def two_sum(numbers, target):
    seen = {}
    for number in numbers:
        needed = target - number
        if needed in seen:
            return[needed, number]
        seen[number] = True
    return None    
print('two_sum:' , two_sum([2, 7, 11, 15], 9))


# ---- Group E: "Have I seen this," flipped and counted ----

# O(n) time, O(n) space
def all_unique(numbers):
    seen = set()
    for number in numbers:
        if number in seen:
            return False
        seen.add(number)
    return True
print('all_unique:', all_unique([1, 2, 2, 4]))

# O(n) time, O(n) space
def count_unique(numbers):
    return len(set(numbers))
print('count_unique:', count_unique([1, 2, 2, 3, 3, 3, 4]))


# ---- Group F: Extending Two Sum ----

# O(n) time, O(n) space
def has_pair_with_difference(numbers, diff):
    seen = set()
    for number in numbers:
        if number + diff in seen or number - diff in seen:
            return True
        seen.add(number)
    return False
print('has_pair_with_difference', has_pair_with_difference([1, 5, 3, 9], 4))

# O(n) time, O(n) space
def find_all_pairs_summing_to(numbers, target):
    seen = set()
    pairs = []
    for number in numbers:
        needed = target - number
        if needed in seen:
            pairs.append((needed, number))
        seen.add(number)
    return pairs
print('find_all_pairs_summing_to:', find_all_pairs_summing_to([2, 4, 3, 5, 7, 8], 9))


# ---- Group G: A dict whose values are lists ----

# O(n) time, O(n) space
def group_by_first_letter(words):
    groups = {}
    for word in words:
        letter = word[0]
        if letter not in groups:
            groups[letter] = []
        groups[letter].append(word)
    return groups
print('group_by_first_letter', group_by_first_letter(["cat", "car", "dog", "duck", "bee"]))

# O(a + b) time, O(a + b) space -- a, b = lengths of the two words (calls count_all twice)
def is_anagram(word1, word2):
    return count_all(word1) == count_all(word2)
print('is_anagram:', is_anagram("listen", "silent"))


# ---- Group H: String versions of Group A ----

# O(n) time, O(n) space
def has_all_unique_characters(word):
    seen = set()
    for letter in word:
        if letter in seen:
            return False
        seen.add(letter)
    return False
print('has_all_unique_characters:', has_all_unique_characters("hello"))

# O(n) time, O(n) space
def first_repeated_char(word):
    seen = set()
    for letter in word:
        if letter in seen:
            return letter
        seen.add(letter)
    return None
print('first_repeated_char:' , first_repeated_char("swiss"))


# ---- Group I: Set operations as a tool ----

# O(n) time, O(n) space
def find_missing_number(numbers, n):
    full_set = set(range(1, n+1))
    seen = set(numbers)
    missing = full_set - seen
    return missing.pop()
print('find_missing_number:', find_missing_number([1, 2, 4, 5], 5) )

# O(n + m) time, O(n + m) space
def symmetric_difference(list1, list2):
    seen1 = set(list1)
    seen2 = set(list2)
    only_in_1 = seen1 - seen2
    only_in_2 = seen2 - seen1
    return list(only_in_1) + list(only_in_2)
print('symmetric_difference:', symmetric_difference([1,2,3,4,5,6,7,8,9,10], [7,8,9,10,11,12,13,14,15,16]))


# ---- Group J: More extensions ----

# O(n) time, O(n) space
def least_frequent(numbers):
    counts = count_all(numbers)
    best_value = None
    best_count = None
    for value, count in counts.items():
         if best_count is None or count < best_count:
            best_value = value
            best_count = count
    return best_value
print('least_frequent:', least_frequent([1, 1, 2, 3, 3, 3]))

# O(n + m) time, O(n) space
def has_common_element(list1, list2):
    seen = set(list1)
    for number in list2:
        if number in seen:
            return True
        seen.add(number)
    return False
print('has_common_element:', has_common_element([1, 2, 3], [5, 6, 3]))

# O(n) time, O(n) space
def count_pairs_with_sum(numbers, target):
    seen = set()
    pairs = []
    for number in numbers:
        needed = target - number
        if needed in seen:
            pairs.append((needed, number))
        seen.add(number)
    return len(pairs)
print('count_pairs_with_sum:', count_pairs_with_sum([1, 5, 3, 4, 2], 6))

# O(n) time, O(n) space
def two_sum_indices(numbers, target):
    seen = {}
    for index ,number in enumerate(numbers):
        needed = target - number
        if needed in seen:
            return [seen[needed], index]
        seen[number] = index
    return None
print('two_sum_indices:', two_sum_indices([2, 7, 11, 15], 9))


# ---- Group K: Free reuse (no new code needed) ----

# O(n) time, O(n) space
def most_common_word(words):
    return most_frequent(words)
print('most_common_word:', most_common_word(["a", "b", "a", "c", "a"]))

# O(n) time, O(n) space
def group_by_length(words):
    groups = {}
    for word in words:
        length = len(word)
        if length not in groups:
            groups[length] = []
        groups[length].append(word)
    return groups
print('group_by_length:', group_by_length(["cat", "dog", "bee", "duck"]))
