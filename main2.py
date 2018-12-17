import pygame
from pygame.locals import *
import os
import sys

size = (550,550)

pygame.init()

pygame.display.set_caption('Tris Bello')

pygame.mixer.music.load ('caligula.ogg') 
pygame.mixer.music.play (- 1 )


class Grid:
	def __init__(self, size, bg_img, grid_size, img0, img1):
		self.screen = pygame.display.set_mode(size)

		self.occ_coords = [0,0,0,0,0,0,0,0,0]

		bg = pygame.image.load(bg_img)
		self.bg = pygame.transform.scale(bg, grid_size)

		img0 = pygame.image.load(img0)
		self.img0 = pygame.transform.scale(img0, (int(grid_size[0]/3-30), int(grid_size[1]/3-30)))
		img1 = pygame.image.load(img1)
		self.img1 = pygame.transform.scale(img1, (int(grid_size[0]/3-30), int(grid_size[1]/3-30)))

		self.coords = []
		for x in range(3):
			for y in range(3):
				self.coords.append((50+grid_size[0]/3*x+15, 50+grid_size[1]/3*y+15))

	def mark(self, pos, num):
		obj = 1
		if num % 2 == 0:
			obj = 2
		self.occ_coords[pos] = obj


	def draw(self):
		self.screen.fill((255, 255, 255))
		self.screen.blit(self.bg, (50,50))
		for x in range(9):
			if self.occ_coords[x] == 1:
				self.screen.blit(self.img0, self.coords[x])
			elif self.occ_coords[x] == 2:
				self.screen.blit(self.img1, self.coords[x])
		pygame.display.update()


grid = Grid(size, "grid.png", (450,450), "Apple4.png", "windows.png")

running = True
num = 0

while running:
	grid.draw()

	for i in pygame.event.get():
	    if i.type == pygame.QUIT:
	      	running = False
	      	pygame.quit()
	    elif i.type == MOUSEBUTTONDOWN and i.button == 1:
	    	x, y = i.pos
	    	for c in range(9):
	    		if grid.occ_coords[c]==0 and x >= grid.coords[c][0] and x <= grid.coords[c][0]+120 and y >= grid.coords[c][1] and y <= grid.coords[c][1]+120:
	    			grid.mark(c, num)
	    			num += 1
	    			break

	