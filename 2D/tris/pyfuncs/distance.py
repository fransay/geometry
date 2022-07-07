import math as m


def distance(stn1: tuple, stn2: tuple):
    eastings, northings = stn2[0] - stn1[0], stn2[1] - stn1[1]
    return m.sqrt(pow(eastings, 2) + pow(northings, 2))
