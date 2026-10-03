# O(n) time, O(1) space
def sum_list(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

# O(n) time, O(1) space
def find_max(numbers):
    if not numbers:
        return None
    max_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number

# O(n) time, O(1) space
def find_min(numbers):
    if not numbers:
        return None
    min_number = numbers[0]
    for number in numbers:
        if number < min_number:
            min_number = number
    return min_number

# O(n) time, O(1) space
def count_occurrences(numbers, target):
    count = 0
    for number in numbers:
        if number == target:
            count += 1
    return count

# O(n) time, O(n) space -- word[::-1] builds a brand-new reversed string
def is_palindrome(word):
    reversed_word = word[::-1]
    return word == reversed_word

# O(1) time, O(1) space -- len() on a list is instant, not a scan
def count_numbers(numbers):
    return len(numbers)

