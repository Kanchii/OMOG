from .Common import Colors

class Line:
    def __init__(self, start_pos, end_pos, thickness, color = Colors.BLACK):
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.thickness = thickness
        self.color = color
    
    def __str__(self):
        return "{} -> {}".format(self.start_pos, self.end_pos)

    def draw(self, pygame, screen, color):
        _color = self.color if color == None else color
        pygame.draw.line(screen, _color, self.start_pos.toTuple(), self.end_pos.toTuple(), self.thickness)

class LineCollection:
    def __init__(self, lines: [Line] = []):
        self.lines: [Line] = lines
    
    def draw(self, pygame, screen, color = None):
        if(self.lines == []):
            return
        for line in self.lines:
            line.draw(pygame, screen, color)
        
    def add(self, line):
        self.lines.append(line)