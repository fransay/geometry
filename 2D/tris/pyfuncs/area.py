from distance import distance as d
from statfuncs import mean as m
from math import sqrt as sq, sin


def area_shoelace(stn1: tuple, stn2: tuple, stn3: tuple):
    """return area result of triangle, employing the shoelace algorithm"""
    f_run = (stn1[0]*stn2[1]) + (stn2[0]*stn3[1]) + (stn3[0]*stn1[1])
    b_run = (stn1[1]*stn2[0]) + (stn2[1]*stn3[0]) + (stn3[1]*stn1[0])
    return abs((f_run-b_run) / 2)


def area_sides(stn1: tuple, stn2: tuple, stn3: tuple):
    """return area result of triangle, employing the sides algorithm"""
    try:
        leng_of_side1 = abs(d(stn1, stn2))
        leng_of_side2 = abs(d(stn2, stn3))
        leng_of_side3 = abs(d(stn1, stn3))
        s = m.mean(leng_of_side1, leng_of_side2, leng_of_side3)
        area_result = sq(s * (s - leng_of_side1) * (s - leng_of_side2) * (s-leng_of_side3))
    except ValueError:
        return "undefined operation"
    return abs(area_result)


def area_dim(base, height):
    """return area value when dimensions of a tri-shape are given"""
    return 0.5 * base * height


def area_angle(angle, length1, length2):
    """return area value when an angle and the length of adjacent lines are given"""

    return 0.5 * length1 * length2 * sin(angle)





