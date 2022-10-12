# Area of the circle:
# Program to calculate the area of  circle.
# Bir dairenin alanını hesaplama programı.

radius = int(input("Enter the radius of the circle: "))
pi = 3.14

if radius > 0:
    area = pi * radius ** 2
    print("Area of the circle:", area)
else:
    print("The radius must be a positive integer!")
