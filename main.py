import pygame
import numpy as np

from libs.XYAxes import XYAxes
from libs.Common import ScreenDimensions, Colors
from libs.Point import Point, PointCollection
from libs.Curve import Curve
from libs.ComplexCurves import HermiteCurve, NURBSCurve

from libs.JointCurveHandler import JointCurveHandler

from libs.Button import Button
from libs.ControlPoint import ControlPointHandler, ControlPoint

background_colour = Colors.WHITE

(width, height) = (ScreenDimensions.WIDTH, ScreenDimensions.HEIGH)

screen = pygame.display.set_mode((width, height))

pygame.display.set_caption('Trabalho de OMOG')

screen.fill(background_colour)

center = Point(ScreenDimensions.WIDTH // 2, ScreenDimensions.HEIGH // 2)

ControlPointHandlerNurbs = ControlPointHandler(
    [
        ControlPoint(400, 250, 8, 1, 1.0, terminal=True),
        ControlPoint(425, 50, 4, 2, 1.0),
        ControlPoint(475, 50, 4, 3, 1.0),
        ControlPoint(525, 300, 4, 4, 0.0),
        ControlPoint(575, 200, 4, 5, 1.0),
        ControlPoint(625, 250, 4, 6, 1.0),
        ControlPoint(650, 100, 8, 7, 2.0, terminal=True)
    ]
)

nurbsCurve = NURBSCurve(4, ControlPointHandlerNurbs)



controlPointHandlerHermite = ControlPointHandler([ControlPoint(300, 300, 8, 1, terminal=True, color=Colors.RED),
                                            ControlPoint(300, 150, 4, 2, color=Colors.GREEN),
                                            ControlPoint(200, 300, 8, 3, terminal=True, color=Colors.BLACK),
                                            ControlPoint(100, 350, 4, 4, color=Colors.GRAY)])
hermiteCurve = HermiteCurve(controlPointHandlerHermite)

jointCurveHandler = JointCurveHandler(nurbsCurve, hermiteCurve)
# jointCurveHandler.Draw(pygame, screen, 2, [Colors.RED, Colors.GREEN], 300)

pygame.display.flip()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if(pygame.mouse.get_pressed()[0]):
        mouse_pos = pygame.mouse.get_pos()

        hermiteCurve.controlPointHandler.MouseClick(mouse_pos[0], mouse_pos[1])
        nurbsCurve.controlPointHandler.MouseClick(mouse_pos[0], mouse_pos[1])

    
    screen.fill(Colors.WHITE)

    xyAxes = XYAxes(center.x, center.y, 5)
    xyAxes.draw(pygame, screen)

    # hermiteCurve.GenerateCurve(300)
    jointCurveHandler.Draw(pygame, screen, 2, [Colors.RED, Colors.GREEN], 100)

    # update the screen
    pygame.display.update()