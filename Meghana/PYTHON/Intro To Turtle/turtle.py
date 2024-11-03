import turtle
turtle.Screen().bgcolor("blue")
src.title("Welcome To The Python Turtle")
src.setup(350,350)

board = turtle.Turtle()

for i in range(4):
    board.forward(100)
    board.right(90)
    i=i+1

turtle.done()