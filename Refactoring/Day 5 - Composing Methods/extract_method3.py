# Written by Kamran Bigdely
# Example for Compose Methods: Extract Method.
import math

xc1 = 4
yc1 = 4.25

xc2 = 53
yc2 = -5.35
# Calculate the distance between the two circle
distance = distance_of_two_circles(xc1, yc1, xc2, yc2)
print('distance', distance)

def distance_of_two_circles(x_circle1, y_circle1, x_circle2, y_circle2):
    """Calculate the distance between the two circle"""
    x_distance = (x_circle1 - x_circle2)**2
    y_distance = (y_circle1 - y_circle2)**2
    distance = math.sqrt(x_distance + y_distance)
    return distance

# *** somewhere else in your program ***
xa = -36
ya = 97

xb = .34
yb = .91
# calcualte the length of vector AB vector which is a vector between A and B points.
length = math.sqrt((xa-xb)*(xa-xb) + (ya-yb)*(ya-yb))
print('length', length)
