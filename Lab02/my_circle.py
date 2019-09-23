"""Demonstrates mathematical functions for Lab 02."""

PI = 3.14159
radius = 0

radius = float(input("Please enter the circle's radius "))

circumference = float(2 * PI * radius)
print("The circle's circumference is " + str(circumference))

area = PI * radius * radius
print("The circle's area is " + str(area))

#  Now onto fun. Investigate results of doubling radius

double_radius = radius * 2
new_area = PI * double_radius * double_radius
new_circumference = 2 * PI * double_radius
print("After doubling the radius, the area becomes " + str(new_area))
print("Further, after radius doubling, the circumference becomes " + str(new_circumference))

area_mag_change = new_area / area
circumference_mag_change = new_circumference / circumference

print("It has been determined that the area will change by " + str((int(area_mag_change))) +
      " when the area is doubled (" + str(area) + " to " + str(new_area) + ")")
print("It has further been determined that the circumference will change by " + str(int(circumference_mag_change)) + " "
      "when the circumference is doubled (" + str(circumference) + " to " + str(new_circumference) + ")")


