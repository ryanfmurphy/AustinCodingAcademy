Drawing With Python
-------------------

In today's warmup we'll be using the `turtle` module to explore some simple programming and geometry concepts.

The `turtle` is a virtual on-screen "robot" that you can control with Python commands.  This Python module is inspired by an older programming language [Logo](http://en.wikipedia.org/wiki/Logo_(programming_language)#Turtle_and_graphics) that was commonly used to teach programming.

*Note: You cannot do this in your VM.  You must use Python on your own local computer.*

When you `import turtle` it opens up a graphics window with a little "cursor" in the middle of the screen, pointing right - that's the "turtle".  You can move control which direction the turtle points and tell it to move forward and backwards.

### Example ###

```python
from turtle import * # load turtle stuff
forward(20)          # go forward 20 pixels
right(45)            # turn right 45 degrees
forward(100)         # go forward 100 pixels

# if you want to reset:
clear()              # clear the screen
goto(0,0)            # send turtle back to center
setheading(0)        # go back to default angle
```

### Exercises ###

* Figure out how to draw a square with the turle.
* Instead of a square, how would you draw an octagon?  How about a circle?

### Bonus ###

* How could you draw a bigger circle?  A smaller circle?
* Instead of a circle, how would you draw a spiral?

