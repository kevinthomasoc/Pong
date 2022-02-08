from graphics import *
import random
import time


RADIUS = 20
color = "black"


win = GraphWin("Pong", 800, 600)


center = Point(800/2, 600/2)

 
lPadPointl = Point(25,250)
lPadPoint2 = Point(40,450)


rPadPointl = Point(760,250)
rPadPoint2 = Point(775,450)




ball = Circle(center, RADIUS)


lPaddle = Rectangle(lPadPointl, lPadPoint2)
rPaddle = Rectangle(rPadPointl, rPadPoint2)


ball.setFill("blue")
lPaddle.setFill(color)
rPaddle.setFill(color)

velocity = .1
yvel = .1


def spawnBall():
    ball.draw(win)
def delBall():
    ball.undraw()



lPaddle.draw(win)


rPaddle.draw(win)



rScore = 0


lScore = 0



anchorPoint = Point(800//2,600//2)
message = Text(anchorPoint, "Score " + str(lScore) + ":" + str(rScore))
message.draw(win)




def paddleMove(lpad, rpad):
    user_event = win.checkKey()
    if user_event == "w":
        lpad.move(0, -20)
    if user_event == "s":
        lpad.move(0, 20)
    if user_event == "Up":
        rpad.move(0, -20)
    if user_event == "Down":
        rpad.move(0, 20)

spawnBall()




while True:

    

    lp2= lPaddle.getP2()
    a = lp2.getY()
    lp1 = lPaddle.getP1()
    b = lp1.getY()
    LpadX = lp2.getX()

    rp1 = rPaddle.getP1()
    RpadX = rp1.getX()
    y = rp1.getY()
    rp2 = rPaddle.getP2()
    z = rp2.getY()
    
    
    

    
    ball.move(velocity, yvel)


    centerBall = ball.getCenter()
    xBall = centerBall.getX()


    
    yBall = centerBall.getY()
    

    
    
    if xBall > (800):
        delBall()
        lScore += 1
        message.undraw()
        message = Text(anchorPoint, "Score " + str(lScore) + ":" + str(rScore))
        message.draw(win)
        secondxcoordball = xBall
        while (secondxcoordball) > 400:
            velocity = -0.9
            yvel = 0
            ball.move(velocity, yvel)
            secondxcoordball = secondxcoordball - 0.9
        velocity = 0
        yvel = 0
        spawnBall()
        time.sleep(1)
        velocity = 0.1
        yvel = 0.1
        
    if xBall < 0:
        delBall()
        rScore += 1
        message.undraw()
        message = Text(anchorPoint, "Score " + str(lScore) + ":" + str(rScore))
        message.draw(win)
        xcoordball = xBall
        while (xcoordball) < 400:
            velocity = 0.9
            yvel = 0
            ball.move(velocity,yvel)
            xcoordball += 0.9
        velocity = 0
        yvel = 0
        spawnBall()
        time.sleep(1)
        velocity = 0.1
        yvel = 0.1
            
        
        
        
        
        
        
        
        

    
    if yBall <= 0:
        yvel = -yvel
        
    
    
    if yBall >= 600:
        yvel = -yvel
        

    
    
    if (xBall - RADIUS) <= (LpadX):
        if (yBall) <= (a):
            if (yBall) >= (b):
                velocity = -velocity
                yvel = -yvel
                

    
    if (xBall + RADIUS) >= (RpadX):
        if (yBall + RADIUS) >= (y):
            if (yBall + RADIUS) <= (z):
                velocity = -velocity
                yvel = -yvel
        

                
    if win.checkMouse():
        win.close()
        break
    
    
    
    
    
    
    

    paddleMove(lPaddle, rPaddle)
    

    

    

exit(0)

