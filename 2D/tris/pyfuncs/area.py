from distance import distance as d
from statfuncs import mean as m
from math import sqrt as sq


def area_shoelace(stn1: tuple, stn2: tuple, stn3: tuple):
    """return area result of triangle, employing the shoelace algorithm"""
    pass


def area_sides(stn1: tuple, stn2: tuple, stn3: tuple):
    """return area result of triangle, employing the sides algorithm"""
    try:
        leng_of_side1 = abs(d(stn1, stn2))
        leng_of_side2 = abs(d(stn2, stn3))
        leng_of_side3 = abs(d(stn1, stn3))
        s = m.mean(leng_of_side1, leng_of_side2, leng_of_side3)
        area_result = sq(s * (s - leng_of_side1) * (s - leng_of_side2) * (s-leng_of_side3))
    except ValueError:
        return "Unable to return undefined results by sides algorithm"
    return area_result


print(area_sides((176, 244), (42, 4), (45, 64)))
