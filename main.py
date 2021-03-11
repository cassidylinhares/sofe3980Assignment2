import pygame
from paddle import Paddle
from ball import Ball
from score import Score
from instrumentation import timeFunc

#global Colours
BLACK = (0,0,0)
WHITE = (255,255,255)

#init game
pygame.init()
timer = pygame.time.Clock()

#init canvas
SCREEN_WIDTH = 720
SCREEN_HEIGHT = 480
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Pong')

#init game objects
player = Paddle(20)
bot = Paddle(SCREEN_WIDTH - 30)
ball = Ball()
playerScore = Score(150)
botScore = Score(450)

#group Sprites
sprite_list = pygame.sprite.Group()

sprite_list.add(player)
sprite_list.add(bot)
sprite_list.add(ball)

#game loop
playing = True
while playing:
    #event listener
    for event in pygame.event.get(): #pygame window events
        if event.type == pygame.QUIT:
            playing = False 
    
    kb = pygame.key.get_pressed()
    if kb[pygame.K_UP]:
        player.up()
    if kb[pygame.K_DOWN]:
        player.down()  
            
    #game logic
    sprite_list.update()
    #timeee
    # timeFunc("Ball.move()", ball.move)
    # timeFunc("Ball.hitPlayer(player)", ball.hitPlayer, player)
    # timeFunc("Score.playerScored()", playerScore.playerScored, ball, botScore)
    
    ball.move()
    ball.hitPlayer(player)
    ball.hitBot(bot)
    bot.moveBot(ball)
    playerScore.playerScored(ball, botScore)
    botScore.botScored(ball, playerScore)
    
    #Rendering
    window.fill(BLACK)
    pygame.draw.line(window, WHITE, [SCREEN_WIDTH/2, 0], [SCREEN_WIDTH/2, SCREEN_HEIGHT], 1)
        #draw sprites
    sprite_list.draw(window)
    
    window.blit(playerScore.display(), playerScore.loc)
    window.blit(botScore.display(), botScore.loc)
    
    pygame.display.flip()
    
    #30 fps
    timer.tick(30)
    
pygame.quit()