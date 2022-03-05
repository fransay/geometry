
from geomlib.geom import geom


class polygon(geom):
    def __init__(self, x, y):
        super().__init__(x, y)


    def length(self):
        pass


    def area(self):
        pass

    def centriod(self):
        pass

    def __str__(self):
        return f""