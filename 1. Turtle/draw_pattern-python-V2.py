import turtle

tor = turtle.Turtle()

def draw_square():
                        
                    tor.color("green")
                    tor.shape("square")
                    tor.speed(5)
                    
                    i = 0
                    while i < 4:
                    
                                tor.forward(150)
                                tor.left(90)
                                i+=1
window = turtle.Screen()
window.bgcolor("black")

for i in range(0,36):
                        draw_square()
                        tor.right(10)
                        
                        #36 * 10 = 360
                        #Need to turn 10 degreed 36 times to draw a complete circle
                        
window.exitonclick()