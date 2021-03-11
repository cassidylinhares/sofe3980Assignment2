import sys, pygame
from paddle import Paddle
from ball import Ball
from score import Score

def traceIt(frame, event, arg):
    if event == "line":
        fname = frame.f_code.co_filename
        lNum = frame.f_lineno
        print(fname, lNum)
    return traceIt
        
# 1. Trace Paddle's y location when paddle moves up
print("Paddles's Y-loc when paddle moves up")
p = Paddle(20, 80)
sys.settrace(traceIt)
p.up()
sys.settrace(None)
print("\n")

# 2. Trace Ball's y location when ball collides with wall
print("Ball's Y-loc when ball hits wall")
b = Ball(60, 0)
sys.settrace(traceIt)
b.wallCollision()
sys.settrace(None)
print("\n")

# 3. Ball's goLeft variable when ball resets
print("Ball's goLeft var when ball resets")
b = Ball(100, 80, [-2, 4])
sys.settrace(traceIt)
b.reset()
sys.settrace(None)
print("\n")

# 4. Trace Ball's x location when ball scores
print("Ball's X-loc when ball crosses goal line")
b = Ball(-2, 30)
sys.settrace(traceIt)
b.wallCollision()
sys.settrace(None)
print("\n")

# 5. Trace Score's points location when score is 10
print("Score's points when ball crosses goal line and score is 10")
s = Score(100, 10)
b = Ball(-2, 30)
s2 = Score(200, 10)
sys.settrace(traceIt)
s.botScored(b, s2)
sys.settrace(None)
print("\n")
