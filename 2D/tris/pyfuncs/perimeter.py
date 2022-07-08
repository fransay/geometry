from distance import distance


def perimeter(stn1: tuple, stn2: tuple, stn3: tuple):
    """returns perimeter when coordinates are given"""
    return distance(stn1, stn2) + distance(stn2, stn3) + distance(stn3, stn1)


def perimeter_dist(d1, d2, d3):
    """perimeter when given distances"""
    return d1+d2+d3


