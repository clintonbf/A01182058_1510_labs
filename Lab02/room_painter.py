"""Code to demonstrate mathematical functions."""


def COVERAGE():
    """constant.

    :return: value of COVERAGE"""
    return 400  # sq. feet


length = int(input("Provide the room length (ft): "))
width = int(input("Provide the room's width (ft): "))
height = int(input("How high is the room?: ") )

coats = int(input("How many coats of paint do you want to add? "))

lateral_wall_area = length * height
anterior_wall_area = width * height
ceiling_area = length * width

surface_area = (lateral_wall_area * 2) + (anterior_wall_area * 2) + ceiling_area

coverage_needed = surface_area * coats

cans_of_paint = coverage_needed / COVERAGE()

print("Head to the paint store and order " + str(cans_of_paint) + " cans of paint. Tell them Clint sent you.")
