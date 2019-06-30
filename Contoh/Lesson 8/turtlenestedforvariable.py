import turtle
nbrSides = 6
for i in range(nbrSides):
    turtle.forward(100)
    turtle.right(360/nbrSides)
    for n in range(nbrSides):
        turtle.forward(50)
        turtle.right(360/nbrSides)