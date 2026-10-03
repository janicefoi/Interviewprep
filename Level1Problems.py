# O(n) time, O(1) space
def count_evens(numbers):
     count = 0
     for number in numbers:
          if number % 2 == 0:
               count += 1
     return count
print("count_evens:", count_evens([1, 2, 3, 4, 5]))

# O(n) time, O(1) space
def sum_evens(numbers):
     total = 0
     for number in numbers:
          if number % 2 == 0:
               total += number
     return total
print("sum_evens:", sum_evens([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))

# O(n) time, O(1) space
def find_average(numbers):
    if not numbers:
        return 0
    total = 0
    for number in numbers:
         total += number
    return total/len(numbers)

print("find_average:", find_average([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))

# O(n) time, O(1) space
def count_odds(numbers):
     count = 0
     for number in numbers:
          if number % 2 != 0:
               count += 1
     return count
print("count_odds:", count_odds([1, 2, 3, 4, 5]))

# O(n) time, O(1) space
def count_greater_than(numbers, target):
     count = 0
     for number in numbers:
          if number > target:
               count += 1
     return count
print("count_greater_than:", count_greater_than([1, 5, 3, 8, 2], 3))

# O(n) time, O(1) space
def count_negatives(numbers):
     count = 0
     for number in numbers:
          if number < 0:
               count += 1
     return count
print("count_negatives:", count_negatives([-2, 3, -5, 0, 7]))

# O(n) time, O(1) space
def count_zeros(numbers):
     count = 0
     for number in numbers:
          if number == 0:
               count +=1
     return count
print("count_zeros:", count_zeros([0, 1, 0, 2, 0]))

# O(n) time, O(1) space
def count_divisible_by(numbers, divisor):
     count = 0
     for number in numbers:
          if number % divisor == 0:
               count += 1
     return count
print("count_divisible_by:", count_divisible_by([3, 6, 9, 10, 12], 3))


# O(n) time, O(1) space
def sum_odds(numbers):
     total = 0
     for number in numbers:
          if number % 2 != 0:
               total += number
     return total
print("sum_odds:",sum_odds([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))

# O(n) time, O(1) space
def sum_positives(numbers):
     total = 0
     for number in numbers:
          if number > 0:
               total += number
     return total
print("sum_positives:",sum_positives([-3, 4, -1, 6, 2]))

# O(n) time, O(1) space
def sum_of_squares(numbers):
     total = 0
     for number in numbers:
          total += number ** 2
     return total
print("sum_of_squares:", sum_of_squares([1, 2, 3]))


# O(n) time, O(1) space
def find_largest_even(numbers):
     largest_even = None
     for number in numbers:
          if number % 2 == 0:
               if largest_even is None or number > largest_even:
                    largest_even = number
     return largest_even
print('find_largest_even:',find_largest_even([1, 3, 8, 4, 7, 10]))

# O(n) time, O(1) space
def find_smallest_even(numbers):
     smallest_even = None
     for number in numbers:
          if number % 2 == 0:
               if smallest_even is None or number < smallest_even:
                    smallest_even = number
     return smallest_even
print('find_smallest_even:',find_smallest_even([1, 3, 8, 4, 7, 10]))


# O(n) time, O(1) space
def find_second_largest(numbers):
    largest = second_largest = None
    for number in numbers:
        if largest is None or number > largest:
            second_largest = largest    # old largest demoted to second
            largest = number             # this number takes the top spot
        elif second_largest is None or number > second_largest:
            second_largest = number

    return second_largest

find_second_largest([3, 7, 2, 9, 4])
