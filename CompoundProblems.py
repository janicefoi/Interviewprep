# Each of these combines TWO shapes you already know. Before coding, name
# both shapes out loud first -- that's the actual skill being tested here,
# not new syntax.

"""Given a list of order IDs (one entry per order placed today, same customer
can appear more than once), can you tell me how many DISTINCT customers
placed more than one order today?"""
# Hint: this is frequency-counting (Tier 1), then a second counting pass
# over the resulting counts -- "how many entries in this dict have a count > 1?"




"""Given two lists of product IDs -- items currently in stock, and items that
were returned today -- can you return the returned items that are NOT
currently in stock (meaning they need to be restocked)?"""
# Hint: this is set subtraction (Level 3/4), just reframed as "needs action"
# instead of "what's different."




"""Given a list of order records, each one like {'id': 'o1', 'amount': 20},
can you find two orders whose amounts add up to exactly $50, and return
their IDs (not the amounts)?"""
# Hint: two-sum (Tier 1), but reading a field out of a record first (Tier 2)
# instead of working with plain numbers directly.




"""Given a string of brackets that might NOT be balanced, instead of just
True/False, can you return the index of the first character that breaks
the balance? Return -1 if it's actually balanced."""
# Hint: same stack mechanics as is_balanced, but instead of returning False,
# you need to know WHERE you were in the loop when it broke.




"""Given a list of daily sales totals, can you find the length of the longest
stretch of CONSECUTIVE days where sales kept strictly increasing day over
day?"""
# Hint: same growing/resetting window shape as longest_run_of_evens, but the
# condition to check is "is today's number bigger than yesterday's,"
# not "is this number even."




"""A list should contain every number from 1 to n exactly once, but instead
it has one number MISSING and a different number appearing TWICE (so the
list still has n numbers total). Can you find both the missing number and
the duplicate?"""
# Hint: this needs both find_missing_n's reasoning AND has_duplicates'
# reasoning at the same time -- think about what a single pass with one
# set can tell you about both at once.

