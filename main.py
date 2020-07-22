import turtle

turtle.title("My Turtle Game")
turtle. bgcolor("blue")
turtle.setup(600,600)
turtle.shape("turtle")

screen = turtle.Screen()
bob = turtle.Turtle()

def Triangle(Length, color):
  bob.fillcolor(color)
  bob.begin_fill()
  x=0
  while x < 3:
    bob.forward(int(Length))
    bob.right(120)
    x+=1
  bob.end_fill()

def Circle(Length, color):
  bob.fillcolor(color)
  bob.begin_fill()
  x=0
  while x < 5:
    bob.forward(int(Length))
    bob.right(360)
    x+=1
  bob.end_fill()

input_shape = input("What shape do you want to draw? ")
input_length = input ("Choose how big: ")
input_color = input("Choose Color: ")

if input_shape == "Triangle":
  Triangle(input_length, input_color)
elif input_shape == "Circle":
  Circle(input_length, input_color)
else:
  print("Star")

