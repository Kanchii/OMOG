from .ComplexCurves import NURBSCurve, HermiteCurve
from .Common import Colors
from .Point import Point
from .ControlPoint import *

import math

class JointCurveHandler:
    def __init__(self, nurbsCurve: NURBSCurve, hermiteCurve: HermiteCurve):
        self.nurbsCurve = nurbsCurve
        self.hermiteCurve = hermiteCurve
    
    def G0_C0(self):
        hermite_last_point = self.hermiteCurve.controlPointHandler.getValue(2)
        nurbs_last_point = self.nurbsCurve.controlPointHandler.getValue(0)

        # Calculando o deslocamento que a curva de Hermite terá q fazer
        desloc = hermite_last_point.vet(nurbs_last_point)

        print(desloc)

        # Movendo a curva de Hermite
        self.hermiteCurve.controlPointHandler.desloc(desloc)

    def G1(self):
        self.G0_C0()

        hermite_vector = self.hermiteCurve.controlPointHandler.getValue(3).vet(self.hermiteCurve.controlPointHandler.getValue(2))

        nurbs_second_control_point = self.nurbsCurve.controlPointHandler.getValue(0).sum(hermite_vector)

        # self.hermiteCurve.v_end = nurbs_tangent
        control_point_ant = self.nurbsCurve.controlPointHandler.control_points[1]
        # print(control_point_ant, nurbs_second_control_point, hermite_vector)
        self.nurbsCurve.controlPointHandler.control_points[1] = ControlPoint(nurbs_second_control_point.x,
                        nurbs_second_control_point.y,                        
                        control_point_ant.radius,
                        control_point_ant.number,
                        control_point_ant.weight,
                        control_point_ant.terminal)  

    def C1(self):
        self.G1()

    def Draw(self, pygame, screen, thickness, colors: [Colors], number_points):
        self.G0_C0()
        
        self.nurbsCurve.Draw(pygame, screen, thickness, colors[0], number_points)
        self.hermiteCurve.Draw(pygame, screen, thickness, colors[1], number_points)
        