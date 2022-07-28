from math import sqrt as s


def perimeter(stn1, stn2, stn3, stn4):
    """returns the total length around the quad"""

    def distance(pnt1, pnt2):
        """ptn must assume the form (x,y)"""
        return s((pnt1[0] - pnt2[0]) - (pnt1[0] - pnt2[0]))

    return sum(distance(stn1, stn2) + distance(stn2, stn3) + distance(stn3,stn4) + distance(stn4, stn1))
