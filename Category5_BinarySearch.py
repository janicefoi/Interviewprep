# ============================================================
# Category 5: Binary Search — BASE PROBLEMS + EXHAUSTIVE VARIANTS
# Core pattern: O(log n) on sorted/answer space
# Key: Find the boundary where condition changes from false to true
# ============================================================

# ============================================================
# PROBLEM 1: BINARY SEARCH
# ============================================================
# What it solves: Find exact target in sorted array
# Why not linear: O(log n) vs O(n) — massive speedup on large data
# Core insight: Always eliminate half the remaining candidates
# Interview angle: What if target not in array? Return insertion point?

# BASE: Find exact target, return index or -1
def binary_search(nums, target):
    """Base: find target index, return -1 if not found"""
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

# VARIANT 1A: Find closest value (if exact not found)
def binary_search_closest(nums, target):
    """Variant A: find closest value to target (closest euclidean distance)"""
    if not nums:
        return -1
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    closest_idx = lo
    if lo > 0 and abs(nums[lo - 1] - target) < abs(nums[lo] - target):
        closest_idx = lo - 1
    return closest_idx

# VARIANT 1B: Count occurrences of target
def count_occurrences(nums, target):
    """Variant B: count how many times target appears"""
    def find_first(nums, target):
        lo, hi = 0, len(nums) - 1
        result = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                result = mid
                hi = mid - 1
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return result

    def find_last(nums, target):
        lo, hi = 0, len(nums) - 1
        result = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                result = mid
                lo = mid + 1
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return result

    first = find_first(nums, target)
    if first == -1:
        return 0
    last = find_last(nums, target)
    return last - first + 1

# VARIANT 1C: Find insertion position
def find_insert_position(nums, target):
    """Variant C: find position where target should be inserted to keep sorted"""
    lo, hi = 0, len(nums)
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return lo

# VARIANT 1D: Find first/last occurrence
def find_first_occurrence(nums, target):
    """Variant D: find FIRST (leftmost) occurrence of target"""
    lo, hi = 0, len(nums) - 1
    result = -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            result = mid
            hi = mid - 1  # Keep searching left
        elif nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return result

print("=== PROBLEM 1: BINARY SEARCH ===")
print("BASE:", binary_search([1, 3, 5, 7, 9], 7))
print("VARIANT 1A (closest):", binary_search_closest([1, 3, 5, 7, 9], 6))
print("VARIANT 1B (count):", count_occurrences([1, 2, 2, 2, 3, 4, 4], 2))
print("VARIANT 1C (insert pos):", find_insert_position([1, 3, 5, 7], 4))
print("VARIANT 1D (first):", find_first_occurrence([1, 2, 2, 2, 3, 4], 2))
print()


# ============================================================
# PROBLEM 2: SEARCH IN ROTATED SORTED ARRAY
# ============================================================
# What it solves: Find target in array that was sorted then rotated
# Example: [4, 5, 6, 7, 0, 1, 2] rotated from [0, 1, 2, 4, 5, 6, 7]
# Key insight: One half is always properly sorted
# Interview angle: What if duplicates allowed? Find rotation point?

# BASE: Find target in rotated sorted array
def search_rotated_sorted(nums, target):
    """Base: find target in rotated sorted array"""
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        # Determine which half is sorted
        if nums[lo] <= nums[mid]:  # Left half is sorted
            if nums[lo] <= target < nums[mid]:
                hi = mid - 1  # Target in sorted left half
            else:
                lo = mid + 1  # Target in right half
        else:  # Right half is sorted
            if nums[mid] < target <= nums[hi]:
                lo = mid + 1  # Target in sorted right half
            else:
                hi = mid - 1  # Target in left half
    return -1

# VARIANT 2A: Find minimum (rotation point)
def find_min_rotated(nums):
    """Variant A: find minimum element (rotation point)"""
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] > nums[hi]:
            lo = mid + 1
        else:
            hi = mid
    return nums[lo]

# VARIANT 2B: Find maximum
def find_max_rotated(nums):
    """Variant B: find maximum element"""
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] < nums[hi]:
            hi = mid
        else:
            lo = mid + 1
    return nums[lo]

# VARIANT 2C: Count occurrences (with duplicates allowed)
def count_occurrences_rotated(nums, target):
    """Variant C: count target in rotated array with duplicates"""
    lo, hi = 0, len(nums) - 1
    first_idx = -1
    last_idx = -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            if first_idx == -1:
                first_idx = mid
            last_idx = mid
            lo += 1
        elif nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return (last_idx - first_idx + 1) if first_idx != -1 else 0

print("=== PROBLEM 2: SEARCH ROTATED SORTED ===")
print("BASE:", search_rotated_sorted([4, 5, 6, 7, 0, 1, 2], 0))
print("VARIANT 2A (min):", find_min_rotated([3, 4, 5, 1, 2]))
print("VARIANT 2B (max):", find_max_rotated([3, 4, 5, 1, 2]))
print()


# ============================================================
# PROBLEM 3: FIND PEAK ELEMENT
# ============================================================
# What it solves: Find index of element > both neighbors
# Constraint: nums[i] != nums[i+1], so answer always exists
# Key: Compare with right neighbor, move toward larger side
# Interview angle: What if 2D grid? Return all peaks?

# BASE: Find peak (element > both neighbors)
def find_peak(nums):
    """Base: find peak (element > both neighbors)"""
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] < nums[mid + 1]:
            lo = mid + 1  # Peak to the right
        else:
            hi = mid  # Peak at mid or left
    return lo

# VARIANT 3A: Find all peaks
def find_all_peaks(nums):
    """Variant A: return indices of ALL peaks"""
    peaks = []
    for i in range(len(nums)):
        left_ok = (i == 0 or nums[i] > nums[i - 1])
        right_ok = (i == len(nums) - 1 or nums[i] > nums[i + 1])
        if left_ok and right_ok:
            peaks.append(i)
    return peaks

# VARIANT 3B: Find valley (element < both neighbors)
def find_valley(nums):
    """Variant B: find valley (inverse of peak)"""
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] > nums[mid + 1]:
            lo = mid + 1
        else:
            hi = mid
    return lo

# VARIANT 3C: Count peaks
def count_peaks(nums):
    """Variant C: count total peaks"""
    return len(find_all_peaks(nums))

print("=== PROBLEM 3: FIND PEAK ===")
print("BASE:", find_peak([1, 2, 3, 1]))
print("VARIANT 3A (all):", find_all_peaks([1, 3, 2, 4, 3, 5]))
print("VARIANT 3C (count):", count_peaks([1, 3, 2, 4, 3, 5]))
print()


# ============================================================
# PROBLEM 4: SQRT(X)
# ============================================================
# What it solves: Find integer square root (largest int where int²≤x)
# Example: sqrt(8) = 2 (since 2² = 4 ≤ 8, but 3² = 9 > 8)
# Binary search on answer space (not input space)
# Interview angle: K-th root? Closest perfect square?

# BASE: Integer square root
def sqrt_int(x):
    """Base: find integer square root"""
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

# VARIANT 4A: Cube root
def cbrt_int(x):
    """Variant A: integer cube root"""
    if x == 0:
        return 0
    lo, hi = 1, x
    while lo <= hi:
        mid = (lo + hi) // 2
        cb = mid * mid * mid
        if cb == x:
            return mid
        elif cb < x:
            lo = mid + 1
        else:
            hi = mid - 1
    return hi

# VARIANT 4B: K-th root
def kth_root(x, k):
    """Variant B: k-th root of x"""
    if x == 0:
        return 0
    lo, hi = 1, x
    while lo <= hi:
        mid = (lo + hi) // 2
        power = mid ** k
        if power == x:
            return mid
        elif power < x:
            lo = mid + 1
        else:
            hi = mid - 1
    return hi

# VARIANT 4C: Closest perfect square
def closest_perfect_square(x):
    """Variant C: find closest perfect square"""
    root = sqrt_int(x)
    if (root + 1) ** 2 - x < x - root ** 2:
        return (root + 1) ** 2
    return root ** 2

print("=== PROBLEM 4: SQRT(X) ===")
print("BASE:", sqrt_int(8))
print("VARIANT 4A (cube):", cbrt_int(27))
print("VARIANT 4B (k-root):", kth_root(32, 5))
print("VARIANT 4C (closest square):", closest_perfect_square(10))
print()


# ============================================================
# PROBLEM 5: CAPACITY TO SHIP (Binary Search on Answer Space)
# ============================================================
# What it solves: Minimum ship capacity to deliver all packages in D days
# Key: Search on answer space (capacity), not input space (weights)
# Strategy: For each candidate capacity, check if feasible (greedy check)
# Interview angle: Multiple ships? Different ship types?

# BASE: Minimum capacity to ship all packages in D days
def capacity_to_ship_packages(weights, days):
    """Base: min capacity to ship all in D days (consecutive packages per day)"""
    def can_ship(capacity):
        current_day = 1
        current_weight = 0
        for w in weights:
            if current_weight + w > capacity:
                current_day += 1
                current_weight = w
            else:
                current_weight += w
        return current_day <= days

    lo, hi = max(weights), sum(weights)
    while lo < hi:
        mid = (lo + hi) // 2
        if can_ship(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo

# VARIANT 5A: Maximum weight per package constraint
def min_capacity_max_weight_constraint(weights, days, max_per_package):
    """Variant A: min capacity with max weight per package limit"""
    # Similar logic but skip packages over max_per_package
    def can_ship(capacity):
        current_day = 1
        current_weight = 0
        for w in weights:
            if w > max_per_package:
                return False
            if current_weight + w > capacity:
                current_day += 1
                current_weight = w
            else:
                current_weight += w
        return current_day <= days

    lo, hi = max(weights), sum(weights)
    while lo < hi:
        mid = (lo + hi) // 2
        if can_ship(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo

# VARIANT 5B: Multiple ships (split optimally)
def min_capacity_multiple_ships(weights, num_ships):
    """Variant B: capacity if we can use multiple ships (distribute optimally)"""
    def can_ship(capacity):
        ships = 1
        current_weight = 0
        for w in weights:
            if current_weight + w > capacity:
                ships += 1
                current_weight = w
            else:
                current_weight += w
        return ships <= num_ships

    lo, hi = max(weights), sum(weights)
    while lo < hi:
        mid = (lo + hi) // 2
        if can_ship(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo

print("=== PROBLEM 5: CAPACITY TO SHIP ===")
print("BASE:", capacity_to_ship_packages([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))
print("VARIANT 5B (multi-ship):", min_capacity_multiple_ships([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3))
print()

print("=" * 70)
print("CATEGORY 5: BINARY SEARCH PATTERN MASTERY")
print("=" * 70)
print("Pattern 1: Search on input space (sorted array)")
print("Pattern 2: Search on answer space (capacity, threshold)")
print("Pattern 3: Find boundary where condition changes")
print("=" * 70)
