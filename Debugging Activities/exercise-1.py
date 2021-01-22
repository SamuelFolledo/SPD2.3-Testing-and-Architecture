"""
Exercise 1
"""

# PART 1: Gather Information
#
# TODO: Gather information about the source of the error and paste your findings here. E.g.:
# - What is the expected vs. the actual output?
#   - should print 4, but the actual output is an error: index out of range
# - What error message (if any) is there?
#   - IndexError: list index out of range
# - What line number is causing the error?
#   - diff = abs(list_of_nums[i] - list_of_nums[i+1])
# - What can you deduce about the cause of the error?
#   - i+1 will crash at the last iteration

# PART 2: State Assumptions
#
# TODO: State your assumptions here or say them out loud to your partner ...
# Make sure to be SPECIFIC about what each of your assumptions is!
# I assume that the developer did not test properly all the way to the last value of a list and forgot to subtract 1 on length of list in order to not go out of bounds

def find_largest_diff(list_of_nums):
    """Find the largest difference between *consecutive* numbers in a list."""
    largest_diff = 0
    for i in range(len(list_of_nums)):
        diff = abs(list_of_nums[i] - list_of_nums[i+1])
        if diff > largest_diff:
            largest_diff = diff

    return largest_diff

if __name__ == '__main__':
    print('### Problem 1 ###')
    answer = find_largest_diff([5, 3, 1, 2, 6, 4])

    # This should print 4, as the largest diff between consecutive numbers is between 2 and 6
    print(answer)