"""
Exercise 4
"""

# PART 1: Gather Information
#
# TODO: Gather information about the source of the error and paste your findings here. E.g.:
# - What is the expected vs. the actual output?
#   - searching for 7, it is expected to get index 4, but output is infinite recursion
# - What error message (if any) is there?
#   - RecursionError: maximum recursion depth exceeded while calling a Python object
# - What line number is causing the error?
#   - calling binary_search again and again
# - What can you deduce about the cause of the error?
#   - Developer did not update the mid's index


# PART 2: State Assumptions
#
# TODO: State your assumptions here or say them out loud to your partner ...
# Make sure to be SPECIFIC about what each of your assumptions is!
# HINT: It may help to draw a picture to clarify what your assumptions are.
#   - Developer assumed to pass the mid as the low or high despite of making sure that the mid does not contain the element we are looking for

def binary_search(arr, element, low=0, high=None):
    """Returns the index of the given element within the array by performing a binary search."""
    
    if high == None:
        high = len(arr) - 1

    if high < low:
        return -1

    mid = (high + low) // 2 # get the mid number and round up

    if arr[mid] == element: 
        return mid

    elif arr[mid] > element:
        return binary_search(arr, element, low, mid - 1)

    else: 
        return binary_search(arr, element, mid + 1, high)


if __name__ == '__main__':
    answer = binary_search([1, 2, 4, 5, 7], 7)
    print(answer)