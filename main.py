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
right_paddle_vel = left_paddle_vel = 0

#Main Loop
while run:
	wn.fill(BLACK)
	for i in pygame.event.get():
		if i.type == pygame.QUIT:
			run = False
		elif i.type == pygame.KEYDOWN:
			if i.key == pygame.K_UP:
				right_paddle_vel = -0.9
			if i.key == pygame.K_DOWN:
				right_paddle_vel = 0.9
			if i.key == pygame.K_w:
				left_paddle_vel = -0.9
			if i.key == pygame.K_s:
				left_paddle_vel = 0.9
		
		if i.type == pygame.KEYUP:
			right_paddle_vel = 0
			left_paddle_vel = 0

		#Ball's Moment Controls
		if ball_y <= 0 + radius or ball_y >= HEIGHT - radius:
			ball_vel_y *= -1
		if ball_x >= WIDTH - radius:
			ball_x,ball_y = WIDTH/2 - radius, HEIGHT/2 - radius
			ball_vel_x *= -1
			ball_vel_y *= -1
		if ball_x <= 0 + radius:
			ball_x,ball_y = WIDTH/2 - radius, HEIGHT/2 - radius
			ball_vel_x, ball_vel_y = 0.7, 0.7

		#Paddle's Moment Controls
		if left_paddle_y >= HEIGHT - paddle_hight:
			left_paddle_y = HEIGHT - paddle_hight
		if left_paddle_y <= 0:
			left_paddle_y = 0
		if right_paddle_y >= HEIGHT - paddle_hight:
			right_paddle_y = HEIGHT - paddle_hight
		if right_paddle_y <= 0:
			right_paddle_y = 0

		#paddle collisions
		#left paddle
		if left_paddle_x <= ball_x <= left_paddle_x + paddle_width:
			if left_paddle_y <= ball_y <= left_paddle_y + paddle_hight:
				ball_x = left_paddle_x + paddle_width
				ball_vel_x *= -1
		
		#right paddle
		if right_paddle_x <= ball_x <= right_paddle_x:
			if right_paddle_x <= ball_y <= right_paddle_x:
				ball_x = right_paddle_x
				ball_vel_x *= -1

		#Moment
		ball_x += ball_vel_x
		ball_y += ball_vel_y
		right_paddle_y += right_paddle_vel
		left_paddle_y += left_paddle_vel 

		#Object
		pygame.draw.circle(wn,WHITE,(ball_x, ball_y),radius)
		pygame.draw.rect(wn, CREAM, pygame.Rect(left_paddle_x, left_paddle_y, paddle_width, paddle_hight))
		pygame.draw.rect(wn, CREAM, pygame.Rect(right_paddle_x, right_paddle_y, paddle_width, paddle_hight))
		pygame.display.update()