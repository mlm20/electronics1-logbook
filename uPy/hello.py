from oled import OLED	# load oled module from flash memory

oled = OLED()           # Instantiate an OLED object
oled.poweron()
oled.init_display()     # initialise the OLED display

#  Simple Hello world message
oled.draw_text(0,0,'Hello World!')   # each character is 6x8 pixels
oled.display()          # flush display# Write your code here :-)
