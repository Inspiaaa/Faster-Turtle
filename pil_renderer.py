from renderer_base import RendererBase
from PIL import Image, ImageDraw, ImageTk
import tkinter as tk


class PILRenderer (RendererBase):
    def __init__(self, size=(1000, 1000), bg=(255, 255, 255, 255)):
        super(PILRenderer, self).__init__(size, bg)

        self.im = Image.new("RGBA", self.size, bg)
        self.draw = ImageDraw.Draw(self.im)

    def draw_line(self, position, width, colour, round_cap=True):
        width *= self.scale
        width = int(width)
        self.draw.line(
            self.to_line(position),
            fill=colour,
            width=width)

        if round_cap and width > 2:
            start = self.to_pos_xy(position[0], position[1])
            end = self.to_pos_xy(position[2], position[3])
            radius = width / 2

            self.draw.ellipse(
                (_add2(start, (-radius, -radius)),
                 _add2(start, (radius, radius))),
                fill=colour)

            self.draw.ellipse(
                (_add2(end, (-radius, -radius)),
                 _add2(end, (radius, radius))),
                fill=colour)

    def draw_polygon(self, positions, colour):
        points = [self.to_pos(pos) for pos in positions]
        self.draw.polygon(points, fill=colour, outline=(0, 0, 0, 0))

    def show(self, size=(500, 500)):
        window = tk.Tk()
        window.title("Turtle Rendering")
        window.geometry(f"{size[0]}x{size[1]}")
        resized = self.im.resize(size, Image.ANTIALIAS)
        img = ImageTk.PhotoImage(resized)
        tk.Label(window, image=img).pack()
        window.mainloop()

    def save(self, path, format="PNG"):
        self.im.save(path, format)


def _add2(t, t2):
    return (t[0] + t2[0], t[1] + t2[1])
