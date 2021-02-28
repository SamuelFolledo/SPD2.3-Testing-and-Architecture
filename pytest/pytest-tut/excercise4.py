# by Kami Bigdely
# Replace nested conditional with gaurd clauses

import pytest

def extract_position(line):
    if not line or 'debug' in line or 'error' in line or 'x:' not in line:
        return None
    start_index = line.find('x:') + 2
    pos = line[start_index:] # from start_index to the end.
    return pos

# if __name__ == "__main__":
#     result1 = extract_position('|error| numerical calculations could not converge.')
#     print(result1)
#     result2 = extract_position('|update| the positron location in the particle accelerator is x:21.432')
#     print(result2)


########## TESTS ##########

# FIXTURES
@pytest.fixture
def average_input():
    return "|update| the positron location in the particle accelerator is x:21.432"

@pytest.fixture
def null_input():
    return None

@pytest.fixture
def error_input():
    return "|error| numerical calculations could not converge."

# TESTS
def test_extract_position_average_case(average_input):
    # Expected Input - contains 'x:
    assert extract_position(average_input) == "21.432"

def test_extract_position_null_case(null_input):
    # NoneType Input
    assert extract_position(null_input) == None

def test_extract_position_error_case(error_input):
    # Error Input - 'debug' or 'error'
    assert extract_position(error_input) == None