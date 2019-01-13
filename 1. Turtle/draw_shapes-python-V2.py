import turtle

tor = turtle.Turtle()
mor = turtle.Turtle()
bor = turtle.Turtle()

def draw_square():
                    
                    tor.color("green")
                    tor.shape("square")
                    tor.speed(5)
                    
                    i = 0
                    while i < 4:
                    
                                tor.forward(150)
                                tor.left(90)
                                i+=1
                                
def draw_circle():
                    
                    mor.color("red")
                    mor.shape("circle")
                    mor.circle(150)

def draw_triangle():

                    bor.color("blue")
                    bor.shape("triangle")
                    
                    """
                    Sum of all angles of triangle is 180
                    But if we were to draw each angle of 60 internally,
                    We'll have to turn 180 - 60 = 120 degrees externally
                    """
                    i = 0
                    while i < 3:
                    
                                bor.forward(150)
                                bor.left(120)    #Makes 60 degree angle internally
                                i+=1
                                
window = turtle.Screen()
window.bgcolor("black")

draw_square()
draw_circle()
draw_triangle()

window.exitonclick()