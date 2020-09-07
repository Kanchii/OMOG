from .Point import *
from .Line import *

class Curve:
    def __init__(self, points: PointCollection):
        self.points = points
    
    def draw(self, pygame, screen, thickness = 1, color = Colors.BLACK):
        self.points.interpolate(thickness).draw(pygame, screen, color)
