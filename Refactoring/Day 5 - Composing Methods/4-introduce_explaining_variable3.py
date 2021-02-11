# by Kami Bigdely
# Extract Variable (alias introduce explaining variable)
WELL_DONE = 900000
MEDIUM = 600000
COOKED_CONSTANT = 0.05

def is_cookeding_criteria_satisfied(time, temperature, pressure, desired_state):
    cook_level = time * temperature * pressure * COOKED_CONSTANT
    is_well_done = desired_state == 'well-done'
    is_medium = desired_state == 'medium'
    if is_well_done and cook_level >= WELL_DONE: 
        return True
    if is_medium and cook_level >= MEDIUM:
        return True
    return False