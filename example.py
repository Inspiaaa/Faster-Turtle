from pil_renderer import PILRenderer
from turtle import Turtle
from random import randint


def get_gradient(d0, d1, steps):
    r0 = d0[1][0]
    g0 = d0[1][1]
    b0 = d0[1][2]
    a0 = d0[1][3]
    s0 = d0[0]

    r1 = d1[1][0]
    g1 = d1[1][1]
    b1 = d1[1][2]
    a1 = d1[1][3]
    s1 = d1[0]

    dr = (r1 - r0) / steps
    dg = (g1 - g0) / steps
    db = (b1 - b0) / steps
    da = (a1 - a0) / steps
    ds = (s1 - s0) / steps

    cr = r0
    cg = g0
    cb = b0
    ca = a0
    cs = s0

    data = []

    for i in range(steps):
        data.append((int(cs), (int(cr), int(cg), int(cb), int(ca))))
        cs += ds
        cr += dr
        cg += dg
        cb += db
        ca += da

    return data


if __name__ == '__main__':
    t = Turtle()

    # Generate the island
    distances = []
    angles = []
    iterations = 500
    for i in range(iterations):
        distances.append(randint(1, 50))
        angles.append(randint(-180, 180))

    layers = []
    layers.extend(get_gradient((300, (0, 140, 225, 255)), (150, (0, 180, 225, 255)), 10))
    layers.extend(get_gradient((100, (255, 250, 60, 255)), (50, (220, 200, 60, 255)), 10))
    layers.extend(get_gradient((50, (150, 200, 0, 255)), (30, (100, 200, 20, 255)), 10))

    for layer in layers:
        t.pensize(layer[0])
        t.pencolour(layer[1])

        t.pendown()
        for i in range(iterations):
            t.forward(distances[i])
            t.right(angles[i])
        t.penup()
        t.goto(0, 0)
        t.set_heading(0)

    renderer = PILRenderer(bg=(0, 140, 225, 255))
    t.render(renderer)
    renderer.show()
