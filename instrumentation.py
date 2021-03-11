import time
import pygame
from paddle import Paddle
from ball import Ball
from score import Score
 
def timeFunc(funcName, method, *args):
    s = time.perf_counter_ns()
    method(*args)
    e = time.perf_counter_ns()
    f = open("timeElapsed", "a")
    f.write("Time to run "+ funcName +": " + str(e-s) + " nano seconds\n")

# 1. Test check win
s = Score(100, 10)
s2 = Score(200, 11)
timeFunc("Score.checkWin(otherPlayersScore)", s2.checkWin, s)

# 2. Test reset ball
b = Ball()
timeFunc("Ball.reset()", b.reset)

# 3. Test Wall Collision with ball
b = Ball(-5, -1)
timeFunc("Ball.wallCollision()", b.wallCollision)

# 4. Test Move Paddle Up
p = Paddle(20)
timeFunc("Paddle.up()", p.up)

# 5. Test ball in contact with Player's Paddle
b = Ball(19, 250)
p = Paddle(20)
timeFunc("Ball.hitPlayer(paddle)", b.hitPlayer, p)