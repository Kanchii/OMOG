from .Line import *
from .Common import Colors

import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    def toTuple(self):
        return (self.x, self.y)

    def sum(self, o):
        return Point(self.x + o.x, self.y + o.y)

    def vet(self, o):
        return Point(o.x - self.x, o.y - self.y)
    
    def norm(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)
    
    def dot_product(self, o):
        return (self.x * o.x) + (self.y * o.y)
    
    def rotate(self, angle):
        return Point(self.x * math.cos(angle) - self.y * math.sin(angle),
                        self.x * math.sin(angle) + self.y * math.cos(angle))
    
    def div(self, k: float):
        if(k == 0):
            return Point(0, 0)
        return Point(self.x / k, self.y / k)
    
    def mult(self, k: float):
        return Point(self.x * k, self.y * k)
    
    def draw(self, pygame, screen, radius, color):
        pygame.draw.circle(screen, color, self.toTuple(), radius, 0)

class PointCollection:
    def __init__(self, points: [Point]):
        self.points = points
    
    def add(self, point: Point):
        self.points.append(point)

    def addRange(self, points):
        for point in points.points:
            self.points.append(point)

    def interpolate(self, thickness = 1) -> LineCollection:
        self.lineCollection = LineCollection([])
        for i in range(1, len(self.points)):
            self.lineCollection.add(Line(self.points[i - 1], self.points[i], thickness, Colors.BLACK))
        
        return self.lineCollection
