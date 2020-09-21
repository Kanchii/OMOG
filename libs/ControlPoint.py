from .Point import Point
from .Common import Colors

from math import sqrt

class ControlPointHandler:
    def __init__(self, control_points):
        self.control_points = control_points

        self.selected = -1
    
    def draw(self, pygame, screen):
        for control_point in self.control_points:
            control_point.draw(pygame, screen)
    
    def getValue(self, idx):
        return self.control_points[idx].pos

    def getWeight(self, idx):
        return self.control_points[idx].weight

    def desloc(self, deslocamento):
        for control_point in self.control_points:
            control_point.pos = control_point.pos.sum(deslocamento)

    def MouseClick(self, x, y, idx):
        self.control_points[idx].pos = Point(x, y)
    
    def DotSelected(self, idx):
        for control_point in self.control_points:
            control_point.ResetColor()
        if(idx != None):
            self.control_points[idx].radius *= 2
            self.control_points[idx].color = Colors.PURPLE
            

class ControlPoint:
    def __init__(self, x, y, radius, number, weight = None, terminal = False, color = Colors.BLUE):
        self.pos = Point(x, y)
        self.number = number
        self.terminal = terminal
        self.weight = weight
        self.color = color
        self.real_color = color

        self.radius = radius
        self.real_radius = radius

    def draw(self, pygame, screen):
        self.pos.draw(pygame, screen, self.radius, self.color)
    
    def __str__(self):
        return self.pos.__str__()

    def SetColor(self, color):
        self.color = color
    
    def ResetColor(self):
        self.color = self.real_color
        self.radius = self.real_radius

    def IsPressed(self, x, y):
        if(sqrt((x - self.pos.x) ** 2 + (y - self.pos.y) ** 2) <= self.radius):
            return True
        return False