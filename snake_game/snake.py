# Lucas Chang, Aaron Jackson

# import required modules
import random
import turtle
import time

delay = 0.1 #TODO change this. what does it do?
score = 0
high_score = 0

# Creating a window screen
screen = turtle.Screen()
screen.title("Snake Game") # TODO put a name in the parenthesis
screen.bgcolor('black') #TODO you need to add a color inside parenthesis
# the width and height can be put as user's choice
screen.setup(width=600, height=600) 
#TODO: modify this, and use the input function to ask the user what size they want. 
# save those values and set it to the size of the window
screen.tracer(0)



# head of the snake
head = turtle.Turtle()
head.shape('square')  #TODO pick a shape for the head
head.color('red')     #TODO pick a color for the head
head.penup()
head.goto(0, 0)
head.direction = "Stop"

# food in the game
food = turtle.Turtle()
# TODO make an array of 5 colors and randomly pick one. make sure it doesn't blend into your background
colors = random.choice({'blue', 'green', 'yellow'})#TODO random choice from your list.
shapes = random.choice(['square', 'triangle', 'circle'])
food.speed(0)
food.shape(shapes)
food.color(colors)
food.penup()
x = random.randinit(0,600)
y = random.randinit(0,600)
food.goto(random.randinit(0,600), random.randinit(0,600)) #TODO: replace x,y with numerical coordinate points

pen = turtle.Turtle()
pen.speed(0)
pen.shape()
pen.color()
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
#TODO write score
pen.write("score: {} high score: {}".format(score,high_score))


# assigning key directions
# TODO: key directions for going up and down
def goup():
	if head.direction != "down":
		head.direction = "up"

def godown():
	if head.direction != "up":
		head.direction = "down"

def goleft():
	if head.direction != "right":
		head.direction = "left"

def goright():
	if head.direction != "left":
		head.direction = "right"


def move():
	if head.direction == "up":
		y = head.ycor()
        y += 10
        # TODO: what do we do after getting the coordinate? what does it mean to go up?
	if head.direction == "down":
            y = head.ycor()
            y -= 10
        # TODO: get coordinate and move down
	if head.direction == "left":
             x = head.xcor()
             x -= 10
        # TODO: get coordinate and move left

	if head.direction == "right":
            x = head.xcor()
            x+= 10
	        # TODO: get coordinate and move right



		
screen.listen()

#TODO: call the funscreen.onkeypress(goup, "w")ctions on key press. example below, make sure you go left right and down.
screen.onkeypress(goup, "w")
screen.onkeypress(godown, "s")
screen.onkeypress(goleft, "a")
screen.onkeypress(goright, "d")


segments = []



# Main Gameplay 
while True:

    #check collision with board
    if(head.xcor()>600 or head.xcor() < 0 or head.ycor()>600 or head.ycor()<0):

        #restart beginning position
        head.goto(0,0)
        head.direction = "Stop"

        #restart time

        #restart score
        score = 0

        #rewrite score
        pen.clear()
        pen.write("score: {} high score: {}".format(score,high_score))

        #food
        if head.distance(food) == 0:
            x = random.randinit(0,600)
            y = random.randinit(0,600)
            food.goto(x ,y)
            score += 10

    #TODO: make the code for the main game iteration, and make sure you call your functions. have the snake move random

screen.mainloop()

snake.py
Displaying snake.py.