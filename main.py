import pygame
import numpy as np

from libs.XYAxes import XYAxes
from libs.Common import ScreenDimensions, Colors
from libs.Point import Point, PointCollection
from libs.Curve import Curve
from libs.ComplexCurves import BSplineCurve, HermiteCurve, NURBSCurve

background_colour = Colors.WHITE

(width, height) = (ScreenDimensions.WIDTH, ScreenDimensions.HEIGH)

screen = pygame.display.set_mode((width, height))

pygame.display.set_caption('Trabalho de OMOG')

screen.fill(background_colour)

center = Point(ScreenDimensions.WIDTH // 2, ScreenDimensions.HEIGH // 2)

# xyAxes = XYAxes(center.x, center.y, 5)
# xyAxes.draw(pygame, screen)

control_points = [
    Point(400, 250),
    Point(425, 50),
    Point(475, 50),
    Point(525, 300),
    Point(575, 200),
    Point(625, 250),
    Point(650, 100),
    Point(650, 100)
]

control_points_2 = [x.sum(Point(-300, 250)) for x in control_points]

control_points_3 = [
    Point(center.x, center.y),
    Point(center.x + 100, center.y),
    Point(center.x + 100, center.y - 200),
    Point(center.x, center.y - 200),
    Point(center.x - 100, center.y - 200),
    Point(center.x - 100, center.y),
    Point(center.x, center.y),
    Point(center.x, center.y)
]

weights_2 = [
    1, 0.5, 0.5, 1, 0.5, 0.5, 1, 1
]

weights = [
    1.0,
    1.0,
    1.0,
    5.0,
    1.0,
    1.0,
    2.0,
    1.0
]

# nurbsCurve = NURBSCurve(3, control_points_3, weights_2)
# nurbsCurve.draw(pygame, screen, 500, 2)

# for p in control_points_3:
#     p.draw(pygame, screen, 5, Colors.BLUE)

nurbsCurve = NURBSCurve(2, control_points, weights)

nurbsCurve.draw(pygame, screen, 500, 2)

bSplineCurve = BSplineCurve(2, control_points_2)

bSplineCurve.draw(pygame, screen, 500, 2)

for p in control_points:
    p.draw(pygame, screen, 5, Colors.BLUE)

for p in control_points_2:
    p.draw(pygame, screen, 5, Colors.BLUE)

# hermiteCurve = HermiteCurve(Point(50, 50), Point(400, 250),
#                             Point(600, -300), Point(25, -200), 1000)

# hermiteCurve.draw(pygame, screen, 2)


pygame.display.flip()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # update the screen
    pygame.display.update()