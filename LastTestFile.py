"""Given a list of sales records, each one like
{'product': 'Widget', 'category': 'hardware', 'amount': 25},
can you write something that totals the sales amount for each category?"""

# O(n) time, O(k) space -- k = number of distinct categories
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
    {'product': 'Widget', 'category': 'hardware', 'amount': 25},
    {'product': 'Bolt', 'category': 'hardware', 'amount': 10},
    {'product': 'Mug', 'category': 'kitchen', 'amount': 15},
]))

"""Given a list of order records, each one like {'customer': 'c1', 'amount': 40},
can you write something that tells me which customer has spent the most
in total today?"""

# O(n) time, O(k) space -- k = number of distinct customers
def top_spending_customer(records):
    totals = {}
    for record in records:
        customer_id = record['customer']
        amount = record['amount']
        if customer_id not in totals:
            totals[customer_id] = 0
        totals[customer_id] += amount
    best_customer = None
    best_total = 0
    for customer_id, total in totals.items():
        if total > best_total:
            best_customer = customer_id
            best_total = total
    return best_customer

print('top_spending_customer:', top_spending_customer([
    {'customer': 'c1', 'amount': 40},
    {'customer': 'c2', 'amount': 15},
    {'customer': 'c1', 'amount': 30},
]))

# ============================================================
# TIER 3 -- Stack / Sliding window
# ============================================================

"""We're validating a batch of nested category codes before they go into
the system — things like '(A(B)C)'. Can you write something that checks
whether the parentheses in a code are properly balanced?"""

# O(n) time, O(n) space
def is_balanced(code):             # True only if every opener got closed
    stack = []
    for char in code:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()
    return not stack
print('is_balanced (expect True):', is_balanced('(A(B)C)'))
print('is_balanced (expect False):', is_balanced('(A(BC)'))

"""We're looking at a week of daily sales totals, and want to find the best
3-day stretch — the 3 consecutive days with the highest combined sales.
Can you write something that finds that?"""

# O(n) time, O(1) space
def best_3_day_stretch(daily_sales):
    window_sum = sum(daily_sales[:3])       # first 3-day window, computed once
    best = window_sum
    for i in range(3, len(daily_sales)):
        window_sum += daily_sales[i] - daily_sales[i - 3]   # add new day, drop oldest
        best = max(best, window_sum)
    return best

print('best_3_day_stretch:', best_3_day_stretch([100, 200, 150, 400, 250, 300, 100]))

"""We're cleaning up a status-code log where repeated ADJACENT codes should
cancel each other out — for example 'abbaca' should collapse down to 'ca'
(the two b's cancel, then the two a's next to each other cancel too).
Can you write something that removes adjacent matching pairs from a string?"""

# O(n) time, O(n) space
def remove_adjacent_duplicates(s):
    stack = []
    for char in s:
        if stack and stack[-1] == char:   # matches the top -> cancel it out
            stack.pop()
        else:
            stack.append(char)             # doesn't match -> push it on
    return "".join(stack)

print('remove_adjacent_duplicates:', remove_adjacent_duplicates('abbaca'))

# ============================================================
# TIER 4 -- Binary search / Recursion (lowest probability, but here for completeness)
# ============================================================

"""We've got a sorted list of invoice numbers, and want to check quickly
whether a specific invoice number exists in it. Can you write something
that finds its position, given the list is sorted?"""

# O(log n) time, O(1) space
def binary_search(invoice_numbers, target):
    lo, hi = 0, len(invoice_numbers) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if invoice_numbers[mid] == target:
            return mid
        elif invoice_numbers[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

print('binary_search:', binary_search([101, 103, 107, 109, 112, 118], 109))

"""Same sorted list, but this time invoice numbers can repeat. Can you write
something that finds the FIRST position where a specific invoice number
appears?"""

# O(log n) time, O(1) space
def first_position_of(invoice_numbers, target):
    lo, hi = 0, len(invoice_numbers) - 1
    result = -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if invoice_numbers[mid] == target:
            result = mid       # record this match...
            hi = mid - 1        # ...but keep searching LEFT for an earlier one
        elif invoice_numbers[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return result

print('first_position_of:', first_position_of([101, 103, 107, 107, 107, 112], 107))

"""Can you write a function that adds up all the numbers in a list, but
using recursion instead of a loop?"""

# O(n^2) time, O(n^2) space -- numbers[1:] copies the remaining list at
# every call (n + n-1 + ... + 0 total elements copied). A version passing
# an index instead of slicing would be true O(n) time, O(n) space.
def sum_list_recursive(numbers):
    if not numbers:
        return 0
    return numbers[0] + sum_list_recursive(numbers[1:])

print ('sum_list_recursive:', sum_list_recursive([2, 4, 6]) )




def is_palindrome_clean(s):
    cleaned =""
    for char in s.lower():
        if char != " ":
            cleaned += char
    left, right = 0, len(cleaned) - 1
    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right += 1
    return True



is_palindrome_clean("race car") 