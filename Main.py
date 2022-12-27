from functi import *
import random


tu.setworldcoordinates(0,-ws,ws,0)
createBoard()

tu.color('white')
tu.width(3)

scr.setup(1.0,1.0)
scr.bgcolor("black")

tu.hideturtle()
tu.tracer(False)

scr.onclick(click)
scr.onkey(qu,'q')
tu.listen()
tu.mainloop()



# credit to _____ for convo png to pixels
