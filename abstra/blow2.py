import svg_build
import shape
import palettes
import random

title = "blow"
x_in = 1920
y_in = 1080


frames = 180

height = 1080
sides = int(height / 16) + 2


spin = 0

origin = [(x_in/2),(y_in/2)]


def blow(size, sides, frame, rotate):
	
	svg_build.generate_path(shape.centre_polygon(origin, sides, size, orient=rotate), st_w=18, st=random.choice(palettes.plt4), layer=frame)
	sides -= 1
	size -= 16
	
	if (sides > 2):
		blow(size, sides, z, rotate)
	
background = random.choice(palettes.plt3)

for z in range (0, frames, 1):
	
	svg_build.start(title, z, x_in, y_in, background, anim=True)

	blow(height, sides, z, spin)
	
	spin += 360/frames
		
	svg_build.end(z)
	