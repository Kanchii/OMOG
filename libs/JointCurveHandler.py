from .ComplexCurves import NURBSCurve, HermiteCurve
from .Common import Colors
from .Point import Point

import math

class JointCurveHandler:
    def __init__(self, nurbsCurve: NURBSCurve, hermiteCurve: HermiteCurve):
        self.nurbsCurve = nurbsCurve
        self.hermiteCurve = hermiteCurve
    
    def G0_C0(self):
        hermite_last_point = self.hermiteCurve.p_end
        nurbs_last_point = self.nurbsCurve.control_points[0]

        # Calculando o deslocamento que a curva de Hermite terá q fazer
        desloc = Point(nurbs_last_point.x - hermite_last_point.x, nurbs_last_point.y - hermite_last_point.y)

        # Movendo a curva de Hermite
        self.hermiteCurve.p_start = self.hermiteCurve.p_start.sum(desloc)
        self.hermiteCurve.p_end = self.hermiteCurve.p_end.sum(desloc)

    def G1(self):
        self.G0_C0()
        # Pegando a reta tangente do começo da curva de NURBS
        nurbs_tangent = self.nurbsCurve.control_points[0].vet(self.nurbsCurve.control_points[1])

        self.hermiteCurve.v_end = nurbs_tangent

    def C1(self):
        self.G1()

    def draw(self, pygame, screen, thickness, colors: [Colors], number_points):
        self.C1()
        
        self.nurbsCurve.GenerateCurve(number_points)
        self.hermiteCurve.GenerateCurve(number_points)

        self.nurbsCurve.Draw(pygame, screen, thickness, colors[0], True)
        self.hermiteCurve.Draw(pygame, screen, thickness, colors[1])
        