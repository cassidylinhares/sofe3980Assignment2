import pygame

BLACK = (0,0,0)
WHITE = (255,255,255)
SCREEN_WIDTH = 720

class Score:
    def __init__(self, x, ptTest = None):
        self.score = 0 if ptTest is None else ptTest
        self.loc = (x, 10)
        
        
    def checkWin(self, otherPlayerScore):
        if self.score >= 11:
            self.score = 0
            otherPlayerScore.score = 0
            
    def playerScored(self, ball, botScore):
        if ball.rect.x > (SCREEN_WIDTH + ball.rect.width):
            self.score +=1 
        
        self.checkWin(botScore)
            
    def botScored(self, ball, playerScore):
        if ball.rect.x < ball.rect.width:
            self.score +=1 
        
        self.checkWin(playerScore)
            
    def display(self):
        font = pygame.font.Font(None, 64)
        return font.render(str(self.score), 1, WHITE)
        
        