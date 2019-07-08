from pil_renderer import PILRenderer
from turtle import Turtle
from random import randint


def run_1():
    t = Turtle()

    t.pendown()
    t.fill(255, 165, 0)
    t.begin_poly()

    for i in range(40):
        t.right(25)
        t.forward(100)
        t.left(160)
        t.forward(25)

    t.end_poly()

    renderer = PILRenderer()
    t.render(renderer)
    renderer.show()


def run_2():
    t = Turtle()

    t.pendown()

    for i in range(18):
        t.begin_poly()
        t.fill(randint(100, 255), 0, randint(100, 255))

        t.forward(25)
        t.right(15)
        t.forward(25)
        t.right(165)
        t.forward(25)
        t.right(15)
        t.forward(25)

        t.right(25)
        t.end_poly()

    renderer = PILRenderer()
    t.render(renderer)
    renderer.show()


def run_3():
    t = Turtle()
    t.pendown()
    t.pencolour(255, 0, 0)

    for i in range(100000):
        t.right(randint(-90, 90))
        t.forward(randint(0, 5))

    renderer = PILRenderer()
    t.render(renderer)
    renderer.show()


if __name__ == '__main__':
    run_1()
    run_2()
    run_3()
