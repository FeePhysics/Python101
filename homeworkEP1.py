import turtle
tao = turtle.Pen()
tao.shape('turtle')
tao.penup()
tao.goto(0,0)
tao.pendown()
for j in range (5):
    for i in range (360):
        tao.forward(2+j)
        tao.left(1)
    for i in range (360):    
        tao.forward(2+j)
        tao.right(1) 
    
          

