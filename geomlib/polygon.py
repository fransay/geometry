
from linear_ring import linearRing


class polygon(linearRing):
    def __init__(self, *points):
        super().__init__(*points)

    def length(self):
        """the length of a polygon must be similar or the same as that of linearRing """
        return linearRing.length(self)

    def area(self):
        """the length of a polygon must be similar or the same as that of linearRing """

        return linearRing.area(self)

    def centriod(self):
        """the length of a polygon must be similar or the same as that of linearRing """

        return linearRing.centriod(self)

    def __str__(self):
        """WKR string representation"""

        return linearRing.__str__(self)



if __name__ == '__main__':
    polygon1 = polygon([1, 3], [3, 5], [4, 5])
    print(polygon1.area())
    print(polygon1.length())
