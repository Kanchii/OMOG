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
        ControlPoint(400, 250, 2, 1, 1.0, terminal=True),
        ControlPoint(425, 50, 4, 2, 1.0),
        ControlPoint(475, 50, 4, 3, 1.0),
        ControlPoint(525, 300, 4, 4, 2.0),
        ControlPoint(575, 200, 4, 5, 1.0),
        ControlPoint(625, 250, 4, 6, 1.0),
        ControlPoint(650, 100, 2, 7, 2.0, terminal=True)
    ]
)
nurbsCurve = NURBSCurve(4, ControlPointHandlerNurbs)

nurbsColor = Colors.RED

controlPointHandlerHermite = ControlPointHandler([ControlPoint(300, 300, 2, 1, terminal=True, color=Colors.RED),
                                            ControlPoint(300, 150, 4, 2, color=Colors.BLACK),
                                            ControlPoint(200, 300, 2, 3, terminal=True, color=Colors.RED),
                                            ControlPoint(100, 350, 4, 4, color=Colors.GRAY)])
hermiteCurve = HermiteCurve(controlPointHandlerHermite)

hermiteColor = Colors.GRAY

jointCurveHandler = JointCurveHandler(nurbsCurve, hermiteCurve)

pygame.display.flip()
running = True

curve_selected = 0
dot_select = 0

screen.fill(Colors.WHITE)

total_points = 300

jointCurveHandler.Draw(pygame, screen, 2, [nurbsColor, hermiteColor], total_points)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if(event.key == pygame.K_DOWN):
                curve_selected = 0
                dot_select = 0
            elif(event.key == pygame.K_UP):
                curve_selected = 1
                dot_select = 0
            elif(event.key == pygame.K_F1):
                jointCurveHandler.G0_C0()
            elif(event.key == pygame.K_F2):
                jointCurveHandler.C1()
            else:
                if(event.key == pygame.K_0):
                    dot_select = 0
                elif(event.key == pygame.K_1):
                    dot_select = 1
                elif(event.key == pygame.K_2):
                    dot_select = 2
                elif(event.key == pygame.K_3):
                    dot_select = 3
                elif(event.key == pygame.K_4):
                    dot_select = 4
                elif(event.key == pygame.K_5):
                    dot_select = 5
                elif(event.key == pygame.K_6):
                    dot_select = 6
                elif(event.key == pygame.K_7):
                    dot_select = 7
                elif(event.key == pygame.K_8):
                    dot_select = 8
                elif(event.key == pygame.K_9):
                    dot_select = 9
            
            if(curve_selected == 0):
                hermiteCurve.controlPointHandler.DotSelected(dot_select)
                nurbsCurve.controlPointHandler.DotSelected(None)
            else:
                nurbsCurve.controlPointHandler.DotSelected(dot_select)
                hermiteCurve.controlPointHandler.DotSelected(None)
            
            screen.fill(Colors.WHITE)

            jointCurveHandler.Draw(pygame, screen, 2, [nurbsColor, hermiteColor], total_points)

    if(pygame.mouse.get_pressed()[0]):
        mouse_pos = pygame.mouse.get_pos()

        if(curve_selected == 0):
            hermiteCurve.controlPointHandler.MouseClick(mouse_pos[0], mouse_pos[1], dot_select)
        else:
            nurbsCurve.controlPointHandler.MouseClick(mouse_pos[0], mouse_pos[1], dot_select)
        
        screen.fill(Colors.WHITE)

        jointCurveHandler.Draw(pygame, screen, 2, [nurbsColor, hermiteColor], total_points)

    # update the screen
    pygame.display.update()