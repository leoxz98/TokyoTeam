# Prototipo del juego

import pygame
from pygame.locals import*
import random
import sys
import math

pygame.init()
mouse = (
"   xx   ",
"  x..x  ",
" x....x ",
"x..xx..x",
"x..xx..x",
" x....x ",
"  x..x  ",
"   xx   ",
)
cursor, mask = pygame.cursors.compile(mouse, '.', 'x', 'o') 
size = 8,8
pygame.mouse.set_cursor(size,(3,3), cursor, mask) #hotspot(3,3): the point where the mouse click
pygame.mouse.set_visible(False)

def createColor():
	r = random.randint(0,255)
	g = random.randint(0,255)
	b = random.randint(0,255)
	return (r,g,b)

def createEnemigo0():
	x = random.randrange(1366)
	y = random.randint(-768,-10)
	aumentovely = random.randint(-1,1)
	color = createColor()
	rect = pygame.Rect(x,y,20,20)
	return {"x":x, "y":y, "vely":aumentovely, "color":color, "rect":rect}

def createEnemigo1():
	x = random.randrange(1366)
	y = random.randint(-768,-10)
	aumentovely = random.randint(-1,1)
	movimientoenx = random.randint(2,5)
	rect = pygame.Rect(x,y,20,20)
	color = createColor()
	return {"x":x, "y":y, "vely":aumentovely, "movx": movimientoenx, "color":color, "rect":rect}

def createEnemigo2():
	x = random.randrange(1366)
	y = random.randint(-768,-10)
	aumentovely = random.randint(-1,1)
	movimientoeny = random.randint(1,4)
	color = createColor()
	rect = pygame.Rect(x,y,20,20)
	return {"x":x, "y":y, "vely":aumentovely, "movy": movimientoeny, "color":color, "rect":rect}
	


def pause(screen):
	pause = True
	while pause:
		fuente = pygame.font.Font(None, 80)
		pausemessage = fuente.render("PAUSE" ,1,(255,255,255))
		screen.blit(pausemessage, (280,250))

		for evento in pygame.event.get():

				if evento.type == QUIT:
					pygame.quit()
					sys.exit()

				elif evento.type == JOYBUTTONDOWN:
					if evento.button == 7:
						pause = False

				elif evento.type == pygame.KEYDOWN:
					if evento.key == pygame.K_ESCAPE:
						pygame.quit()
						sys.exit()
					elif evento.key == pygame.K_p:
						pause = False
		pygame.display.update()




def main():
	score = 0

	fuente = pygame.font.Font(None, 20)	

	radio = 20
	posx = 700
	posy = 730
	velocidadx = 0
	velocidadmovimiento = 5
	boost = 0

	aumentovelocidadenemigos = 20

	cantidad_enemigos = 3
	enemigos = [[] for i in range(cantidad_enemigos)]


	pygame.init()
	resolution = pygame.display.Info()
	screen = pygame.display.set_mode((resolution.current_w, resolution.current_h), pygame.FULLSCREEN)  #1366x768

	clock = pygame.time.Clock()
	playing = True
	lose = False

	joysticks = []
	for i in range(pygame.joystick.get_count()):
		joysticks.append(pygame.joystick.Joystick(i))
		joysticks[-1].init()

	sensibilidad = 0.4
	joystick_control = False


	while playing:
		if not lose:
			screen.fill((0,0,0))

			scoreprint = fuente.render(str(int(score)),1,(255,255,255))

			
			player = pygame.Rect(posx-15,posy-15,30,30)
			pygame.draw.rect(screen, (createColor()), player)

			posx += velocidadx * boost if boost else velocidadx
			
			#enemigo0
			
			velocidadEnemigo0 = 6 + int(score/aumentovelocidadenemigos)
			if len(enemigos[0]) < 20:
				enemigos[0].append(createEnemigo0())
			for i in range(len(enemigos[0])):
				enemigos[0][i]["rect"] = pygame.Rect(enemigos[0][i]["x"], enemigos[0][i]["y"], 20, 20)
				pygame.draw.rect(screen, enemigos[0][i]["color"], enemigos[0][i]["rect"]) 
				enemigos[0][i]["y"] += velocidadEnemigo0 + enemigos[0][i]["vely"]
				if enemigos[0][i]["y"] > 768:
					enemigos[0][i] = createEnemigo0()
				#collision: aprender a utilizar masks
				if player.colliderect(enemigos[0][i]["rect"]):
					lose = True
			

			#enemigo1
			velocidadEnemigo1 = 5 + int(score/aumentovelocidadenemigos)
			if len(enemigos[1]) < 15:
				enemigos[1].append(createEnemigo1())
			for i in range(len(enemigos[1])):
				enemigos[1][i]["rect"] = pygame.Rect(enemigos[1][i]["x"], enemigos[1][i]["y"], 20, 20)
				pygame.draw.rect(screen, enemigos[1][i]["color"], enemigos[1][i]["rect"])
				enemigos[1][i]["y"] += velocidadEnemigo1 + enemigos[1][i]["vely"]
				enemigos[1][i]["x"] += enemigos[1][i]["movx"]*math.sin(enemigos[1][i]["y"]/60)
				if enemigos[1][i]["y"] > 768:
					enemigos[1][i] = createEnemigo1()
				if player.colliderect(enemigos[1][i]["rect"]):
					lose = True
			
			#enemigo2
			velocidadEnemigo2 = 5 + int(score/aumentovelocidadenemigos)
			if len(enemigos[2]) < 15:
				enemigos[2].append(createEnemigo2())
			for i in range(len(enemigos[2])):
				enemigos[2][i]["rect"] = pygame.Rect(enemigos[2][i]["x"], enemigos[2][i]["y"], 20, 20)
				pygame.draw.rect(screen, enemigos[2][i]["color"], enemigos[2][i]["rect"])
				enemigos[2][i]["y"] += velocidadEnemigo2 + enemigos[2][i]["vely"]
				enemigos[2][i]["y"] += enemigos[2][i]["movy"]*math.sin(enemigos[2][i]["y"]/60)
				if enemigos[2][i]["y"] > 768:
					enemigos[2][i] = createEnemigo2()
				if player.colliderect(enemigos[2][i]["rect"]):
					lose = True
			


			score += 1/60

			screen.blit(scoreprint,(10,10))

			# joystick controls
			if joystick_control:
				if pygame.joystick.Joystick(0).get_axis(0) < -sensibilidad:
					#left
					velocidadx = -velocidadmovimiento
				elif pygame.joystick.Joystick(0).get_axis(0) > sensibilidad:
					#right
					velocidadx = +velocidadmovimiento
				else:
					velocidadx = 0

				boost = 2 if pygame.joystick.Joystick(0).get_button(0) else 0



			# keyboard controls
			if not joystick_control:
				if pygame.key.get_pressed()[K_RIGHT]:
					velocidadx = +velocidadmovimiento
				elif pygame.key.get_pressed()[K_LEFT]:
					velocidadx = -velocidadmovimiento
				else:
					velocidadx = 0

				boost = 2 if pygame.key.get_pressed()[K_SPACE] else 0


			for evento in pygame.event.get():

				if evento.type == QUIT:
					playing = False

				elif evento.type == JOYAXISMOTION:
					joystick_control = True
				elif evento.type == JOYBUTTONDOWN:
					if evento.button == 7:
						pause(screen)

				elif evento.type == pygame.KEYDOWN:
					joystick_control = False
					if evento.key == pygame.K_ESCAPE:
						playing = False

					elif evento.key == pygame.K_p:
						pause(screen)


		else:
			fuente1 = pygame.font.Font(None, 80)
			fuente2 = pygame.font.Font(None, 30)

			finalscoremessage = "score: " + str(int(score))
			finalscore = fuente1.render(finalscoremessage,1,(255,255,255))
			screen.blit(finalscore, (280,250))

			restarButton = "<< Press <r> to restart >>" if not joystick_control else "<<Press -> to restart>>"
			restartmessage = fuente2.render(restarButton,1,(255,255,255))
			screen.blit(restartmessage, (250,320))

			for evento in pygame.event.get():

				if evento.type == QUIT:
					playing = False
					

				elif evento.type == pygame.JOYBUTTONDOWN:
					if evento.button == 7:
						score = 0
						posx = 700
						posy = 730
						velocidadx = 0
						velocidady = 0
						enemigos = [[] for i in range(cantidad_enemigos)]
						lose = False

				elif evento.type == pygame.KEYDOWN:
					if evento.key == pygame.K_ESCAPE:
						playing = False


					elif evento.key == pygame.K_r:
						score = 0
						posx = 700
						posy = 730
						velocidadx = 0
						velocidady = 0
						enemigos = [[] for i in range(cantidad_enemigos)]
						lose = False



		clock.tick(60)
		pygame.display.update()

	pygame.quit()
main()
