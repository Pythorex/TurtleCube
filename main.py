import turtle

pointtop1 = (-20,20)
pointtop2 = (20,20)
pointtop3 = (0,0)
pointtop4 = (-40,0)

pointbottommid = (0,-30)
pointbottomleft = (-40,-30)
pointbottomright = (20,-10)



turtle.penup()
turtle.goto(pointtop1)
turtle.pendown()
turtle.goto(pointtop2)
turtle.goto(pointtop3)
turtle.goto(pointtop4)
turtle.goto(pointtop1)
turtle.penup()
turtle.goto(pointtop3)
turtle.pendown()
turtle.goto(pointbottommid)
turtle.goto(pointbottomleft)
turtle.goto(pointtop4)
turtle.penup()
turtle.goto(pointbottommid)
turtle.pendown()
turtle.goto(pointbottomright)
turtle.goto(pointtop2)

turtle.hideturtle()
turtle.exitonclick()
