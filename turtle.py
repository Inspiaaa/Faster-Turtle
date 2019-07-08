
import math
from renderer_base import RendererBase


class Turtle:
    """
    This is a faster turtle implementation than the built in turtle implementation
    """

    def __init__(self):
        self._x = 0
        self._y = 0
        self._angle = 0

        self._min_x = 0
        self._max_x = 0
        self._min_y = 0
        self._max_y = 0

        self._lines = []
        self._poly_lines = []
        self._widths = []
        self._colours = []
        self._fill_colours = []

        self._width = 1
        self._colour = (0, 0, 0, 255)
        self._fill_colour = (0, 0, 0, 255)
        self._state = False
        self._is_poly = False

    def render(self, renderer: RendererBase, auto_scale=True, auto_offset=True, auto_margin=0.1, flush=True):
        """
        Renders the line and polygons using the given renderer

        :param renderer: The renderer object extending RendererBase, used to render the lines and polygons
        :param auto_scale: If true, automatically scald the turtle's drawing to fit the canvas size
        :param auto_offset: If true, automatically places the turtle's drawing in the center of the canvas
        :param auto_margin: The margin to the edge of the renderer's canvas for auto_scale
        :param flush: If true, the existing line and polygon data will be deleted
        """

        w = self._max_x - self._min_x
        h = self._max_y - self._min_y

        scale = min((renderer.size[0] * (1.0 - auto_margin)) / w, (renderer.size[1] * (1.0 - auto_margin)) / h)

        screen_center_x = renderer.size[0] / 2
        screen_center_y = renderer.size[1] / 2

        real_center_x = (self._max_x - (w / 2))
        real_center_y = (self._max_y - (h / 2))

        if auto_scale:
            renderer.setup_scale(scale)
            real_center_x *= scale
            real_center_y *= scale
        if auto_offset:
            offset_x = screen_center_x - real_center_x
            offset_y = screen_center_y - real_center_y
            renderer.setup_offset(offset_x, offset_y)

        renderer.draw_polygons(self._poly_lines, self._fill_colours)
        renderer.draw_lines(self._lines, self._widths, self._colours)

        if flush:
            self._lines = []
            self._widths = []
            self._colours = []
            self._poly_lines = []
            self._fill_colours = []

    def _draw(self, distance):
        """
        Draws a line while moving forward

        :param distance: The distance to move forward
        """

        x0 = self._x
        y0 = self._y
        self._move(distance)
        self._add_line(x0, y0)

    def _check_minmax(self):
        """
        Checks the minimum and maxiumum x, y coordinates to enable auto_offset and auto_scale later
        """

        if self._x - self._width * 0.5 < self._min_x:
            self._min_x = self._x - self._width * 0.5
        elif self._x + self._width * 0.5 > self._max_x:
            self._max_x = self._x + self._width * 0.5

        if self._y - self._width * 0.5< self._min_y:
            self._min_y = self._y - self._width * 0.5
        elif self._y + self._width * 0.5 > self._max_y:
            self._max_y = self._y + self._width * 0.5

    def _add_line(self, x0, y0):
        """
        Adds another drawn line

        :param x0: The starting x coordinate
        :param y0: The starting y coordinate
        """

        self._check_minmax()
        self._lines.append((x0, y0, self._x, self._y))
        self._widths.append(int(self._width))
        self._colours.append(self._colour)

    def _add_poly(self):
        """
        Adds another point to the current polygon
        """

        if not self._state:
            self._check_minmax()

        self._poly_lines[-1].append((self._x, self._y))

    def _move(self, distance):
        self._x -= math.cos(self._angle * 0.01745329251) * distance
        self._y -= math.sin(self._angle * 0.01745329251) * distance

    def _int4_tuple(self, t, v0, v1, v2, v3):
        return tuple([int(v) for v in t + (v0, v1, v2, v3)[:4-len(t)]])

    def forward(self, distance):
        """
        Moves the turtle forward

        :param distance: The distance to move forward
        """

        if self._state:
            self._draw(distance)
        else:
            self._move(distance)

        if self._is_poly:
            self._add_poly()

    def backward(self, distance):
        """
        Moves the turtle backward

        :param distance: The distance to move backward
        """

        if self._state or self._is_poly:
            self._draw(- distance)
        else:
            self._move(- distance)

        if self._is_poly:
            self._add_poly()

    def pendown(self):
        """
        Begins the drawing of lines with the turtle's width and colour
        """

        self._state = True

    def penup(self):
        """
        Ends the drawing of lines
        """

        self._state = False

    def begin_poly(self):
        """
        Begins the drawing of a polygon with the turtle's fillcolour
        """

        self._is_poly = True
        self._poly_lines.append([])
        self._poly_lines[-1].append((self._x, self._y))

    def end_poly(self):
        """
        Ends the drawing of the polygon
        """

        self._is_poly = False
        self._fill_colours.append(self._fill_colour)

    def right(self, angle):
        """
        Turns the turtle right

        :param angle: The angle to turn right
        """

        self._angle += angle

    def left(self, angle):
        """
        Turns the turtle left

        :param angle: The angle to turn left
        """

        self._angle -= angle

    def get_heading(self):
        """
        Returns the heading of the turtle

        :return: Float angle of turtle
        """

        return self._angle

    def get_position(self):
        """
        Returns the x, y coordinates of the turtle

        :return: Tuple XY
        """

        return self._x, self._y

    def set_heading(self, angle):
        """
        Directly sets the heading of the turtle

        :param angle: The new heading angle
        """

        self._angle = angle

    def pencolour(self, r, g=0, b=0, a=255):
        """
        Sets the colour of the line drawn by the turtle

        :param r: Either a tuple of RGBA, or the red value
        :param g: The green value
        :param b: The blue value
        :param a: The alpha value
        """

        if isinstance(r, tuple):
            self._colour = self._int4_tuple(r, 0, g, b, a)
        else:
            self._colour = (r, g, b, a)

    def fill(self, r, g=0, b=0, a=255):
        """
        Sets the fill colour of the polygon drawn by the turtle

        :param r: Either a tuple of RGBA, or the red value
        :param g: The green value
        :param b: The blue value
        :param a: The alpha value
        """

        if isinstance(r, tuple):
            self._fill_colour = r
        else:
            self._fill_colour = (r, g, b, a)

    def set_position(self, pos, y=None):
        """
        Directly sets the position of the turtle (with drawing a line if the pen is down)

        :param pos: Either a tuple of XY, or the new x value
        :param y: The new y value
        """

        x0 = self._x
        y0 = self._y

        if isinstance(pos, tuple):
            self._x = pos[0]
            self._y = pos[1]
        else:
            self._x = pos
            self._y = y

        if self._state:
            self._add_line(x0, y0)
        if self._is_poly:
            self._add_poly()

    def goto(self, pos, y=None):
        """
        Same as Turtle.set_position
        """

        self.set_position(pos, y)

    def set_x(self, x):
        """
        Directly sets the x coordinate of the turtle (with drawing a line if the pen is down)

        :param x: The new x coordinate
        """

        x0 = self._x

        self._x = x
        if self._state:
            self._add_line(x0, self._y)
        if self._is_poly:
            self._add_poly()

    def set_y(self, y):
        """
        Directly sets the y coordinate of the turtle (with drawing a line if the pen is down)

        :param y: The new y coordinate
        """

        y0 = self._y

        self._y = y
        if self._state:
            self._add_line(self._x, y0)
        if self._is_poly:
            self._add_poly()

    def pensize(self, size):
        """
        Sets the pen size (/ width) of the turtle

        :param size: The new size
        """

        self._width = size

    def get_size(self):
        """
        Returns the size of the turtle's pen
        """
        return self._width

    def get_colour(self):
        """
        Returns the turtle's pen colour

        :return: Tuple RGBA
        """

        return self._colour

    def get_fill(self):
        """
        Returns the turtle's fill colour for polygons

        :return: Tuple RGBA
        """

        return self._fill_colour
