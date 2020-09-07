from .Point import Point, PointCollection
from .Curve import Curve
from .Common import Colors
import numpy as np

class BSplineCurve:
    def __init__(self, degree: int, control_points: [Point]):
        self.degree = degree
        self.number_of_points = degree + 1
        self.control_points = control_points

        self.knots = self.CalculateKnots()        

    def CalculateKnots(self):
        knots = []
        for i in range(len(self.control_points) + self.number_of_points + 1):
            if(i < self.number_of_points):
                knots.append(0)
            elif(i <= len(self.control_points)):
                knots.append(i - self.number_of_points + 1)
            else:
                knots.append(len(self.control_points) - self.number_of_points + 2)
        print("knots", knots)
        return [float(x) for x in knots]

    def CalcuteBasisFunction(self, u, i, k):
        if(k == 1):
            if(self.knots[i] <= u and u < self.knots[i + 1]):
                return 1.0
            else:
                return 0.0
        try:
            first = ((u - self.knots[i]) / float(self.knots[i + k - 1] - self.knots[i])) * self.CalcuteBasisFunction(u, i, k - 1)
        except ZeroDivisionError:
            first = 0.0
        except:
            raise
        
        try:
            second = ((self.knots[i + k] - u) / float(self.knots[i + k] - self.knots[i + 1])) * self.CalcuteBasisFunction(u, i + 1, k - 1)
        except ZeroDivisionError:
            second = 0.0
        except:
            raise

        return first + second
    
    def GenerateSegment(self, s, number_points, weights = None):
        points_list = PointCollection([])
        for u in np.arange(s, s + 1 + (1.0)/float(number_points), 1.0 / float(number_points)):
            p = Point(0, 0)
            u = float(u)
            nurbs_weight = 1 if weights == None else 0
            for i in range(self.number_of_points):
                v = self.CalcuteBasisFunction(u, s + i, self.number_of_points)
                if(weights != None):
                    v *= weights[s+i]
                    nurbs_weight += v
                pv = self.control_points[s+i].mult(v)
                p = p.sum(pv)
            if(nurbs_weight == 0):
                continue
            points_list.add(p.div(nurbs_weight))
        return points_list
    
    def draw(self, pygame, screen, number_points, thickness, color = Colors.RED):
        for i in range(0, len(self.control_points) - self.number_of_points + 1):
            segment = self.GenerateSegment(i, number_points)
            segment_interpolate = segment.interpolate(thickness)
            segment_interpolate.draw(pygame, screen, color)

class NURBSCurve:
    def __init__(self, degree: int, control_points: [Point], weights: [float]):
        self.bSplineCurve = BSplineCurve(degree, control_points)
        self.weights = weights
    
    def draw(self, pygame, screen, number_points, thickness, color = Colors.RED):
        for i in range(0, len(self.bSplineCurve.control_points) - self.bSplineCurve.number_of_points + 1):
            segment = self.bSplineCurve.GenerateSegment(i, number_points, self.weights)
            segment_interpolate = segment.interpolate(thickness)
            segment_interpolate.draw(pygame, screen, color)

class HermiteCurve:
    def __init__(self, p0: Point, p1: Point, v0: Point, v1: Point, total_points: int):
        self.p0 = p0
        self.p1 = p1
        self.v0 = v0
        self.v1 = v1
        self.total_points = total_points

        self.generateCurve(self.total_points)
    def generateCurve(self, total_points):
        pointCollection = PointCollection([])
        unit = 1 / float(total_points)
        for t in np.arange(0.0, 1.0 + unit, unit):
            pointCollection.add(self.resolve(t))
        
        self.curve = Curve(pointCollection)

    def draw(self, pygame, screen, thickness, color = Colors.GREEN):
        self.curve.draw(pygame, screen, 2, color)

    def resolve(self, t) -> Point:
        x = self.resolve_x(t)
        y = self.resolve_y(t)

        return Point(x, y)

    def resolve_x(self, t):
        return self.p0.x * (2 * t ** 3 - 3 * t ** 2 + 1) +\
                self.p1.x * (-2 * t ** 3 + 3 * t ** 2) + \
                self.v0.x * (t ** 3 - 2 * t ** 2 + t) +\
                self.v1.x * (t ** 3 - t ** 2)
    
    def resolve_y(self, t):
        return self.p0.y * (2 * t ** 3 - 3 * t ** 2 + 1) +\
                self.p1.y * (-2 * t ** 3 + 3 * t ** 2) + \
                self.v0.y * (t ** 3 - 2 * t ** 2 + t) +\
                self.v1.y * (t ** 3 - t ** 2)
