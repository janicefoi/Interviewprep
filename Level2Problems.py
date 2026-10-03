# O(n) time, O(n) space (output list)
def odds_only(numbers):
    result = []
    for number in numbers:
        if number % 2 != 0:
            result.append(number)
    return result
print("odds_only:", odds_only([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))

# O(n) time, O(n) space
def positives_only(numbers):
    result = []
    for number in numbers:
        if number > 0:
            result.append(number)
    return result
print( 'positives_only:',positives_only([-3, 4, -1, 6, 2]) )

# O(n) time, O(n) space
def filter_greater_than(numbers, target):
    result = []
    for number in numbers:
        if number > target:
            result.append(number)
    return result
print ('filter_greater_than:',filter_greater_than([1, 5, 3, 8, 2, 11], 7) )

# O(n) time, O(n) space
def remove_value(numbers, target):
    result = []
    for number in numbers:
        if number != target:
            result.append(number)
    return result
print ('remove_value:',remove_value([1, 2, 3, 2, 4, 2], 2))

# O(n) time, O(n) space
def square_all(numbers):
    result = []
    for number in numbers:
        result.append(number**2)
    return result
print('square_all:',square_all([1, 2, 3, 4]))

# O(n) time, O(n) space
def add_n(numbers, n):
    result = []
    for number in numbers:
        result.append(number+n)
    return result
print('add_n:',add_n([1, 2, 3], 10) )

# O(n) time, O(n) space
def to_uppercase(words):
    result = []
    for word in words:
        result.append(word.upper())
    return result
print('to_uppercase:',to_uppercase(["hello", "world"]) )

# O(n) time, O(n) space
def double_evens(numbers):
    result = []
    for number in numbers:
        if number % 2 == 0:
            result.append(number*2)
    return result
print('double_evens:',double_evens([1, 2, 3, 4, 5, 6]) )


# O(n) time, O(n) space
def squares_of_odds(numbers):
    result = []
    for number in numbers:
        if number %2 != 0:
            result.append(number**2)
    return result
print('squares_of_odds:',squares_of_odds([1, 2, 3, 4, 5]) )

# O(n) time, O(n) space
def list_lengths(words):
    result = []
    for word in words:
        result.append(len(word))
    return result
print('list_lengths:',list_lengths(["cat", "elephant", "dog"]) )

# O(n) time, O(n) space
def get_indices_of_evens(numbers):
    result = []
    for index, number in enumerate(numbers):
        if number % 2 == 0:
            result.append(index)
    return result
print('get_indices_of_evens:',get_indices_of_evens([1, 4, 3, 8]) )

# O(n^2) time, O(n) space -- NOT O(n)! .insert(0, x) has to shift every
# existing element over by one, and that happens n times, so it's n
# shifts of up to n items each. If asked for the O(n) version: walk the
# indices backwards with range(len(numbers)-1, -1, -1) and .append() instead.
def reverse_list_manually(numbers):
    result= []
    for number in numbers:
        result.insert(0, number)
    return result
print('reverse_list_manually:',reverse_list_manually([1, 2, 3, 4]) )
