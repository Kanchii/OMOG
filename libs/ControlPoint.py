from .Point import Point
from .Common import Colors

from math import sqrt

class ControlPointHandler:
    def __init__(self, control_points):
        self.control_points = control_points

        self.selected = -1
    
    def draw(self, pygame, screen):
        for control_point in self.control_points:
            if(control_point.terminal):
                continue
            control_point.draw(pygame, screen)
    
    def getValue(self, idx):
        return self.control_points[idx].pos

    def getWeight(self, idx):
        return self.control_points[idx].weight

    def desloc(self, deslocamento):
        for control_point in self.control_points:
            control_point.pos = control_point.pos.sum(deslocamento)

    def MouseClick(self, x, y):
        if(self.selected == -1):
            for idx, control_point in enumerate(self.control_points):
                if(control_point.IsPressed(x, y)):
                    self.selected = idx
                    break
        else:
            if(not self.control_points[self.selected].IsPressed(x, y)):
                self.selected = -1
                return
            self.control_points[self.selected].pos = Point(x, y)
            

class ControlPoint:
    def __init__(self, x, y, radius, number, weight = None, terminal = False, color = Colors.BLUE):
        self.pos = Point(x, y)
        self.number = number
        self.terminal = terminal
        self.weight = weight
        self.color = color

        self.radius = radius

    def draw(self, pygame, screen):
        self.pos.draw(pygame, screen, self.radius, self.color if not self.terminal else Colors.RED)
    
    def __str__(self):
        return self.pos.__str__()

    def IsPressed(self, x, y):
        if(sqrt((x - self.pos.x) ** 2 + (y - self.pos.y) ** 2) <= self.radius):
            return True
        return False