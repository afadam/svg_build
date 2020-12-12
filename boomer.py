import datetime
import svg_build
import shape
import palettes
import random

title = "boomer"
x_in = 1920
y_in = 1080
origin = [960, 540]

time = datetime.datetime.now()
string_time = time.strftime("%d-%m-%Y-%H-%M-%S")

name = (title + "_" + string_time)

svg_build.start(name, 0, x_in, y_in, "white")

sides = 5

root_shape = shape.centre_polygon(origin, sides, (y_in / 8))

#svg_build.generate_path(root_shape,st_w=2,st=palettes.plt4[random.randint(1, 3)])

perimeter_list = []

for x in range (0, len(root_shape)):
	edge = shape.divide_line(root_shape[x], root_shape[(x + 1) % len(root_shape)], 2, False)
	
	for y in range (0, 2):
		perimeter_list.append(edge[y])

for x in range (0, sides):
	segment = [origin]
	segment.append(perimeter_list[(2*x - 1) % len(perimeter_list)])
	segment.append(perimeter_list[2*x])
	segment.append(perimeter_list[(2*x + 1) % len(perimeter_list)])

	svg_build.generate_path(segment, st_w=5, st=palettes.plt4[random.randint(1, 3)])

for y in range (1, len(perimeter_list)+1):
	svg_build.generate_text(perimeter_list[y-1], y, size=36)
	
svg_build.end()
				   
				   
				 #  notes[note % len(notes)]