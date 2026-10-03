# ============================================================
# ORDERED BY LIKELIHOOD, HIGHEST FIRST. Read top to bottom --
# stop wherever your remaining time runs out. Everything below
# has already been verified to run correctly.
# ============================================================


# ---- 1. HASHMAP / SET -- highest probability, proven (this is what was
#         actually asked in this exact interview process before) ----

# "Does anything from list A also show up in list B?"
# O(n + m) time, O(n) space
def is_sold_and_restocked(restocked, sold):
    seen = set(restocked)
    for item in sold:
        if item in seen:
            return True
    return False
print('is_sold_and_restocked (True):', is_sold_and_restocked(['A1','B2'], ['X9','B2']))
print('is_sold_and_restocked (False):', is_sold_and_restocked(['A1','B2'], ['X9','Y8']))

# "Which one shows up the most?"
# O(n) time, O(n) space
def most_frequent(items):
    counts = {}
    for item in items:
        if item not in counts:
            counts[item] = 0
        counts[item] += 1
    best_item, best_count = None, 0
    for item, count in counts.items():
        if count > best_count:
            best_item, best_count = item, count
    return best_item
print('most_frequent:', most_frequent(['c1','c2','c1','c3','c1','c2']))

# "Do any two numbers add up to a target?"
# O(n) time, O(n) space
def has_pair_summing_to(numbers, target):
    seen = set()
    for number in numbers:
        needed = target - number
        if needed in seen:
            return True
        seen.add(number)
    return False
print('has_pair_summing_to (True):', has_pair_summing_to([20,30,15], 50))
print('has_pair_summing_to (False):', has_pair_summing_to([10,12,8], 50))

# "Does anything repeat?"
# O(n) time, O(n) space
def has_duplicates(items):
    seen = set()
    for item in items:
        if item in seen:
            return True
        seen.add(item)
    return False
print('has_duplicates (True):', has_duplicates([1,2,3,2,5]))
print('has_duplicates (False):', has_duplicates([1,2,3,4,5]))

# "Do two words use exactly the same letters?"
# O(a + b) time, O(a + b) space
def is_anagram(word1, word2):
    def counts(word):
        c = {}
        for letter in word:
            if letter not in c:
                c[letter] = 0
            c[letter] += 1
        return c
    return counts(word1) == counts(word2)
print('is_anagram (True):', is_anagram('listen', 'silent'))
print('is_anagram (False):', is_anagram('listen', 'sailor'))


# ---- 2. DATA RECORDS -- moderate probability, matches the actual
#         take-home domain ----

# "Given records, total a field grouped by category"
# O(n) time, O(k) space
def total_by_category(records):
    totals = {}
    for record in records:
        category = record['category']
        amount = record['amount']
        if category not in totals:
            totals[category] = 0
        totals[category] += amount
    return totals
print('total_by_category:', total_by_category([
    {'category': 'hardware', 'amount': 25},
    {'category': 'hardware', 'amount': 10},
    {'category': 'kitchen', 'amount': 15},
]))


# ---- 3. STACK -- low-moderate, classic and fast to state ----

# "Are these brackets balanced?"
# O(n) time, O(n) space
def is_balanced(expression):
    pairs = {')': '(', ']': '[', '}': '{'}
    stack = []
    for char in expression:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack or stack.pop() != pairs[char]:
                return False
    return not stack
print('is_balanced (True):', is_balanced('({[]})'))
print('is_balanced (False):', is_balanced('({[)]}'))


# ---- 4. TWO-POINTER -- low-moderate, also fast to state ----

# "Is this a palindrome (ignoring case/spaces)?"
# O(n) time, O(n) space
def is_palindrome_clean(s):
    cleaned = ""
    for char in s.lower():
        if char != " ":
            cleaned += char
    left, right = 0, len(cleaned) - 1
    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    return True
print('is_palindrome_clean:', is_palindrome_clean("race car"))

# "Remove duplicates from an already-sorted list, in place"
# O(n) time, O(1) extra space
def remove_duplicates_sorted(numbers):
    if not numbers:
        return []
    write = 0
    for read in range(1, len(numbers)):
        if numbers[read] != numbers[write]:
            write += 1
            numbers[write] = numbers[read]
    return numbers[:write + 1]
print('remove_duplicates_sorted:', remove_duplicates_sorted([1,1,2,2,2,3,4,4]))

def remove_duplicates_sorted2(numbers):
    if not numbers:
        return []
    write = 0
    for read in range(1, len(numbers)):
        if numbers[read] != numbers[write]:
            write += 1
            numbers[write] = numbers[read]
    return numbers[:write+1]



# ---- 5. SLIDING WINDOW -- lower probability, needs more setup to state ----

# "Best sum of a fixed-size contiguous stretch"
# O(n) time, O(1) space
def max_sum_subarray(numbers, k):
    window_sum = sum(numbers[:k])
    best = window_sum
    for i in range(k, len(numbers)):
        window_sum += numbers[i] - numbers[i - k]
        best = max(best, window_sum)
    return best
print('max_sum_subarray:', max_sum_subarray([2,1,5,1,3,2], 3))


# ---- 6. BINARY SEARCH -- lower still, needs a sorted-list premise ----

# "Find a target's position in a sorted list"
# O(log n) time, O(1) space
def binary_search(numbers, target):
    lo, hi = 0, len(numbers) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if numbers[mid] == target:
            return mid
        elif numbers[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
print('binary_search:', binary_search([1,3,5,7,9,11], 7))


# ---- 7. RECURSION -- lowest probability, hardest to state/solve live
#         in a short slot ----

# "Solve this using recursion instead of a loop"
# O(n) time, O(n) space (call stack)
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)
print('factorial:', factorial(5))
