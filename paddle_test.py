import unittest, pygame
from paddle import Paddle
from ball import Ball

class TestPaddle(unittest.TestCase):
    def testPaddleInit(self):
        print('Describe: test cases for paddle Class')  

        p = Paddle(26);

        self.assertEqual(p.rect.x, 26, 'paddle x should be 26px')
        self.assertEqual(p.rect.y, 160, 'paddle y should be 1/3 of main canvas')
        
        self.assertEqual(p.rect.width, 10, 'width of paddle should be 10px')
        self.assertEqual(p.rect.height, 90, 'height of paddle should be 90px')

    def testPaddleMoveUp(self):
        print('Describe: test Paddle Class Movement Up') 
        x = 27
        i = 0
        p = Paddle(x);
        while i<200:
            p.up();
            i+=1
            
        #move up
        self.assertLess(p.rect.y, 160, 'y loc is less than 160')
        self.assertLess(p.rect.y, 25, 'y loc is less than 25')
        self.assertEqual(p.rect.y, 0, 'y loc is 0')
  
    def testPaddleMoveDown(self):
        print('Describe: test Paddle Class Movement Down') 
        x = 27
        i = 0
        p = Paddle(x);
        while i<200:
            p.down();
            i+=1
            
        #move up
        self.assertGreater(p.rect.y, 160, 'y loc is less than 160')
        self.assertGreater(p.rect.y, 200, 'y loc is less than 200')
        self.assertEqual(p.rect.y, 390, 'y loc is screenHeight - p.height')

    def testBotPaddle(self):
        print('Describe: test bot paddle movement') 
        tests = [
            {'x': 300, 'y': 0, 'speed': [3,3], 'expcX': 673, 'expcY': 150},
            {'x': 300, 'y': 400, 'speed': [3,3], 'expcX': 673, 'expcY': 170}
        ]

        for t in tests:
            b = Ball(t['x'], t['y'], t['speed'])
            p = Paddle(673)
            p.moveBot(b)
            
            self.assertEqual(p.rect.x, t['expcX'], 'x of paddle should be ' + str(t['expcX']))
            self.assertEqual(p.rect.y, t['expcY'], 'y of paddle should be ' + str(t['expcY']))
