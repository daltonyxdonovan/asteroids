import pygame, sys
GREEN = (0,255,0)
count = 0

def load_image(name):
	image = pygame.image.load(name)
	return image

class Ship(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.images = []
		self.images.append(load_image('Ship.png'))
		self.images.append(load_image('Ship.png'))

		# assuming both images are 50x50 pixels
		self.index = 0
		self.image = self.images[self.index]
		self.rect = pygame.Rect(0, 0, 50, 50)
		
	def update(self):
		global count
		self.image = self.images[self.index]
		count += 1
		if count > 10:
			self.index += 1
			count = 0
		if self.index > 1:
			self.index = 0
	
	def still(self):
		self.images.pop(0)
		self.images.pop(0)
		self.images.append(load_image('Ship.png'))
		self.images.append(load_image('Ship.png'))
	def moveLeft(self):
		self.images.pop(0)
		self.images.pop(0)
		self.images.append(load_image('ShipLeft.png'))
		self.images.append(load_image('ShipLeft.png'))
	def moveRight(self):
		self.images.pop(0)
		self.images.pop(0)
		self.images.append(load_image('ShipRight.png'))
		self.images.append(load_image('ShipRight.png'))
	def moveUp(self):
		self.images.pop(0)
		self.images.pop(0)
		self.images.append(load_image('ShipUp.png'))
		self.images.append(load_image('ShipUp.png'))
	def moveUpLeft(self):
		self.images.pop(0)
		self.images.pop(0)
		self.images.append(load_image('ShipUpLeft.png'))
		self.images.append(load_image('ShipUpLeft.png'))
	def moveUpRight(self):
		self.images.pop(0)
		self.images.pop(0)
		self.images.append(load_image('ShipUpRight.png'))
		self.images.append(load_image('ShipUpRight.png'))
	def moveDown(self):
		self.images.pop(0)
		self.images.pop(0)
		self.images.append(load_image('ShipDown.png'))
		self.images.append(load_image('ShipDown.png'))
	def moveDownLeft(self):
		self.images.pop(0)
		self.images.pop(0)
		self.images.append(load_image('ShipDownLeft.png'))
		self.images.append(load_image('ShipDownLeft.png'))
	def moveDownRight(self):
		self.images.pop(0)
		self.images.pop(0)
		self.images.append(load_image('ShipDownRight.png'))
		self.images.append(load_image('ShipDownRight.png'))
	def hurt(self):
		self.images.pop(0)
		self.images.pop(0)
		self.images.append(load_image('shiphurt1.png'))
		self.images.append(load_image('shiphurt2.png'))