from .Line import Line, LineCollection
from .Point import Point
from .Common import Colors, ScreenDimensions

class XYAxes:
    def __init__(self, origin_x, origin_y, unit_size):
        self.lineCollection = LineCollection()
        self.origin_x = origin_x
        self.origin_y = origin_y
        self.unit_size = unit_size
        self.axes_color = Colors.BLACK
        self.axes_cross_color = Colors.RED

        # Horizontal Line
        self.lineCollection.add(
            Line(
                Point(-ScreenDimensions.WIDTH, origin_y),
                Point(ScreenDimensions.WIDTH, origin_y),
                2,
                self.axes_color
            )
        )

        axesCrossLineSize = unit_size // 2
        for i in range(unit_size, ScreenDimensions.WIDTH + unit_size, unit_size):
            self.lineCollection.add(
                Line(
                    Point(origin_x + i, origin_y - axesCrossLineSize),
                    Point(origin_x + i, origin_y + axesCrossLineSize),
                    1,
                    self.axes_cross_color
                )
            )
            self.lineCollection.add(
                Line(
                    Point(origin_x - i, origin_y - axesCrossLineSize),
                    Point(origin_x - i, origin_y + axesCrossLineSize),
                    1,
                    self.axes_cross_color
                )
            )

        # Vertical Line
        self.lineCollection.add(
            Line(
                Point(origin_x, -ScreenDimensions.HEIGH),
                Point(origin_x, ScreenDimensions.HEIGH),
                2,
                self.axes_color
            )
        )

        axesCrossLineSize = unit_size // 2
        for j in range(unit_size, ScreenDimensions.HEIGH + unit_size, unit_size):
            self.lineCollection.add(
                Line(
                    Point(origin_x - axesCrossLineSize, origin_y + j),
                    Point(origin_x + axesCrossLineSize, origin_y + j),
                    1,
                    self.axes_cross_color
                )
            )
            self.lineCollection.add(
                Line(
                    Point(origin_x - axesCrossLineSize, origin_y - j),
                    Point(origin_x + axesCrossLineSize, origin_y - j),
                    1,
                    self.axes_cross_color
                )
            )
    
    def draw(self, pygame, screen):
        self.lineCollection.draw(pygame, screen)