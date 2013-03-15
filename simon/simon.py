import RPi.GPIO as GPIO, time, pyscreen
import random
from time import sleep

class simon:
	GPIO.cleanup()
	GPIO.setmode(GPIO.BCM)
	pscreen = pyscreen.pyscreen()
	
	#Listing pin cconfiguration like this to for easy reference.
	#inputs
	blue_input = 25
	green_input  = 24
	red_input = 23
	yellow_input = 18

	#outputs
	blue_led = 22
	green_led= 27
	red_led = 17
	yellow_led = 4

	io_combo = [[blue_led,blue_input],[yellow_led, yellow_input],[red_led, red_input],[green_led, green_input]]
	
	def start_game(self):
		self.pscreen.print_text("Welcome to the r-pi mem game!!!")
		
		for match in self.io_combo:
			GPIO.setup(match[0], GPIO.OUT)
			GPIO.setup(match[1], GPIO.IN)
			GPIO.output(match[0], False)
		
		batch = []
		score = 0
		keep_playing = True
		while keep_playing:
			#Cleanup
			self.leds_off()
			sleep(0.30)
			batch.append(self.io_combo[random.randint(0,3)][0])
			for item in batch:
				GPIO.output(item, True)
				sleep(1)
				GPIO.output(item, False)
				sleep(0.30)
			for item in batch:
				waiting_for_input = True
			
				while waiting_for_input:
					for match in self.io_combo:
						while (GPIO.input(match[1]) == False):
							waiting_for_input = False
							GPIO.output(match[0], True)
							if (item != match[0]):
								keep_playing = False
								self.end_game(score)
						GPIO.output(match[0], False)
		
			score = score + 1
			self.pscreen.print_text("Current score :" + str(score))
						
	def end_game(self, score):
		self.leds_off()

		self.pscreen.print_text ("Final Score: " + str(score))
		time.sleep(2)
		self.pscreen.print_text ("Enter Name:")
		name = raw_input()

		self.pscreen.print_text (name +" scored: " +  str(score))
		time.sleep(4)
		raise SystemExit
	
	def leds_off(self):
		for match in self.io_combo:
			GPIO.output(match[0], False)	

	
	def __del__(self):
		GPIO.cleanup()		