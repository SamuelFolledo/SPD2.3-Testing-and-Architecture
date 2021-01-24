"""
Exercise 3
"""

# PART 1: Gather Information
#
# TODO: Gather information about the source of the error and paste your findings here. E.g.:
# - What is the expected vs. the actual output?
#   - expected a sorted number but got an error instead
# - What error message (if any) is there?
#   - Error message is "IndexError: list index out of range"
# - What line number is causing the error?
#   - while key < arr[j]
# - What can you deduce about the cause of the error?
#   - Developer does not know how to insert error and to worry about the last element to move


# PART 2: State Assumptions
#
# TODO: State your assumptions here or say them out loud to your partner ...
# Make sure to be SPECIFIC about what each of your assumptions is!
# HINT: It may help to draw a picture to clarify what your assumptions are.
#   - Developer didnt foresee that if element to move (j's index) is less than the length of arr, then that number will not exist anymore

# What is insertion sort: https://www.youtube.com/watch?v=JU767SDMDvA

def insertion_sort(arr):
    """Performs an Insertion Sort on the array arr."""
    for i in range(1, len(arr)-1):
        key = arr[i] 
        j = i-1
        while key < arr[j] and j >= 0: #Move elements of arr[0..i-1], that are greater than key, to one position ahead of their current position
            arr[j+1] = arr[j] 
            j -= 1
        arr[j+1] = key
    return arr

if __name__ == '__main__':
    print('### Problem 3 ###')
    answer = insertion_sort([5, 2, 3, 1, 6])
    print(answer)

