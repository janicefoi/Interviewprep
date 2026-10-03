# ============================================================
# Category 3: Two Pointer Problems
# Core pattern: pointers from both ends, meet in the middle
# ============================================================

# PROBLEM 1: Valid Palindrome
# QUESTION: Check if string is palindrome (ignoring non-alphanumeric, case-insensitive)
# EXPLANATION: Two pointers from ends moving inward. When characters don't match, it's not a palindrome.
# WHY: O(n) time, O(1) space (no extra data structure needed)
# WHEN: Common warm-up, string validation problems
# TIME/SPACE: O(n) time, O(1) space

def is_palindrome(s):
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    left, right = 0, len(cleaned) - 1
    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    return True

print("is_palindrome('A man, a plan, a canal: Panama'):", is_palindrome('A man, a plan, a canal: Panama'))
print()


# PROBLEM 2: Container With Most Water
# QUESTION: Given heights array, find two lines that form container holding max water
# EXPLANATION: Water is bounded by the SHORTER of two lines and the distance between them.
# Start with max distance (both ends), then move the shorter pointer inward (only way to possibly improve).
# KEY INSIGHT: Moving the taller pointer won't help (still limited by shorter one and distance shrinks).
# TIME/SPACE: O(n) time, O(1) space

def max_area(heights):
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

print("max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]):", max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print()


# PROBLEM 3: 3Sum (Three Number Sum)
# QUESTION: Find all UNIQUE triplets that sum to 0 in array
# EXPLANATION: Sort array first, then for each number, use two-pointer on remaining array to find pair summing to -number.
# Dedup at every level to avoid duplicate triplets.
# GOTCHA: Must handle edge cases where same number appears multiple times.
# TIME/SPACE: O(n²) time (n for outer, n for two-pointer), O(1) space (if not counting sort)

def three_sum(numbers):
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

print("three_sum([-1, 0, 1, 2, -1, -4]):", three_sum([-1, 0, 1, 2, -1, -4]))
print()


# PROBLEM 4: Remove Duplicates From Sorted Array
# QUESTION: Remove duplicates IN PLACE. Sorted array, return length of array without duplicates.
# EXPLANATION: Two pointers: "write" tracks where unique elements go, "read" scans for new values.
# When a new value is found, write it to write position and advance write.
# CRITICAL: "in place" means you modify the array itself, return the length.
# TIME/SPACE: O(n) time, O(1) space

def remove_duplicates_sorted(numbers):
    if not numbers:
        return 0
    write = 0
    for read in range(1, len(numbers)):
        if numbers[read] != numbers[write]:
            write += 1
            numbers[write] = numbers[read]
    return write + 1

arr = [1, 1, 2, 2, 2, 3, 4, 4]
result_len = remove_duplicates_sorted(arr)
print("remove_duplicates_sorted([1, 1, 2, 2, 2, 3, 4, 4]): length =", result_len, ", array =", arr[:result_len])
print()


# PROBLEM 5: Is Sorted Rotated
# QUESTION: Check if array is sorted (ascending) AFTER some rotation
# E.g., [3,4,5,1,2] is sorted-then-rotated, but [2,1,3,4] is not
# EXPLANATION: A sorted-rotated array has EXACTLY ONE point where a larger number is followed by a smaller.
# Count these "breaks"; if 0 or 1, it's valid.
# TIME/SPACE: O(n) time, O(1) space

def is_sorted_rotated(numbers):
    count = 0
    n = len(numbers)
    for i in range(n):
        if numbers[i] > numbers[(i + 1) % n]:
            count += 1
    return count <= 1

print("is_sorted_rotated([3, 4, 5, 1, 2]):", is_sorted_rotated([3, 4, 5, 1, 2]))
print()


# PROBLEM 6: Two Sum in Sorted Array (Two-Pointer Variant)
# QUESTION: Given SORTED array and target, return indices of two numbers summing to target
# EXPLANATION: Two pointers from ends. Move towards middle based on whether sum is too small or too big.
# This is the SORTED variant of Category 1's two_sum (which used hashmap on unsorted).
# TIME/SPACE: O(n) time, O(1) space

def two_sum_sorted_array(numbers, target):
    left, right = 0, len(numbers) - 1
    while left < right:
        s = numbers[left] + numbers[right]
        if s == target:
            return [left + 1, right + 1]
        elif s < target:
            left += 1
        else:
            right -= 1
    return None

print("two_sum_sorted_array([2, 7, 11, 15], 9):", two_sum_sorted_array([2, 7, 11, 15], 9))
print()


# PROBLEM 7: Dutch Flag Sort (Partition Colors)
# QUESTION: Sort array of 0s, 1s, 2s IN PLACE (like color sorting)
# EXPLANATION: Three pointers: low, mid, high. Move mid through array:
#   - If 0, swap with low, advance both
#   - If 1, just advance mid
#   - If 2, swap with high, DON'T advance mid (swapped-in value is unexamined)
# CRITICAL: Don't advance mid after swapping with high (the swapped value needs checking).
# TIME/SPACE: O(n) time, O(1) space

def partition_colors(arr):
    low, mid, high = 0, 0, len(arr) - 1
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    return arr

print("partition_colors([2, 0, 2, 1, 1, 0]):", partition_colors([2, 0, 2, 1, 1, 0]))
print()


# PROBLEM 8: Trapping Rain Water
# QUESTION: Given elevation heights, calculate how much rain water is trapped
# E.g., [0,1,0,2,1,0,1,3,2,1,2,1] → water trapped between peaks
# EXPLANATION: For each position, water level = min(max_left, max_right) - height.
# Use two pointers tracking left_max and right_max from opposite ends.
# When left < right, left side controls the water level (since right_max is larger).
# TIME/SPACE: O(n) time, O(1) space

def trapping_rain_water(heights):
    if not heights:
        return 0
    left, right = 0, len(heights) - 1
    left_max, right_max = 0, 0
    total = 0
    while left < right:
        if heights[left] < heights[right]:
            if heights[left] >= left_max:
                left_max = heights[left]
            else:
                total += left_max - heights[left]
            left += 1
        else:
            if heights[right] >= right_max:
                right_max = heights[right]
            else:
                total += right_max - heights[right]
            right -= 1
    return total

print("trapping_rain_water([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]):", trapping_rain_water([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
