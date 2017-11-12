# Prototipo del juego

import pygame
from pygame.locals import*
import random

pygame.init()

def createenemigo1():
	x = random.randrange(800)
	y = random.randint(-610,-10)
	return [x,y]



def main():
	score = 0

	fuente = pygame.font.Font(None, 20)	

	radio = 20
	posx = 400
	posy = 550
	velocidadx = 0
	velocidady = 0
	velocidadmovimiento = 5

	enemigos = []
	enemy = []
	velocidadEnemigo = 5


	pygame.init()
	screen = pygame.display.set_mode((800,600))

	clock = pygame.time.Clock()
	playing = True
	lose = False
	while playing:
		if not lose:
			screen.fill((0,0,0))

			scoreprint = fuente.render(str(int(score)),1,(255,255,255))

			for evento in pygame.event.get():

				if evento.type == QUIT:
					playing = False


				elif evento.type == pygame.KEYDOWN:
					if evento.key == pygame.K_ESCAPE:
						playing = False
					elif evento.key == pygame.K_LEFT:
						velocidadx = - velocidadmovimiento
						movement = True

					elif evento.key == pygame.K_RIGHT:
						velocidadx = + velocidadmovimiento
						movement = True

				elif evento.type == pygame.KEYUP:
					if evento.key == pygame.K_LEFT:
						if pygame.key.get_pressed()[K_RIGHT]:
							velocidadx = velocidadmovimiento
						else:
							velocidadx = 0
						
					elif evento.key == pygame.K_RIGHT:
						if pygame.key.get_pressed()[K_LEFT]:
							velocidadx = - velocidadmovimiento

						else:
							velocidadx = 0

			player = pygame.Rect(posx-15,posy-15,30,30)
			pygame.draw.rect(screen, (200,0,0),player)

			posx += velocidadx
			posy += velocidady

			velocidadEnemigo = 5 + int(score/10)

			if len(enemigos) < 30:
				enemigos.append(createenemigo1())	
				enemy.append("")		

			for i in range(len(enemigos)):
				enemy[i] = pygame.Rect(enemigos[i][0],enemigos[i][1],20,20)
				pygame.draw.rect(screen, (0,255,0), enemy[i]) 
				enemigos[i][1] += velocidadEnemigo
				if enemigos[i][1] > 600:
					enemigos[i] = createenemigo1()

				#collision: aprender a utilizar masks
				if player.colliderect(enemy[i]):
					lose = True


			score += 1/60

			screen.blit(scoreprint,(10,10))

		else:
			fuente1 = pygame.font.Font(None, 80)
			fuente2 = pygame.font.Font(None, 30)

			finalscoremessage = "score: " + str(int(score))
			finalscore = fuente1.render(finalscoremessage,1,(255,255,255))
			screen.blit(finalscore, (280,250))

			restartmessage = fuente2.render("<< Press <r> to restart >>",1,(255,255,255))
			screen.blit(restartmessage, (250,320))

			for evento in pygame.event.get():

				if evento.type == QUIT:
					playing = False
					


				elif evento.type == pygame.KEYDOWN:
					if evento.key == pygame.K_ESCAPE:
						playing = False

					elif evento.key == pygame.K_r:

						score = 0
						posx = 400
						posy = 550
						velocidadx = 0
						velocidady = 0
						enemigos = []
						enemy = []
						lose = False



		clock.tick(60)
		pygame.display.update()

	pygame.quit()
main()