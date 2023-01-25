# Student name: Minhui Roh
# McGill ID: 261120462
import turtle

def lightning():
    """ () -> NoneType
    Returns nothing and takes no input.
    Using turtle module, it draws lightning when it is called.
    """
    l = turtle.Turtle()
    l.speed("fastest")
    l.hideturtle()
    x_coordinate=-180
    for i in range(3):
        l.penup()
        l.goto(x_coordinate,300)
        l.pendown()
        l.fillcolor("yellow")
        l.begin_fill()
        for i in range(2):
            l.right(110)
            l.forward(50)
            l.left(110)
            l.forward(25)
        l.right(110)
        l.forward(50)
        l.left(160)
        l.forward(90)
        l.left(130)
        l.forward(30)
        l.right(110)
        l.forward(40)
        l.left(110)
        l.forward(30)
        l.right(110)
        l.forward(38)
        l.left(110)
        l.forward(23)
        l.end_fill()
        l.right(180)
        x_coordinate+=180
        
def raindrop(length,radius):
    """ (num,num) -> NoneType
    Takes two numbers which will determine
    the side length and the radius of a raindrop.
    Using turtle module, draws the raindrop.
    Returns nothing.
    """
    x_coordinate=-220
    y_coordinate=50
    for i in range (4):
        r = turtle.Turtle()
        r.speed("fastest")
        r.hideturtle()
        r.penup()
        r.goto(x_coordinate,y_coordinate)
        r.pendown()
        r.hideturtle()
        r.fillcolor("aquamarine")
        r.begin_fill()
        r.right(110)
        r.forward(length)
        r.left(20)
        r.circle(radius,180)
        r.left(20)
        r.forward(length)
        r.end_fill()
        if x_coordinate==-170: 
            x_coordinate+=350
            y_coordinate+=50
        else:
            x_coordinate+=50
            y_coordinate-=50
    

def my_artwork():
    """ () -> NoneType
    Returns nothing and takes no input.
    It draws my chosen shapes using turtle module.
    """
    flag = turtle.Turtle()
    flag.speed("fastest")
    flag.hideturtle()
    flag.right(180)
    flag.forward(100)
    flag.left(70)
    flag.fillcolor("blue")
    flag.begin_fill()
    flag.circle(120,180)
    flag.end_fill()
    flag.fillcolor("red")
    flag.begin_fill()
    flag.circle(120,180)
    flag.end_fill()
    flag.pendown()
    flag.fillcolor("red")
    flag.begin_fill()
    flag.circle(60,180)
    flag.right(180)
    flag.end_fill()
    flag.penup()
    flag.circle(60,180)
    flag.pendown()
    flag.fillcolor("blue")
    flag.begin_fill()
    flag.circle(60,180)
    flag.end_fill()
    
    lightning()
    raindrop(90,31)
    
    flag.penup()
    flag.goto(250,-200)
    flag.pendown()
    flag.right(180)
    flag.forward(50)
    flag.right(140)
    flag.forward(50)
    flag.left(140)
    flag.forward(50)
    flag.right(140)
    flag.forward(50)
    
    



    
    
    
    


    

