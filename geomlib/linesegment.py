
import math


class linesegment(object):
    def __init__(self, pointA: list, pointB: list):
        self.pointA = pointA
        self.pointB = pointB

    def length(self):  # point A and point B
        """a line segment has a length"""
        change_y, change_x = self.pointB[1] - self.pointA[1], self.pointB[0] - self.pointA[0]
        axis_change = change_y - change_x
        _length = math.sqrt(axis_change)
        return _length


    def area(self, shape):
        """a line segment in space has no area"""
        return None

    def centriod(self):
        """centroid of a line segment can be considered as the the midpoint of the line"""
        _centroid = (self.x / 2, self.y / 2)
        return _centroid

    def __str__(self):
        """WKT string representation"""
        return f'POINTA({self.pointA[0]}, {self.pointA[1]}) , POINTB({self.pointB[0]},{self.pointB[1]})'
        pass


if __name__ == '__main__':
    linesegment_one = linesegment([32, 34], [6, 78])
    print(linesegment_one.length())
