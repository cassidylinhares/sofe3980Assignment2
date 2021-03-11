import unittest, pygame
from ball import Ball
from paddle import Paddle

class TestBall(unittest.TestCase):
    def testBallInit(self):
        print('Describe: test cases for Ball Class init')    
        b = Ball();

        self.assertEqual(b.rect.x, 360, 'ball x should be width/2 px')
        self.assertEqual(b.rect.y, 240, 'y should be height/2 of main canvas')
 
        self.assertEqual(b.rect.width, 10, 'width should be 10px')
        self.assertEqual(b.rect.height, 10, 'height should be 10px')

    def testBallReset(self):
        print('Describe: test Ball reset Function')

        x, y, vel = 100, 200, [4, 4]
        b = Ball(x, y, vel);
        b.reset();
        
        self.assertEqual(b.rect.x, 100, 'x should be 100')
        self.assertEqual(b.rect.y, 200, 'y should be 200')

        self.assertEqual(b.vel[1], 4, 'y Speed should be 4')
        self.assertIn(b.vel[0], [-4, 4], 'x Speed should be 4 or -4')
       
    def testBallWallCollision(self):
        print('Describe: test Ball Collision with Wall')

        tests = [
            #test y and yspeed
            {'x': 200, 'y': 0, 'speed': [3,3], 'expcX': 200, 'expcY': 0, 'expcXspeed': 3, 'expcYspeed': -3},
            {'x': 200, 'y': 480, 'speed': [3,3], 'expcX': 200, 'expcY': 480, 'expcXspeed': 3, 'expcYspeed': -3},
            {'x': 200, 'y': 200, 'speed': [3,3], 'expcX': 200, 'expcY': 200, 'expcXspeed': 3, 'expcYspeed': 3},
            {'x': 0, 'y': 480, 'speed': [3,0], 'expcX': 0, 'expcY': 480, 'expcXspeed': [-3,3], 'expcYspeed': 0},
            #test x and xspeed
            {'x': 0, 'y': 200, 'speed': [3,3], 'expcX': 0, 'expcY': 200, 'expcXspeed': [-3,3], 'expcYspeed': 3},
            {'x': 740, 'y': 200, 'speed': [3,3], 'expcX': 740, 'expcY': 200, 'expcXspeed': [-3,3], 'expcYspeed': 3},
            {'x': 100, 'y': 200, 'speed': [3,3], 'expcX': 100, 'expcY': 200, 'expcXspeed': 3, 'expcYspeed': 3}
        ]
        
        for t in tests:
            b = Ball(t['x'], t['y'], t['speed'])
            b.wallCollision()
            
            self.assertEqual(b.rect.x, t['expcX'], 'x should be ' + str(t['expcX']))
            self.assertEqual(b.rect.y, t['expcY'], 'y should be ' + str(t['expcY']))

            self.assertEqual(b.vel[1], t['expcYspeed'], 'y Speed should be '+ str(t['expcYspeed']))
            
            if isinstance(t['expcXspeed'], list):
                self.assertIn(b.vel[0], t['expcXspeed'], 'x Speed should be one of '+ str(t['expcXspeed']))
            elif type(t['expcXspeed']) == 'int':
                self.assertEqual(b.vel[0], t['expcXspeed'], 'x Speed should be one of '+ str(t['expcXspeed']))
       
    def testBallWithinPaddleHeight(self):
        print('Describe: test Ball Collision with function: withinPaddleHeight')
        tests = [
            {'x': 100, 'y': 160, 'speed': [-3,3], 'expc': True},
            {'x': 100, 'y': 300, 'speed': [-3,3], 'expc': False}
        ]
        
        for t in tests:
            b = Ball(t['x'], t['y'], t['speed'])
            p = Paddle(27)
            p2 = Paddle(673)

            self.assertEqual(b.withinPaddleHeight(p), t['expc'], 'ball in Paddle1 height should be' + str(t['expc']))
            self.assertEqual(b.withinPaddleHeight(p2), t['expc'], 'ball in Paddle2 height should be' + str(t['expc']))

    def testBallHitPlayer(self):
        print('Describe: test Ball Collision with player Paddle')
        tests = [
            {'x': 37, 'y': 160, 'speed':[-3,3], 'expcX': 37, 'expcY': 160, 'expcVel': [3,3]},
            {'x': 30, 'y': 160, 'speed':[-3,3], 'expcX': 37, 'expcY': 160, 'expcVel': [3,3]},
            {'x': 65, 'y': 160, 'speed':[-3,3], 'expcX': 65, 'expcY': 160, 'expcVel': [-3,3]},
            {'x': 45, 'y': 100, 'speed':[-3,3], 'expcX': 45, 'expcY': 100, 'expcVel': [-3,3]}
        ]
        for t in tests:
            b = Ball(t['x'], t['y'], t['speed'])
            p = Paddle(27)
            b.hitPlayer(p)

            self.assertEqual(b.rect.x, t['expcX'], 'x should be ' + str(t['expcX']))
            self.assertEqual(b.rect.y, t['expcY'], 'y should be ' + str(t['expcY']))
            self.assertListEqual(b.vel, t['expcVel'], 'Vel should be ' + str(t['expcVel']))
            
    def testBallHitBot(self):
        print('Describe: test Ball Collision with Bot Paddle')
        tests = [
            {'x': 675, 'y': 160, 'speed':[3,3], 'expcX': 663, 'expcY': 160, 'expcVel':[-3,3]},
            {'x': 665, 'y': 160, 'speed':[3,3], 'expcX': 663, 'expcY': 160, 'expcVel':[-3,3]},
            {'x': 300, 'y': 160, 'speed':[3,3], 'expcX': 300, 'expcY': 160, 'expcVel':[3,3]},
            {'x': 675, 'y': 100, 'speed':[3,3], 'expcX': 675, 'expcY': 100, 'expcVel':[3,3]}
        ]
        
        for t in tests:
            b = Ball(t['x'], t['y'], t['speed'])
            p = Paddle(673)
            b.hitBot(p)

            self.assertEqual(b.rect.x, t['expcX'], 'x should be ' + str(t['expcX']))
            self.assertEqual(b.rect.y, t['expcY'], 'y should be ' + str(t['expcY']))
            self.assertListEqual(b.vel, t['expcVel'], 'Vel should be ' + str(t['expcVel']))
