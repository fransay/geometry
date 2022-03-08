from geomlib.geom import geom
from linear_ring import linearRing


class polygon(linearRing):
    def __init__(self, *points):
        super().__init__(*points)

    def length(self):
        """the length of a polygon must be similar or the same as that of linearRing """
        return linearRing.length()

    def area(self):
        """the length of a polygon must be similar or the same as that of linearRing """

        return linearRing.area()

    def centriod(self):
        """the length of a polygon must be similar or the same as that of linearRing """

        return linearRing.centriod()

    def __str__(self):
        """WKR string representation"""

        return linearRing.__str__()

    # Unfinished and there is more to add!!!!
    # {

    
    # }
