from .Point import Point, PointCollection
from .Curve import Curve
from .Common import Colors
import numpy as np

class NURBSCurve:
    def __init__(self, degree: int, control_points: [Point], weights: [float] = None):
        self.degree = degree
        self.number_of_points = degree + 1
        self.control_points = control_points

        self.knots = self.CalculateKnots()

        self.points = PointCollection([])

        self.weights = weights
    
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
        if(i + 1 == len(self.knots)):
            return
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
    
    def GenerateSegment(self, s, number_points):
        points_list = PointCollection([])
        unit = 1.0/float(number_points)
        print(s, self.number_of_points)
        for u in np.arange(s, s + 1 + unit, unit):
            p = Point(0, 0)
            u = float(u)
            nurbs_weight = 1 if self.weights == None else 0
            for i in range(self.number_of_points):
                v = self.CalcuteBasisFunction(u, s + i, self.number_of_points)
                if(self.weights != None):
                    v *= self.weights[s+i] if s+i < len(self.weights) else self.weights[-1]
                    nurbs_weight += v
                pv = self.control_points[s+i].mult(v) if s+i < len(self.control_points) else self.control_points[-1].mult(v)
                p = p.sum(pv)
            if(nurbs_weight == 0):
                continue
            points_list.add(p.div(nurbs_weight))
        self.points.addRange(points_list)

    def GenerateCurve(self, number_points):
        self.points = PointCollection([])
        for i in range(0, len(self.control_points) - self.number_of_points + 2):
            self.GenerateSegment(i, number_points)

    def Draw(self, pygame, screen, thickness, color = Colors.RED, debug = False):
        if(debug):
            for p, w in zip(self.control_points, self.weights):
                p.draw(pygame, screen, int(w)*2, Colors.BLUE)

        self.points.interpolate(thickness).draw(pygame, screen, color)

class HermiteCurve:
    def __init__(self, p0: Point, p1: Point, v0: Point, v1: Point):
        self.p_start = p0
        self.p_end = p1
        self.v_start = v0
        self.v_end = v1

        self.points = PointCollection([])
    
    def BuildCurve(self, number_points):
        pointCollection = PointCollection([])
        unit = 1 / float(number_points)
        for t in np.arange(0.0, 1.0 + unit, unit):
            pointCollection.add(self.Resolve(t))
        
        self.points.addRange(pointCollection)

    def GenerateCurve(self, number_points):
        self.points = PointCollection([])
        self.BuildCurve(number_points)

    def Draw(self, pygame, screen, thickness = 2, color = Colors.GREEN):
        self.points.interpolate(thickness).draw(pygame, screen, color)

    def Resolve(self, t) -> Point:
        x = self.Resolve_x(t)
        y = self.Resolve_y(t)

        return Point(x, y)

    def Resolve_x(self, t):
        return self.p_start.x * (2 * t ** 3 - 3 * t ** 2 + 1) +\
                self.p_end.x * (-2 * t ** 3 + 3 * t ** 2) + \
                self.v_start.x * (t ** 3 - 2 * t ** 2 + t) +\
                self.v_end.x * (t ** 3 - t ** 2)
    
    def Resolve_y(self, t):
        return self.p_start.y * (2 * t ** 3 - 3 * t ** 2 + 1) +\
                self.p_end.y * (-2 * t ** 3 + 3 * t ** 2) + \
                self.v_start.y * (t ** 3 - 2 * t ** 2 + t) +\
                self.v_end.y * (t ** 3 - t ** 2)
