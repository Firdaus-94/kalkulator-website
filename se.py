# Note: mobile turtle implementation does not support animation
# You can't see the turtle moving on the screen
# The following code will draw the final result directly

from turtle import *

for i in range(6):
    circle(100)
    right(60)
dot(10, 'green')

done()  # must call done() to show the image
