import svg_build
import shape
import palettes
import random

title = "blow"
x_in = 1920
y_in = 1080

origin = [(x_in/2),(y_in/2)]

frames = 1

sides = 7
height = 7

for z in range (0, frames, 1):
	
	svg_build.start(title, z, x_in, y_in, random.choice(palettes.plt1))

	for x in range (0, x_in, 16):
	
		svg_build.generate_path(shape.centre_polygon(origin, sides, x), st_w=18, st=random.choice(palettes.plt1))
		sides += 1
		
	svg_build.end(z)
	