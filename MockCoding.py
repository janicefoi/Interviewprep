# ============================================================
# TIER 1 -- Hashmap / Set reasoning (highest probability)
# ============================================================

"""Say you've got a list of product SKUs that got restocked today,
and a separate list of SKUs that sold today.
Can you write something that tells me whether any product was both
restocked and sold on the same day?"""

# O(n + m) time, O(n) space
def is_sold_and_restocked(list1, list2):
    restocked = list1
    sold = list2
    seen = set(restocked)
    for number in sold:
        if number in seen:
            return True
    return False

print('is_sold_and_restocked (expect True):', is_sold_and_restocked(['A1', 'B2', 'C3'], ['X9', 'B2', 'Z5']))
print('is_sold_and_restocked (expect False):', is_sold_and_restocked(['A1', 'B2', 'C3'], ['X9', 'Y8', 'Z5']))

""""We've got a list of customer IDs — one entry for every order placed today.
 The same customer might show up more than once if they ordered multiple times.
 Can you tell me which customer placed the most orders today?"""

# O(n) time, O(n) space
def most_frequent_customer(numbers):
    customer_ids = numbers
    counts = {}
    for customer_id in customer_ids:
        if customer_id not in counts:
            counts[customer_id] = 0
        counts[customer_id] += 1

    best_customer = None
    best_count = 0
    for customer_id, count in counts.items():
        if count > best_count:
            best_customer = customer_id
            best_count = count
    return best_customer

print('most_frequent_customer:', most_frequent_customer(['c1', 'c2', 'c1', 'c3', 'c1', 'c2']))

""""We're running a promotion: if any two items in someone's cart add up to exactly $50,
 they get a discount applied automatically. Given a list of item prices in a cart,
   can you tell me whether such a pair exists?"""

# O(n) time, O(n) space
def apply_promotion(numbers, target):
    costs = numbers
    seen = set()
    for cost in costs:
        needed = target - cost
        if needed in seen:
            return True
        seen.add(cost)
    return False

print('apply_promotion (expect True):', apply_promotion([20, 30, 15], 50))
print('apply_promotion (expect False):', apply_promotion([10, 12, 8], 50))

"""""We just sent out a batch of order confirmation emails —
it's a list of order IDs we confirmed today.
 Can you write something that tells me if we accidentally sent a
 confirmation to the same order twice?"""

# O(n) time, O(n) space
def check_confirmation_email(numbers):
    order_ids = numbers
    seen = set()
    for order_id in order_ids:
        if order_id in seen:
            return True
        seen.add(order_id)
    return False
print('Has email been sent twice (expect True):', check_confirmation_email([1, 2, 3, 2, 5]))
print('Has email been sent twice (expect False):', check_confirmation_email([1, 2, 3, 4, 5, 8, 6, 7]))

""""Say you've got a list of support tickets, each one is a pair
like (101, 'billing') — a ticket ID and a category.
Can you write something that groups all the ticket IDs together by category?"""

# O(n) time, O(n) space
def group_tickets_by_category(tickets):
    groups = {}
    for ticket_id, category in tickets:
        if category not in groups:
            groups[category] = []
        groups[category].append(ticket_id)
    return groups

group_tickets_by_category([(101, 'billing'), (102, 'technical'), (103, 'billing'), (104, 'account')])

"""One of our data entry folks flagged that two product names might actually
be the same product, just entered with the letters rearranged by mistake —
like 'listen' and 'silent'. Can you write something that checks whether
two names use exactly the same letters?"""

# O(a + b) time, O(a + b) space -- a, b = lengths of the two names
def is_same_letters(name1, name2):
    counts1 = {}
    for letter in name1:
        if letter not in counts1:
            counts1[letter] = 0
        counts1[letter] += 1

    counts2 = {}
    for letter in name2:
        if letter not in counts2:
            counts2[letter] = 0
        counts2[letter] += 1

    return counts1 == counts2

print('is_same_letters (expect True):', is_same_letters('listen', 'silent'))
print('is_same_letters (expect False):', is_same_letters('listen', 'sailor'))

"""We expected order IDs 1 through n to all come through today, but it
looks like exactly one didn't get processed. Given the list of order IDs
that WERE processed, can you find the one that's missing?"""

# O(n) time, O(n) space
def find_missing_n(numbers, n):
    full_set = set(range(1, n+1))
    seen= set(numbers)
    missing = full_set - seen
    return missing.pop()
print('find_missing_number:', find_missing_n([1, 2, 4, 5], 5) )


"""We're comparing this month's active customer list to last month's.
Can you write something that returns the customers who were active in
exactly one of the two months, not both?"""

# O(n + m) time, O(n + m) space
def active_customers(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    only_in_1 = set1 - set2      # active in month 1, NOT month 2
    only_in_2 = set2 - set1      # active in month 2, NOT month 1
    return list(only_in_1) + list(only_in_2)
print ('active customers:', active_customers([1,2,3,4,5], [4,5,6,7,]))


"""Same $50 cart promotion as before, but now finance wants to know exactly
HOW MANY qualifying pairs exist in someone's cart, not just whether one
exists. Can you write something that counts them?"""

# O(n) time, O(n) space
def apply_promotion_count(numbers, target):
    costs = numbers
    seen = set()
    pairs = []
    for cost in costs:
        needed = target - cost
        if needed in seen:
            pairs.append((cost, needed))
        seen.add(cost)
    return len(pairs)          # a COUNT, not the pairs themselves

print('apply_promotion_count:', apply_promotion_count([25,25,12,38,24,16,26] ,50))


"""We want to find the product that's ordered the LEAST often today, so we
can flag it for a possible clearance sale. Given a list of product IDs
ordered today, can you write something that finds it?"""

# O(n) time, O(n) space
def find_least_frequent_item(product_ids):
    counts = {}
    for product_id in product_ids:
        if product_id not in counts:
            counts[product_id] = 0
        counts[product_id] += 1                    # STEP 1: build the frequency dict

    least_value = None
    least_count = None
    for product_id, count in counts.items():
        if least_count is None or count < least_count:   # STEP 2: scan for the SMALLEST
            least_value = product_id
            least_count = count
    return least_value

print('find_least_frequent_item:', find_least_frequent_item(['p1', 'p1', 'p2', 'p3', 'p3', 'p3']))



# ============================================================
# TIER 2 -- Data-record / grouping (matches the actual take-home domain)
# ============================================================

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
        customer = record['customer']
        amount = record['amount']
        if customer not in totals:
            totals[customer] = 0
        totals[customer] += amount

    best_customer = None
    best_total = 0
    for customer, total in totals.items():
        if total > best_total:
            best_customer = customer
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
def is_balanced(code):
    stack = []
    for char in code:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:          # a closer with nothing open to match -> unbalanced
                return False
            stack.pop()
    return not stack                # True only if every opener got closed

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
