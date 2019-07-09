# Faster Turtle
Faster Turtle is another turtle implementation written in pure Python. As its name indicates, it is faster than Python's default turtle implementation. Although Python's default one is better for real-time and learning, Faster Turtle offers incredible performance for rendering.

## Same as Python's Turtle
```Python
from turtle import Turtle
from random import randint
from pil_renderer import PILRenderer

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
```

The only noticeable difference is that the turtle uses an external renderer to produce the result:

![enter image description here](https://raw.githubusercontent.com/LavaAfterburner/Faster-Turtle/master/Example%20Images/E2.png)
