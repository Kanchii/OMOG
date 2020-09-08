import pygame
import numpy as np

from libs.XYAxes import XYAxes
from libs.Common import ScreenDimensions, Colors
from libs.Point import Point, PointCollection
from libs.Curve import Curve
from libs.ComplexCurves import HermiteCurve, NURBSCurve

from libs.JointCurveHandler import JointCurveHandler

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
    Point(650, 100)
]

control_points_2 = [
    Point(200, 300),
    Point(300, 150),
    Point(400, 300),
    Point(500, 150),
    Point(600, 300)
]

weights_2 = [
    1.0,
    1.0,
    0.0,
    1.0,
    1.0
]

weights = [
    1.0,
    1.0,
    1.0,
    1.0,
    1.0,
    1.0,
    1.0
]

nurbsCurve = NURBSCurve(4, control_points, weights)
hermiteCurve = HermiteCurve(Point(10, 300), Point(200, 300),
                            Point(0, -300), Point(500, -200))


jointCurveHandler = JointCurveHandler(nurbsCurve, hermiteCurve)
jointCurveHandler.Draw(pygame, screen, 2, [Colors.RED, Colors.GREEN], 1000, True)

pygame.display.flip()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # update the screen
    pygame.display.update()