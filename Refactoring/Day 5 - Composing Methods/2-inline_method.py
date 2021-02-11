# by Kami Bigdely
# Inline method.
# TODO: Refactor this program to improve its readability.

LEGAL_DRINKING_AGE = 18
class Person:
    def __init__(self, my_age):
        self.age = my_age
        
def enter_night_club(individual):
    if is_drinking_age(individual.age):
        print("Allowed to enter.")
    else:
        print("Enterance of minors is denited.")

def is_drinking_age(age):
    if age > LEGAL_DRINKING_AGE:
        return True
    return False
    
    
person = Person(17.9)
enter_night_club(person)
        
