from math import sqrt as s


def perimeter(stn1, stn2, stn3, stn4):
    """returns the total length around the quad"""

    def distance(pnt1, pnt2):
        """ptn must assume the form (x,y)"""
        return s(abs((pnt1[0] - pnt2[0]) - (pnt1[1] - pnt2[1])))

    return distance(stn1, stn2) + distance(stn2, stn3) + distance(stn3, stn4) + distance(stn1, stn4)



if __name__ == '__main__':
    print(perimeter([200, 893], [43, 6], [47, 7], [6, 8]))
