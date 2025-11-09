from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self._root = Tk()
        self._root.title("Box Mover")
        self._canvas = Canvas(self._root, bg="white", height=height, width=width)
        self._canvas.pack(fill=BOTH, expand=1)
        self._running = False
        self._root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self._root.update_idletasks
        self._root.update()
    
    def wait_for_close(self):
        self._running = True
        while self._running == True:
            self.redraw()
        print("window closed...")

    def draw_line(self, line, fill_color="black"):
        line.draw(self._canvas, fill_color)

    def close(self):
        self._running = False


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas, fill_color="black"):
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2)    


class Cell:
    def __init__(self, win=None, type="VOID"):
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._win = win
        self.type = type

    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

        p1 = Point(x1, y1)     #top left
        p2 = Point(x2, y1)     #top right
        p3 = Point(x1, y2)     #bottom left
        p4 = Point(x2, y2)     #bottom rigt

        self._win.draw_line(Line(p1, p2))        #top line
        self._win.draw_line(Line(p3, p4))        #bottom line
        self._win.draw_line(Line(p1, p3))        #left line
        self._win.draw_line(Line(p2, p4))        #right line

        #to do add filling/sprite
