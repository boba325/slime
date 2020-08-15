import turtle
import time
import random
import signal
import sys

class WatchedKey:
    def __init__(self, key):
        self.key = key
        self.pressed = False
        turtle.onkeypress(self.press, key)
        turtle.onkeyrelease(self.release, key)

    def press(self):
        self.pressed = True

    def release(self):
        self.pressed = False

def quit():
    print("Bye...")
    sys.exit(0)

def run():
    screen=turtle.Screen()
    screen.addshape("resources/blaze.gif")
    screen.addshape("resources/blazeUp.gif")
    screen.addshape("resources/blazeLeft.gif")
    screen.addshape("resources/blazeRight.gif")
    screen.addshape("resources/eye.gif")
    screen.addshape("resources/eyeClosed.gif")
    screen.addshape("resources/eyeExp-3.gif")
    screen.setup(800, 800)

    n=1
    eyes = []

    blaze=turtle.Turtle()
    blaze.penup()
    blaze.shape("resources/blaze.gif")

    eyeShot=turtle.Turtle()
    eyeShot.penup()
    eyeShot.shape("resources/eyeExp-3.gif")

    up = WatchedKey("Up")
    down = WatchedKey("Down")
    left = WatchedKey("Left")  
    right = WatchedKey("Right")

    # def up():
    #     y=blaze.ycor()
    #     blaze.sety(y+10)
    #     blaze.shape("resources/blazeUp.gif")

    # def down():
    #     y=blaze.ycor()
    #     blaze.sety(y-10)    
    #     blaze.shape("resources/blaze.gif")

    # def left():
    #     x=blaze.xcor()
    #     blaze.setx(x-10)
    #     blaze.shape("resources/blazeLeft.gif")

    # def right():
    #     x=blaze.xcor()
    #     blaze.setx(x+10)                    
    #     blaze.shape("resources/blazeRight.gif")

    def move():
        y=blaze.ycor()
        x=blaze.xcor()
        if up.pressed:
            blaze.sety(y+10)
            blaze.shape("resources/blazeUp.gif")
        if down.pressed:
            blaze.sety(y-10)
            blaze.shape("resources/blaze.gif")
        if left.pressed:
            blaze.setx(x-10)
            blaze.shape("resources/blazeLeft.gif")
        if right.pressed:
            blaze.setx(x+10) 
            blaze.shape("resources/blazeRight.gif")
        screen.ontimer(move, 10)

    def follow():
        direction = eyeShot.towards(blaze)
        eyeShot.setheading(direction)
        eyeShot.forward(5)
        screen.ontimer(follow, 10)

    for i in range(n):
        eye=turtle.Turtle()
        eye.penup()
        eye.shape("resources/eye.gif")
        eyes.append(eye)

    # screen.onkey(up, "Up")
    # screen.onkey(down, "Down")
    # screen.onkey(left, "Left")  
    # screen.onkey(right, "Right")
    screen.onkey(quit, "Q")

    move()
    follow()

    screen.listen()     
    turtle.mainloop()