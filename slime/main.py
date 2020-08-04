import turtle
import time
import random
import signal
import sys

def quit():
	print("Bye...")
    sys.exit(0)

def run():
	screen=turtle.Screen()
	screen.addshape("resources/blaze.gif")
	screen.addshape("resources/blazeUp.gif")
	screen.addshape("resources/blazeLeft.gif")
	screen.addshape("resources/blazeRight.gif")

	blaze=turtle.Turtle()
	blaze.penup()
	blaze.shape("resources/blaze.gif")


	def up():
		y=blaze.ycor()
		blaze.sety(y+10)
		blaze.shape("resources/blazeUp.gif")

	def down():
		y=blaze.ycor()
		blaze.sety(y-10)	
		blaze.shape("resources/blaze.gif")

	def left():
		x=blaze.xcor()
		blaze.setx(x-10)
		blaze.shape("resources/blazeLeft.gif")

	def right():
		x=blaze.xcor()
		blaze.setx(x+10)					
		blaze.shape("resources/blazeRight.gif")

	screen.onkey(up, "Up")
	screen.onkey(down, "Down")
	screen.onkey(left, "Left")	
	screen.onkey(right, "Right")
	screen.onkey(quit, "Q")

	screen.listen()		
	turtle.mainloop()