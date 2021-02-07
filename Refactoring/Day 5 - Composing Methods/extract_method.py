# Written by Kamran Bigdely
# Example for Compose Methods: Extract Method.
import math 

def print_stat():
    """ 
        Prints a list of user's inputs and its mean and standard deviation
    """
    grade_list = get_user_inputs()
    mean = calculate_mean(grade_list)
    sd = calculate_standard_deviation(grade_list)
    # print out the mean and standard deviation in a nice format.
    print('****** Grade Statistics ******')
    print("The grades's mean is:", mean)
    print('The population standard deviation of grades is: ', round(sd, 3))
    print('****** END ******')

def get_user_inputs():
    grade_list = []
    n_student = 5
    for _ in range(0, n_student):
        grade_list.append(int(input('Enter a number: ')))
    return grade_list

def calculate_mean(grade_list):
    total = 0
    for grade in grade_list:
        total += grade
    mean = total / len(grade_list)
    return mean

def calculate_standard_deviation(grade_list):
    mean = calculate_mean(grade_list)
    sd = 0 # standard deviation
    sum_of_sqrs = 0
    for grade in grade_list:
        sum_of_sqrs += (grade - mean) ** 2
    sd = math.sqrt(sum_of_sqrs / len(grade_list))
    return sd

print_stat()
