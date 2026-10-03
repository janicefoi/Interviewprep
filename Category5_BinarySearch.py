# ============================================================
# Category 5: Binary Search Problems
# Core pattern: O(log n) on sorted/nearly-sorted data
# ============================================================

# PROBLEM 1: Binary Search
# QUESTION: Find target's index in sorted array, return -1 if not found
# EXPLANATION: Split search space in half each iteration. Move left/right based on comparison.
# WHY: Eliminates half the remaining space per step → O(log n)
# TIME/SPACE: O(log n) time, O(1) space

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

print("binary_search([1, 3, 5, 7, 9, 11], 7):", binary_search([1, 3, 5, 7, 9, 11], 7))
print()

# PROBLEM 2: First Position Of Target
# QUESTION: Find LEFTMOST (first) index of target in sorted array (may have duplicates)
# EXPLANATION: When found, continue searching LEFT (hi = mid - 1) to find earlier occurrence.
# Record the found position and keep searching.
# TIME/SPACE: O(log n) time, O(1) space

def first_position_of(numbers, target):
    lo, hi = 0, len(numbers) - 1
    result = -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if numbers[mid] == target:
            result = mid
            hi = mid - 1
        elif numbers[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return result

print("first_position_of([5, 7, 7, 8, 8, 10], 8):", first_position_of([5, 7, 7, 8, 8, 10], 8))
print()

# PROBLEM 3: Search in Rotated Sorted Array
# QUESTION: Find target in rotated sorted array (sorted then shifted), O(log n)
# EXPLANATION: One half is always properly sorted. Check if target is in the sorted half.
# If yes, search there. If no, search the other half. Repeat.
# KEY: Determine which half is sorted by comparing ends.
# TIME/SPACE: O(log n) time, O(1) space

def search_rotated_sorted(numbers, target):
    lo, hi = 0, len(numbers) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if numbers[mid] == target:
            return mid
        if numbers[lo] <= numbers[mid]:
            if numbers[lo] <= target < numbers[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        else:
            if numbers[mid] < target <= numbers[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
    return -1

print("search_rotated_sorted([4, 5, 6, 7, 0, 1, 2], 0):", search_rotated_sorted([4, 5, 6, 7, 0, 1, 2], 0))
print()

# PROBLEM 4: Find Peak Element
# QUESTION: Find index of peak (element > neighbors). Array has at least one peak.
# EXPLANATION: Compare mid with right neighbor. If mid > right, peak is left or at mid.
# If mid <= right, peak is right. Shrink search space until finding peak.
# TIME/SPACE: O(log n) time, O(1) space

def find_peak(numbers):
    lo, hi = 0, len(numbers) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if numbers[mid] < numbers[mid + 1]:
            lo = mid + 1
        else:
            hi = mid
    return lo

print("find_peak([1, 2, 3, 1]):", find_peak([1, 2, 3, 1]))
print()

# PROBLEM 5: Sqrt(x) Integer
# QUESTION: Find integer square root of x (largest int whose square <= x)
# EXPLANATION: Binary search from 2 to x/2. When mid*mid == x, found. Else adjust bounds.
# At end, hi is the answer (largest value where mid² <= x).
# TIME/SPACE: O(log x) time, O(1) space

def sqrt_int(x):
    if x < 2:
        return x
    lo, hi = 2, x // 2
    while lo <= hi:
        mid = (lo + hi) // 2
        sq = mid * mid
        if sq == x:
            return mid
        elif sq < x:
            lo = mid + 1
        else:
            hi = mid - 1
    return hi

print("sqrt_int(8):", sqrt_int(8))
print()

# PROBLEM 6: Minimum in Rotated Sorted Array
# QUESTION: Find minimum in rotated sorted array, O(log n)
# EXPLANATION: Compare mid with right boundary. If mid > right, minimum is right.
# If mid <= right, minimum is at mid or left. Shrink accordingly.
# TIME/SPACE: O(log n) time, O(1) space

def min_rotated(numbers):
    lo, hi = 0, len(numbers) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if numbers[mid] > numbers[hi]:
            lo = mid + 1
        else:
            hi = mid
    return numbers[lo]

print("min_rotated([3, 4, 5, 1, 2]):", min_rotated([3, 4, 5, 1, 2]))
print()

# PROBLEM 7: Find Insert Position
# QUESTION: Find position where target should be inserted in sorted array to keep it sorted
# EXPLANATION: Standard binary search, but when target not found, lo points to insert position.
# TIME/SPACE: O(log n) time, O(1) space

def find_insert_position(numbers, target):
    lo, hi = 0, len(numbers)
    while lo < hi:
        mid = (lo + hi) // 2
        if numbers[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return lo

print("find_insert_position([1, 3, 5, 6], 5):", find_insert_position([1, 3, 5, 6], 5))
print()

# PROBLEM 8: Capacity to Ship Packages (Binary Search + Feasibility)
# QUESTION: Minimum capacity to ship all packages within D days (each day ship consecutive packages)
# EXPLANATION: Binary search on capacity (answer space, not input). For each capacity, check if feasible.
# Feasibility: can we ship all packages in D days with this capacity? Greedy check.
# WHY: Answer space is easier to binary search than input-based problems.
# TIME/SPACE: O(n log(sum)) time (n packages, log sum capacity values checked)

def capacity_to_ship_packages(weights, days):
    def can_ship(capacity):
        curr_day = 1
        curr_weight = 0
        for w in weights:
            if curr_weight + w > capacity:
                curr_day += 1
                curr_weight = w
            else:
                curr_weight += w
        return curr_day <= days
    
    lo, hi = max(weights), sum(weights)
    while lo < hi:
        mid = (lo + hi) // 2
        if can_ship(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo

print("capacity_to_ship_packages([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5):", capacity_to_ship_packages([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))
