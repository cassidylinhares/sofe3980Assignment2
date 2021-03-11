import unittest
from ball import Ball
from score import Score

class TestScore(unittest.TestCase):
    def testScorePlayer1Win(self):
        print('Describe: checkWin Function: p1 wins') 
        p1 = Score(100, 11)
        p2 = Score(400, 7)
        p1.checkWin(p2)
        
        self.assertEqual(p1.score, 0, 'player1 score should be 0')
        self.assertEqual(p2.score, 0, 'player2 score should be 0')
        
    def testScorePlayer2Win(self):
        print('Describe: checkWin Function: p2 wins') 
        p1 = Score(100, 3)
        p2 = Score(400, 11)
        p2.checkWin(p1)
        
        self.assertEqual(p1.score, 0, 'player1 score should be 0')
        self.assertEqual(p2.score, 0, 'player2 score should be 0')
        
    def testScorePlayer1Score(self):
        print('Describe: p1 scores a point') 
        tests = [
            {'x':740, 'y':200, 'speed':[3,3], 'p1': 3, 'p2':1, 'ansP1':4, 'ansP2':1},
            {'x':200, 'y':200, 'speed':[3,3], 'p1': 3, 'p2':1, 'ansP1':3, 'ansP2':1},
        ]
        
        for t in tests:
            b = Ball(t['x'], t['y'], t['speed'])
            p1 = Score(100, t['p1'])
            p2 = Score(400, t['p2'])
            p1.playerScored(b, p2)
        
            self.assertEqual(p1.score, t['ansP1'], 'player1 score should be ' + str(t['ansP1']))
            self.assertEqual(p2.score, t['ansP2'], 'player2 score should be ' + str(t['ansP2']))
        
    def testScorePlayer2Score(self):
        print('Describe: p2 scores a point') 
        tests = [
            {'x':-16, 'y':200, 'speed':[-3,3], 'p1': 2, 'p2':2, 'ansP1':2, 'ansP2':3},
            {'x':200, 'y':200, 'speed':[-3,3], 'p1': 2, 'p2':2, 'ansP1':2, 'ansP2':2},
        ]
        
        for t in tests:
            b = Ball(t['x'], t['y'], t['speed'])
            p1 = Score(100, t['p1'])
            p2 = Score(400, t['p2'])
            p2.botScored(b, p1)
        
            self.assertEqual(p1.score, t['ansP1'], 'player1 score should be ' + str(t['ansP1']))
            self.assertEqual(p2.score, t['ansP2'], 'player2 score should be ' + str(t['ansP2']))
