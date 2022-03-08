import math


class linearRing(object):
    def __init__(self, *points):
        self.points = points

    def length(self):
        m, n = 0, 1
        total_length = 0
        while len(self.points) >= n:
            point1, point2 = self.points[m], self.points[n]
            diff_in_x, diff_in_y = point2[0] - point1[0], point2[1] - point1[1]
            add_diff = diff_in_x ** 2 + diff_in_y ** 2
            dist = math.sqrt(add_diff)
            total_length += dist
            m += 1
            n += 1
            return total_length

    def area(self):

        """calculating area using coordinates"""
        len_of_points = len(self.points)

        b, u = 0, 1
        forwardPassResults, backwardPassResults = 0, 0

        sumForwardPassResults, sumBackwardPassResults = 0, 0
        for x in range(len_of_points - 1):
            index_one, index_two = self.points[b][1], self.points[u][0]
            index_three = self.points[b][0]
            index_four = self.points[u][1]

            forwardPassResults, backwardPassResults = index_one * index_two, index_three * index_four

            sumForwardPassResults = sumForwardPassResults + forwardPassResults
            sumBackwardPassResults = sumBackwardPassResults + backwardPassResults
            b, u = u, u + 1

        areaOfLinearRing = (sumForwardPassResults - sumBackwardPassResults) / 2
        return abs(areaOfLinearRing)


    def centriod(self):

        """centriod also known as geometric center is the arithmetic mean position
        of all the points in the plane figure. the barycenter in geometry is also another
        name of the centriod...source {https://en.wikipedia.org/wiki/Centroid}
        """

        x_collection, y_collection = [], []
        for m in self.points:
            x_collection.append(m[0])
            y_collection.append(m[1])
        return f" Centroid : {sum(x_collection)/len(x_collection), sum(y_collection)/len(y_collection)}"



    def __str__(self):
        """WKR string representation"""
        return f"POINTS : {self.points}"


if __name__ == '__main__':
    linearRingOne = linearRing([105450.54544, 203404545], [309450, 40670], [5056550, 600], [707570, 866500], [900, 10600])
    print(linearRingOne.area())
    print(linearRingOne.centriod())





