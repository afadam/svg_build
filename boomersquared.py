import datetime
import svg_build
import shape
import palettes
import random

title = "boomersquared"
x_in = 1920
y_in = 1080
origin = [960, 540]

time = datetime.datetime.now()
string_time = time.strftime("%d-%m-%Y-%H-%M-%S")

name = (title + "_" + string_time)

svg_build.start(name, 0, x_in, y_in, palettes.plt0[0])

sides = 6

root_shape = shape.centre_polygon(origin, sides, (y_in / 2))

#svg_build.generate_path(root_shape,st_w=2,st=palettes.plt4[random.randint(1, 3)])

perimeter_list = []

def slice(slice_shape):

	slice_list = []

	for x in range (0, len(slice_shape)):
		edge = shape.divide_line(slice_shape[x], slice_shape[(x + 1) % len(slice_shape)], 2, False)

		for y in range (0, 2):
			slice_list.append(edge[y])

	return slice_list

def kernel(kernel_list, shape_sides, recurse):
	
	for x in range (0, shape_sides):
		segment = [shape.centre(kernel_list)]				   
		segment.append(kernel_list[(2*x + 1) % len(kernel_list)])
		segment.append(kernel_list[(2*x) % len(kernel_list)])
		segment.append(kernel_list[(2*x - 1) % len(kernel_list)])
	
		if recurse == False:
			svg_build.generate_path(segment, st_w=1, fill=palettes.plt1[random.randint(1, 4)])
		#svg_build.generate_path(segment, st_w=4, st=palettes.plt1[1])
		#else:
			#svg_build.generate_path(segment, st_w=recurse*2, st=palettes.plt1[random.randint(1, 4)])
			
		if recurse:
			kernel(slice(segment), shape_sides, recurse - 1)
		
i = slice(root_shape)
kernel(i, sides, 4)

for y in range (1, len(perimeter_list)+1):
	svg_build.generate_text(perimeter_list[y-1], y, size=36)
	
svg_build.end()
				   
				   
				 #  notes[note % len(notes)]