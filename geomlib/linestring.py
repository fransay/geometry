# polygonal chain consist of a series of node(s) or point stn(s)

import math


class linestring(object):
    def __init__(self, *points: list):
        self.points = points


    def length(self):
        """the length of a linestring is the sum total of the individual line segments making up the string"""
        m, n = 0, 1
        total_length = 0
        while len(self.points) >= n:
            point1 = self.points[m]
            point2 = self.points[n]
            diff_in_x = point2[0] - point1[0]
            diff_in_y = point2[1] - point1[1]
            add_diff = diff_in_x ** 2 + diff_in_y ** 2
            dist = math.sqrt(add_diff)
            total_length += dist
            m += 1
            n += 1
            return total_length


    def area(self, shape):
        """a line string in space has no area"""
        return None


    def centriod(self):
        """centroid of a line segment can be considered as  the midpoint of the line"""

    def str(self):
        """WKT string version"""
        pass


if __name__ == '__main__':
    linestring_one = linestring([1, 2], [2, 4])
    print(linestring_one.length())
