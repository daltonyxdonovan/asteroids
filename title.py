import pygame, sys
count = 0

def load_image(name):
	image = pygame.image.load(name)
	return image

class Title(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.images = []
		self.images.append(load_image('title1.png'))
		self.images.append(load_image('title2.png'))
		self.images.append(load_image('title3.png'))
		self.images.append(load_image('title4.png'))
		self.images.append(load_image('title5.png'))
		self.images.append(load_image('title6.png'))
		self.images.append(load_image('title7.png'))
		self.images.append(load_image('title8.png'))
		self.images.append(load_image('title9.png'))
		self.images.append(load_image('title10.png'))
		self.images.append(load_image('title11.png'))
		self.images.append(load_image('title12.png'))
		self.images.append(load_image('title13.png'))
		self.images.append(load_image('title14.png'))
		self.images.append(load_image('title15.png'))
		self.images.append(load_image('title16.png'))
		self.images.append(load_image('title17.png'))
		self.images.append(load_image('title18.png'))
		self.images.append(load_image('title19.png'))
		self.images.append(load_image('title20.png'))
		self.images.append(load_image('title21.png'))
		self.images.append(load_image('title22.png'))
		self.images.append(load_image('title23.png'))
		self.images.append(load_image('title24.png'))
		self.images.append(load_image('title25.png'))
		self.images.append(load_image('title26.png'))
		self.images.append(load_image('title27.png'))
		self.images.append(load_image('title28.png'))
		self.images.append(load_image('title29.png'))
		self.images.append(load_image('title30.png'))
		self.images.append(load_image('title31.png'))
		self.images.append(load_image('title32.png'))
		self.images.append(load_image('title33.png'))
		self.images.append(load_image('title34.png'))
		self.images.append(load_image('title35.png'))

		# assuming images are 400x300 pixels
		self.index = 0
		self.image = self.images[self.index]
		self.rect = pygame.Rect(5, 5, 400, 300)
		
	def update(self):
		global count
		count += 1
		if count >= 5:
			self.index += 1
			count = 0
		if self.index > 34:
			self.index = 0		
		self.image = self.images[self.index]

		
def main():
	pygame.init()
	screen = pygame.display.set_mode((800, 800))
	my_sprite = Title()
	my_group = pygame.sprite.Group(my_sprite)
	
	while True:
		event = pygame.event.poll()
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit(0)

		# Calling the 'my_group.update' function calls the 'update' function of all 
		# its member sprites. Calling the 'my_group.draw' function uses the 'image'
		# and 'rect' attributes of its member sprites to draw the sprite.
		my_group.update()
		my_group.draw(screen)
		pygame.display.flip()

		

	if __name__ == '__main__':
		main()