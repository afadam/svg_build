import svg_build
import shape
import palettes
import random

title = "empty"
x_in = 1920
y_in = 1080

origin = [(x_in/2),(y_in/2)]

frames = 1

for z in range (0, frames, 1):
	
	svg_build.start(title, z, x_in, y_in)

		
	svg_build.end(z)
	