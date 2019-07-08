
class RendererBase:
    def __init__(self, size=(1000, 1000), bg=(255, 255, 255, 255)):
        self.size = size
        self.offset_x = 0
        self.offset_y = 0
        self.scale = 1

    def draw_line(self, position, width, colour) -> None:
        pass

    def draw_lines(self, positions, widths, colours) -> None:
        for i in range(len(positions)):
            self.draw_line(positions[i], widths[i], colours[i])

    def draw_polygon(self, positions, colour) -> None:
        pass

    def draw_polygons(self, polygons, colours) -> None:
        for i in range(len(polygons)):
            self.draw_polygon(polygons[i], colours[i])

    def clear(self):
        pass

    def setup_offset(self, x, y):
        self.offset_x = x
        self.offset_y = y

    def setup_scale(self, scale):
        self.scale = scale

    def save(self, path, format="PNG") -> None:
        pass

    def show(self, size=(500, 500)) -> None:
        pass

    def to_pos(self, t):
        return (t[0] * self.scale + self.offset_x,
                t[1] * self.scale + self.offset_y)

    def to_pos_xy(self, x, y):
        return (x * self.scale + self.offset_x,
                y * self.scale + self.offset_y)

    def to_line(self, t):
        return (self.to_pos_xy(t[0], t[1]),
                self.to_pos_xy(t[2], t[3]))
