import turtle
import random




## 함수 선언 부분 ##
def  screenLeftClick(x, y):
    global r, g, b
    r = random.random()
    g = random.random()
    b = random.random()
    turtle.pencolor((r, g, b))
    turtle.pendown()
    turtle.goto(x, y)

    tSize = random.randrange(1, 10)
    turtle.shapesize(tSize)
   
def  screenRightClick(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.right(angle)
    tSize = random.randrange(1, 10)
    angle = random.randrange(1, 361)
    turtle.stamp()

# def  screenMidClick(x, y):
#     global r, g, b
#     tSize = random.randrange(1, 10)
#     turtle.shapesize(tSize)
#     r = random.random()
#     g = random.random()
#     b = random.random()

## 변수 선언 부분 ##
pSize = 10
r, g, b = 0.0, 0.0, 0.0

## 메인 코드 부분 ##
turtle.title('거북이로 그림 그리기')
turtle.shape('turtle')
turtle.pensize(pSize)

turtle.onscreenclick(screenLeftClick, 1)
# turtle.onscreenclick(screenMidClick, 2)
turtle.onscreenclick(screenRightClick, 3)

myT = None

## 메인 코드 부분 ## 
myT = turtle.Turtle()
myT.shape('turtle')

for i in range(0, 6) :
    myT.forward(200)
    myT.right(90)
    myT.forward(180)
    myT.right(70)
    myT.forward(160)
    myT.right(50)

turtle.done()
