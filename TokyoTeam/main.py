import pygame
from pygame.locals import*
import random

from scoreboards import *

pygame.init()
pygame.mouse.set_visible(False)



def main():
	scene = "menu"
	scores = getHighScores()

	screen = pygame.display.set_mode((450,500))
	
	string = keyboard(screen)
	
	playing = True
	while playing:
		screen.fill((0,0,0))

		for evento in pygame.event.get():

			if evento.type == QUIT:
				playing = False


			elif evento.type == pygame.KEYDOWN:
				if evento.key == pygame.K_ESCAPE:
					playing = False

		

		"""
		if scene == "menu":
			scene = menu()
		elif scene == "scoreboards":
			scene = scoreboards()
		elif scene == "storymode":
			pass
		elif scene == "arcade":
			score = game()
			if score > min(scores):
				name = keyboard()
				score.index(min(scores)) = [score, name]
			scene = restart()
			

		"""

		pygame.display.update()

	pygame.display.quit()

main()
