# ============================================================
# Category 2: Sliding Window Problems
# Core pattern: maintain a window, expand/shrink as needed
# ============================================================


# ---- PROBLEM 1: Max Sum Subarray (Fixed Window) ----
# QUESTION:
#   Given a list of numbers and a window size k, find the maximum sum
#   of any k consecutive numbers.
#   E.g., [2, 1, 5, 1, 3, 2] with k=3 → max is [5, 1, 3] = 9
#
# EXPLANATION:
#   Brute force: compute the sum for every possible k-length window (O(n*k)).
#   Sliding window trick: compute the first window's sum, then slide by
#   removing the leftmost element and adding the new rightmost element.
#   This amortizes to O(n) total.
#   PATTERN: "window_sum += arr[right] - arr[left]" is the core move.
#
# WHEN YOU'D SEE THIS:
#   - Very common in Datadog (monitoring over time windows)
#   - Variants: max product subarray, minimum window
#   - Often Question 2 material
#
# TIME/SPACE: O(n) time, O(1) space
def max_sum_subarray(numbers, k):
    window_sum = sum(numbers[:k])
    best = window_sum
    for i in range(k, len(numbers)):
        window_sum += numbers[i] - numbers[i - k]
        best = max(best, window_sum)
    return best

print("max_sum_subarray([2, 1, 5, 1, 3, 2], 3):", max_sum_subarray([2, 1, 5, 1, 3, 2], 3))
print()


# ---- PROBLEM 2: Best Time to Buy and Sell Stock ----
# QUESTION:
#   Given daily stock prices, find the maximum profit from buying on one day
#   and selling on a LATER day. Return 0 if no profit is possible.
#   E.g., [7, 1, 5, 3, 6, 4] → buy at 1, sell at 6, profit = 5
#
# EXPLANATION:
#   Don't think "window of fixed size". Instead: as you scan through prices,
#   track the MINIMUM price seen so far (best buying opportunity up to now).
#   For each current price, the profit is (current - min_so_far).
#   Keep track of the best profit encountered.
#   This is a "best-so-far" pattern, related to sliding window thinking.
#   KEY: You can't sell before you buy (left pointer must be left of right pointer).
#
# WHEN YOU'D SEE THIS:
#   - Very common warm-up
#   - Variants: buy and sell multiple times, with cooldown/fee
#   - Tests one-pass thinking
#
# TIME/SPACE: O(n) time, O(1) space
def max_profit(prices):
    if not prices:
        return 0
    min_price = prices[0]
    best_profit = 0
    for price in prices[1:]:
        profit = price - min_price
        best_profit = max(best_profit, profit)
        min_price = min(min_price, price)
    return best_profit

print("max_profit([7, 1, 5, 3, 6, 4]):", max_profit([7, 1, 5, 3, 6, 4]))
print()


# ---- PROBLEM 3: Longest Substring Without Repeating Characters ----
# QUESTION:
#   Given a string, find the LENGTH of the longest substring with NO repeated
#   characters. E.g., "abcabcbb" → "abc" has length 3
#
# EXPLANATION:
#   This is a VARIABLE window problem. You want the window to be as long as
#   possible while maintaining the constraint (no duplicates).
#   ALGORITHM:
#     - Expand right pointer to include a new character
#     - If it creates a duplicate, shrink left pointer until the duplicate is gone
#     - Track the maximum window size seen
#   Use a dict to store the last-seen index of each character for quick checking.
#   This is THE canonical variable window problem.
#
# WHEN YOU'D SEE THIS:
#   - Very common medium problem
#   - Variant: "at most k distinct characters" (same pattern, change the constraint)
#   - Tests understanding of variable window vs fixed window
#
# TIME/SPACE: O(n) time, O(min(n, alphabet_size)) space
def length_of_longest_substring(s):
    last_seen = {}
    left = best = 0
    for right, char in enumerate(s):
        if char in last_seen and last_seen[char] >= left:
            left = last_seen[char] + 1  # move left past the duplicate
        last_seen[char] = right
        best = max(best, right - left + 1)
    return best

print("length_of_longest_substring('abcabcbb'):", length_of_longest_substring('abcabcbb'))
print()


# ---- PROBLEM 4: Longest Substring with At Most K Distinct Characters ----
# QUESTION:
#   Given a string and an integer k, find the length of the longest substring
#   that contains AT MOST k distinct characters.
#   E.g., "eceba" with k=2 → "ece" has length 3 (e and c only)
#
# EXPLANATION:
#   Same sliding window idea as Problem 3, but the constraint changes:
#   Instead of "no repeats", it's "at most k distinct".
#   ALGORITHM:
#     - Expand right to include a new character
#     - Count how many distinct characters are in the window
#     - If count > k, shrink left until count == k
#     - Track maximum window size
#   Use a dict to count character frequencies, delete when count hits 0.
#   This is the direct generalization of Problem 3.
#
# WHEN YOU'D SEE THIS:
#   - Medium-difficulty sliding window problem
#   - Similar to Problem 3 but with a different constraint
#   - Tests "how do I adapt this pattern to a new problem?"
#
# TIME/SPACE: O(n) time, O(k) space
def longest_substring_k_distinct(s, k):
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

print("longest_substring_k_distinct('eceba', 2):", longest_substring_k_distinct('eceba', 2))
print()


# ---- PROBLEM 5: Shortest Error Burst (At-Least-Threshold) ----
# QUESTION:
#   Given a list of error counts per minute and a threshold, find the
#   LENGTH of the SHORTEST contiguous window whose sum is AT LEAST the threshold.
#   Return 0 if no window meets the threshold.
#   E.g., [2, 3, 1, 2, 4, 3] with threshold=7 → [4, 3] sums to 7, length 2
#
# EXPLANATION:
#   This is the "opposite" constraint from max_sum_subarray:
#   Instead of "find max within fixed k", it's "find min size where sum >= threshold".
#   ALGORITHM:
#     - Expand right to grow the window sum
#     - When sum >= threshold, shrink left to find the minimal window
#     - Track the minimum window size that ever met the constraint
#   KEY INSIGHT: The while loop shrinks aggressively. Once a window is valid,
#   we want to shrink it as much as possible to find the TRUE minimum.
#
# WHEN YOU'D SEE THIS:
#   - Medium sliding window problem (Datadog Question 2 from MockTest)
#   - Tests understanding of when to shrink vs expand
#   - "At least" threshold is common in real systems (SLA requirements)
#
# TIME/SPACE: O(n) time, O(1) space
def shortest_burst(errors, threshold):
    left = total = 0
    best = len(errors) + 1
    for right in range(len(errors)):
        total += errors[right]
        while total >= threshold:
            best = min(best, right - left + 1)
            total -= errors[left]
            left += 1
    return 0 if best == len(errors) + 1 else best

print("shortest_burst([2, 3, 1, 2, 4, 3], 7):", shortest_burst([2, 3, 1, 2, 4, 3], 7))
print()


# ---- PROBLEM 6: Min Window Substring (Sliding Window + Hashmap) ----
# QUESTION:
#   Given two strings s and t, find the SHORTEST contiguous substring of s
#   that contains all characters in t with the correct frequencies.
#   E.g., s="ADOBECODEBANC", t="ABC" → "BANC" (length 4)
#
# EXPLANATION:
#   This combines sliding window with hashmap (Category 1).
#   ALGORITHM:
#     1. Build a frequency map of t (what we NEED)
#     2. Use two pointers on s; expand right to collect characters
#     3. Track how many characters we still NEED; when it hits 0, we have a valid window
#     4. Shrink left to minimize the window size
#     5. Record the best (shortest) window found
#   GOTCHA: You must check actual substring equality after window shrinking,
#   because different substrings can have the same hash.
#
# WHEN YOU'D SEE THIS:
#   - Hard sliding window problem (combines two techniques)
#   - Real-world analog: "find the smallest service log that contains all required events"
#   - Tests combination skills
#
# TIME/SPACE: O(n + m) time, O(alphabet_size) space
def min_window_substring(s, t):
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

print("min_window_substring('ADOBECODEBANC', 'ABC'):", min_window_substring('ADOBECODEBANC', 'ABC'))
print()


# ---- PROBLEM 7: Longest Repeating Character Replacement ----
# QUESTION:
#   Given a string and an integer k, find the length of the longest substring
#   where you can replace AT MOST k characters to make all characters the same.
#   E.g., "ABAB" with k=2 → replace both B's with A, result is "AAAA", length 4
#
# EXPLANATION:
#   Use sliding window. At each step:
#     - Expand right to include a new character
#     - Count frequencies of characters in the window
#     - If (window_length - max_frequency) > k, we have too many "odd" characters
#       to fix with k replacements, so shrink left
#     - Track maximum valid window size
#   The key insight: (window_length - max_frequency) tells you how many characters
#   you'd need to replace to make everything match the most frequent character.
#
# WHEN YOU'D SEE THIS:
#   - Medium-hard sliding window problem
#   - Tests creative constraint interpretation
#   - Real analog: "can we fix this data stream with k corrections?"
#
# TIME/SPACE: O(n) time, O(1) space (alphabet is bounded)
def longest_repeating_char(s, k):
    counts = {}
    left = best = 0
    for right, c in enumerate(s):
        counts[c] = counts.get(c, 0) + 1
        while right - left + 1 - max(counts.values()) > k:
            counts[s[left]] -= 1
            left += 1
        best = max(best, right - left + 1)
    return best

print("longest_repeating_char('ABAB', 2):", longest_repeating_char('ABAB', 2))
print()


# ---- PROBLEM 8: Valid Palindrome Substring (Simplified) ----
# QUESTION:
#   Given a string and a length k, check if ANY substring of length k
#   is a palindrome. Return True if found, False otherwise.
#   E.g., "abaca" with k=3 → "aba" at index 0 is a palindrome
#
# EXPLANATION:
#   This is a simpler use of sliding window: just slide a fixed-size window
#   and check each one for the palindrome property. Not the most efficient
#   (expand-around-center in Category 3 is better), but tests sliding window pattern.
#   KEY: This is a fixed-window (size k) problem, not variable.
#
# WHEN YOU'D SEE THIS:
#   - Rare standalone; usually a sub-step in a larger problem
#   - Tests "can you slide a window and check a property?"
#
# TIME/SPACE: O(n * k) time, O(1) space
def is_valid_palindrome_substring(s, k):
    for i in range(len(s) - k + 1):
        if s[i:i+k] == s[i:i+k][::-1]:
            return True
    return False

print("is_valid_palindrome_substring('abaca', 3):", is_valid_palindrome_substring('abaca', 3))
