import pygame
pygame.init()

class pyscreen:
	#Screen
	screen = None
	#Background color
	bg_color = None
	#Font color
	font_color = None
	def __init__(self):
		self.bg_color = (150, 150, 150)
		size = (pygame.display.Info().current_w, pygame.display.Info().current_h)
		self.screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
		self.font = pygame.font.Font(None, 60)
		self.font_color = (255, 255, 255)
		self.screen.fill(self.bg_color)
		pygame.font.init()
		pygame.display.update()
		
		
	def print_text(self, text):
		self.screen.fill(self.bg_color)
		font = pygame.font.Font(None, 60)
		text_area = font.render(text, True, self.font_color)
		self.screen.blit(text_area, (150, 150))
		pygame.display.update()