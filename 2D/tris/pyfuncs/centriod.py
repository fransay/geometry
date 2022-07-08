def centriod(stn1: tuple, stn2: tuple, stn3: tuple):
    """return the cartesian coordinate of the centriod"""
    return (stn1[0] + stn2[0] + stn3[0]) / 3, (stn1[1] / 3 + stn2[1] / 3 + stn3[1] / 3) / 3

