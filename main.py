import pygame

pygame.init()

#Initials
WIDTH, HEIGHT = 1000, 600
wn = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PONG GAME")
run = True

#Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
CREAM = (255, 253, 208)

#Ball
radius = 10
ball_x,ball_y = WIDTH/2 - radius, HEIGHT/2 - radius
ball_vel_x, ball_vel_y = 0.7, 0.7

#Paddle
paddle_width, paddle_hight = 20, 120
left_paddle_y = right_paddle_y = HEIGHT/2 - paddle_hight/2
left_paddle_x, right_paddle_x = 100 - paddle_width/2, WIDTH - (100 - paddle_width/2)

#Main Loop
while run:
	wn.fill(BLACK)
	for i in pygame.event.get():
		if i.type == pygame.QUIT:
			run = False

		#Ball's Moment Controls

		#Moment
		ball_x += ball_vel_x
		ball_y += ball_vel_y
		#Object
		pygame.draw.circle(wn,WHITE,(ball_x, ball_y),radius)
		pygame.draw.rect(wn, CREAM, pygame.Rect(left_paddle_x, left_paddle_y, paddle_width, paddle_hight))
		pygame.draw.rect(wn, CREAM, pygame.Rect(right_paddle_x, right_paddle_y, paddle_width, paddle_hight))
		pygame.display.update()