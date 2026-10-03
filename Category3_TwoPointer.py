# ============================================================
# Category 3: Two Pointer — BASE PROBLEMS + EXHAUSTIVE VARIANTS
# Core pattern: Pointers from both ends moving inward
# Key: When to move which pointer (based on comparison)
# ============================================================

# ============================================================
# PROBLEM 1: CONTAINER WITH MOST WATER
# ============================================================
# What it solves: Find two lines that form container with max water
# Water = min(height[i], height[j]) * distance
# Key insight: Always move the SHORTER pointer (only way to improve)
# Interview angle: Min area? Count pairs? Closest to target?

# BASE: Max area container
def max_area(heights):
    """Base: find two lines forming container with max water"""
    left, right = 0, len(heights) - 1
    best = 0
    while left < right:
        area = min(heights[left], heights[right]) * (right - left)
        best = max(best, area)
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
    return best

# VARIANT 1A: Min area (inverse)
def min_area(heights):
    """Variant A: find min area"""
    left, right = 0, len(heights) - 1
    best = float('inf')
    while left < right:
        area = min(heights[left], heights[right]) * (right - left)
        best = min(best, area)
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
    return best

# VARIANT 1B: Count pairs with area >= K
def count_area_pairs(heights, k):
    """Variant B: count how many pairs form area >= k"""
    count = 0
    n = len(heights)
    for i in range(n):
        for j in range(i + 1, n):
            area = min(heights[i], heights[j]) * (j - i)
            if area >= k:
                count += 1
    return count

# VARIANT 1C: Find pair closest to target area
def find_closest_area(heights, target):
    """Variant C: find pair with area closest to target"""
    left, right = 0, len(heights) - 1
    best_area = 0
    best_diff = float('inf')
    while left < right:
        area = min(heights[left], heights[right]) * (right - left)
        diff = abs(area - target)
        if diff < best_diff:
            best_diff = diff
            best_area = area
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
    return best_area

print("=== PROBLEM 1: CONTAINER WITH MOST WATER ===")
print("BASE:", max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print("VARIANT 1A (min):", min_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print("VARIANT 1B (count >= 20):", count_area_pairs([1, 8, 6, 2, 5, 4, 8, 3, 7], 20))
print("VARIANT 1C (closest to 30):", find_closest_area([1, 8, 6, 2, 5, 4, 8, 3, 7], 30))
print()


# ============================================================
# PROBLEM 2: THREE SUM
# ============================================================
# What it solves: Find all unique triplets summing to target (usually 0)
# Strategy: Sort + two-pointer for each fixed element
# Key: Deduplicate at every level (skip duplicates)
# Interview angle: Custom target? Closest sum? Count instead?

# BASE: All triplets summing to 0
def three_sum(numbers):
    """Base: find all unique triplets summing to 0"""
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

# VARIANT 2A: Sum to custom target
def three_sum_target(numbers, target):
    """Variant A: sum to custom target (not 0)"""
    numbers.sort()
    result = []
    for i in range(len(numbers) - 2):
        if i > 0 and numbers[i] == numbers[i - 1]:
            continue
        sub_target = target - numbers[i]
        left, right = i + 1, len(numbers) - 1
        while left < right:
            s = numbers[left] + numbers[right]
            if s == sub_target:
                result.append([numbers[i], numbers[left], numbers[right]])
                while left < right and numbers[left] == numbers[left + 1]:
                    left += 1
                while left < right and numbers[right] == numbers[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif s < sub_target:
                left += 1
            else:
                right -= 1
    return result

# VARIANT 2B: Closest sum to target
def three_sum_closest(numbers, target):
    """Variant B: triplet with sum CLOSEST to target"""
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

# VARIANT 2C: Count triplets (not return them)
def count_triplets_summing_to(numbers, target):
    """Variant C: count triplets (not return them)"""
    numbers.sort()
    count = 0
    for i in range(len(numbers) - 2):
        if i > 0 and numbers[i] == numbers[i - 1]:
            continue
        left, right = i + 1, len(numbers) - 1
        while left < right:
            s = numbers[i] + numbers[left] + numbers[right]
            if s == target:
                count += 1
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
    return count

print("=== PROBLEM 2: THREE SUM ===")
print("BASE:", three_sum([-1, 0, 1, 2, -1, -4]))
print("VARIANT 2A (target=2):", three_sum_target([-1, 0, 1, 2, -1, -4], 2))
print("VARIANT 2B (closest to 1):", three_sum_closest([-1, 2, 1, -4], 1))
print("VARIANT 2C (count):", count_triplets_summing_to([-1, 0, 1, 2, -1, -4], 0))
print()


# ============================================================
# PROBLEM 3: REMOVE DUPLICATES (Sorted Array)
# ============================================================
# What it solves: Remove duplicates IN-PLACE from sorted array
# Strategy: Two pointers (write index, read index)
# Key: Write pointer tracks where to place next unique element
# Interview angle: Allow K duplicates? Return removed items?

# BASE: Remove all duplicates
def remove_duplicates_sorted(numbers):
    """Base: remove duplicates in-place, return new length"""
    if not numbers:
        return 0
    write = 0
    for read in range(1, len(numbers)):
        if numbers[read] != numbers[write]:
            write += 1
            numbers[write] = numbers[read]
    return write + 1

# VARIANT 3A: Allow at most K duplicates per value
def remove_duplicates_k(numbers, k):
    """Variant A: allow at most k duplicates per value"""
    if not numbers or k <= 0:
        return 0
    write = 0
    count = 1
    for read in range(1, len(numbers)):
        if numbers[read] != numbers[write]:
            write += 1
            numbers[write] = numbers[read]
            count = 1
        elif count < k:
            write += 1
            numbers[write] = numbers[read]
            count += 1
    return write + 1

# VARIANT 3B: Return deduplicated array (not length)
def deduplicate_array(numbers):
    """Variant B: return deduplicated array"""
    if not numbers:
        return []
    result = [numbers[0]]
    for i in range(1, len(numbers)):
        if numbers[i] != numbers[i - 1]:
            result.append(numbers[i])
    return result

# VARIANT 3C: Collect all duplicate values
def collect_duplicates(numbers):
    """Variant C: return all values that appear more than once"""
    seen = set()
    duplicates = set()
    for num in numbers:
        if num in seen:
            duplicates.add(num)
        seen.add(num)
    return sorted(list(duplicates))

print("=== PROBLEM 3: REMOVE DUPLICATES ===")
arr1 = [1, 1, 1, 2, 2, 3]
print("BASE:", remove_duplicates_sorted(arr1))
print("VARIANT 3B:", deduplicate_array([1, 1, 1, 2, 2, 3]))
print("VARIANT 3C:", collect_duplicates([1, 1, 1, 2, 2, 3]))
print()


# ============================================================
# PROBLEM 4: VALID PALINDROME
# ============================================================
# What it solves: Check if string is palindrome (ignore non-alphanumeric)
# Strategy: Two pointers from ends, skip non-alphanumeric
# Interview angle: Palindrome after removing K chars? Edit distance?

# BASE: Check palindrome (ignore non-alphanumeric)
def is_palindrome(s):
    """Base: check if palindrome (ignore non-alphanumeric, case-insensitive)"""
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    left, right = 0, len(cleaned) - 1
    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    return True

# VARIANT 4A: Palindrome after removing at most K chars
def is_palindrome_k_removes(s, k):
    """Variant A: palindrome after removing at most k chars"""
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    n = len(cleaned)
    def helper(l, r, removes):
        if l >= r:
            return True
        if cleaned[l] == cleaned[r]:
            return helper(l + 1, r - 1, removes)
        if removes > 0:
            return helper(l + 1, r, removes - 1) or helper(l, r - 1, removes - 1)
        return False
    return helper(0, n - 1, k)

# VARIANT 4B: Minimum chars to remove to make palindrome
def min_chars_remove_palindrome(s):
    """Variant B: minimum chars to remove to make palindrome"""
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    n = len(cleaned)
    def lcs_length(l, r):
        if l > r:
            return 0
        if l == r:
            return 1
        if cleaned[l] == cleaned[r]:
            return 2 + lcs_length(l + 1, r - 1)
        return max(lcs_length(l + 1, r), lcs_length(l, r - 1))
    return n - lcs_length(0, n - 1)

# VARIANT 4C: Check specific substring is palindrome
def substring_is_palindrome(s, start, end):
    """Variant C: check if substring [start, end] is palindrome"""
    while start < end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    return True

print("=== PROBLEM 4: VALID PALINDROME ===")
print("BASE:", is_palindrome('A man, a plan, a canal: Panama'))
print("VARIANT 4A (remove 1):", is_palindrome_k_removes('Aa', 1))
print("VARIANT 4B (min remove):", min_chars_remove_palindrome('abcdef'))
print()


# ============================================================
# PROBLEM 5: PARTITION ARRAY (DUTCH FLAG)
# ============================================================
# What it solves: Partition array into three groups (0s, 1s, 2s)
# Strategy: Three pointers (left=0s, middle=1s, right=2s)
# Key: Swap carefully, only advance when certain
# Interview angle: K colors? Minimize swaps?

# BASE: Partition into 0s, 1s, 2s
def partition_colors(numbers):
    """Base: partition into 0s, 1s, 2s (in-place)"""
    left, middle, right = 0, 0, len(numbers) - 1
    while middle <= right:
        if numbers[middle] == 0:
            numbers[left], numbers[middle] = numbers[middle], numbers[left]
            left += 1
            middle += 1
        elif numbers[middle] == 1:
            middle += 1
        else:
            numbers[middle], numbers[right] = numbers[right], numbers[middle]
            right -= 1

# VARIANT 5A: Partition into K colors
def partition_k_colors(numbers, k):
    """Variant A: partition into k colors"""
    for target in range(k):
        left = sum(1 for x in numbers if x < target)
        for i in range(len(numbers)):
            if numbers[i] == target:
                numbers[left], numbers[i] = numbers[i], numbers[left]
                left += 1
    return numbers

# VARIANT 5B: Minimize swaps to partition
def min_swaps_to_partition(numbers):
    """Variant B: minimum swaps needed"""
    swaps = 0
    left, middle, right = 0, 0, len(numbers) - 1
    while middle <= right:
        if numbers[middle] == 0:
            if numbers[left] != 0:
                numbers[left], numbers[middle] = numbers[middle], numbers[left]
                swaps += 1
            left += 1
            middle += 1
        elif numbers[middle] == 1:
            middle += 1
        else:
            if numbers[right] != 2:
                numbers[middle], numbers[right] = numbers[right], numbers[middle]
                swaps += 1
            right -= 1
    return swaps

# VARIANT 5C: Return counts (not sort in-place)
def count_colors(numbers):
    """Variant C: return count of each color"""
    return [sum(1 for x in numbers if x == i) for i in range(3)]

print("=== PROBLEM 5: PARTITION COLORS ===")
arr = [2, 0, 2, 1, 1, 0]
partition_colors(arr)
print("After partition:", arr)
print("Counts:", count_colors([2, 0, 2, 1, 1, 0]))
print()


# ============================================================
# PROBLEM 6: TRAPPING RAIN WATER
# ============================================================
# What it solves: Calculate volume of water trapped between elevations
# Strategy: Two pointers from ends, track left_max and right_max
# Key: Water at position = min(left_max, right_max) - height[i]
# Interview angle: 2D grid? With obstacles?

# BASE: Trap rain water
def trap_rain_water(heights):
    """Base: calculate trapped water volume"""
    if not heights:
        return 0
    left, right = 0, len(heights) - 1
    left_max, right_max = 0, 0
    water = 0
    while left < right:
        if heights[left] < heights[right]:
            if heights[left] >= left_max:
                left_max = heights[left]
            else:
                water += left_max - heights[left]
            left += 1
        else:
            if heights[right] >= right_max:
                right_max = heights[right]
            else:
                water += right_max - heights[right]
            right -= 1
    return water

# VARIANT 6A: 2D trap (rain water in 2D grid)
def trap_rain_water_2d(grid):
    """Variant A: trapped water in 2D grid"""
    if not grid or not grid[0]:
        return 0
    visited = set()
    import heapq
    pq = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if i == 0 or i == len(grid) - 1 or j == 0 or j == len(grid[0]) - 1:
                heapq.heappush(pq, (grid[i][j], i, j))
                visited.add((i, j))
    water = 0
    while pq:
        h, i, j = heapq.heappop(pq)
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and (ni, nj) not in visited:
                visited.add((ni, nj))
                water += max(0, h - grid[ni][nj])
                heapq.heappush(pq, (max(h, grid[ni][nj]), ni, nj))
    return water

# VARIANT 6B: Count water units (not volume)
def count_water_units(heights):
    """Variant B: count total water units (same as volume)"""
    return trap_rain_water(heights)

print("=== PROBLEM 6: TRAPPING RAIN WATER ===")
print("BASE:", trap_rain_water([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
print()

print("=" * 70)
print("CATEGORY 3: TWO POINTER PATTERN MASTERY")
print("=" * 70)
print("Pattern 1: Both ends converging (max area, closest sum)")
print("Pattern 2: Fixed element + two pointer (3sum)")
print("Pattern 3: Single pass with write pointer (remove duplicates)")
print("=" * 70)
