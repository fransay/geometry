import math as m


def angles(stn1: tuple, stn2: tuple, stn3: tuple):
    """returns the angles formed at the vertices"""

    def bearing(stat1, stat2):
        return m.atan((stat1[1] - stat2[1]) / (stat1[0] - stat2[0]))

    # angle formed at stn1
    """
    determine bearing from stn1 to stn2 and bearing from stn1 to stn3,
    return the difference in bearing as the angle formed at stn1
    """
    angle_stn1 = bearing(stn1, stn2) - bearing(stn1, stn3)

    # angle formed at stn2
    """
    determine bearing from stn2 to stn1 and bearing from stn2 to stn3,
    return the difference in bearing as the angle formed at stn1
    """
    # angle formed at stn3
    angle_stn2 = bearing(stn2, stn1) - bearing(stn2, stn3)
    """
    determine bearing from stn3 to stn1 and bearing from stn3 to stn2,
    return the difference in bearing as the angle formed at stn1
    """

    angle_stn3 = bearing(stn3, stn1) - bearing(stn3, stn2)
    return f'Angle of station 1= {angle_stn1}, Angle of station 2 = {angle_stn2},' \
           f'Angle of station 3= {angle_stn3}'


