"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Emily Wilcox.
"""
########################################################################
# Done: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# Done: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################
import rosegraphics as rg
window = rg.TurtleWindow()

harry = rg.SimpleTurtle('circle')
harry.speed = 10
for k in range(20):
    harry.forward(200)
    harry.left(28)
    harry.forward(20)
    harry.left(90)
    harry.forward(200)
    harry.forward(k)

gary = rg.SimpleTurtle('turtle')
gary.pen = rg.Pen('blue', 5)
gary.speed = 5
for i in range(25):
    gary.forward(60)
    gary.right(40)
    gary.forward(100)
    gary.left(20)
    gary.forward(50)
    gary.left(i)

window.close_on_mouse_click()
