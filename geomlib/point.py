from geomlib.geom import geom


class point(geom):
    def __init__(self, x, y):
        super().__init__(x, y)


    def length(self):
        """a point has no length"""
        return 0.0

    def area(self, shape):
        """a point in space has no area, unless represented by shape"""
        if shape.lower() == 'square' or shape.lower() == 'rectangle':
            area = self.x * self.y
            return area
        return 'point geom has no area'

    def centriod(self):
        """centroid of a point is the same as the x and y coords of the point"""
        centroid = (self.x, self.y)
        return centroid

    def __str__(self):
        """WKT representation"""
        return f'POINT ({self.x} {self.y})'


if __name__ == '__main__':
    point_one = point(1, 2)
    print("area--->", point_one.area('square') ,"<--->>>length:", point_one.length())
