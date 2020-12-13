import datetime
import svg_build
import shape
import palettes
import random

title = "cavalcade"
x_in = 1920
y_in = 1080

time = datetime.datetime.now()
string_time = time.strftime("%d-%m-%Y-%H-%M-%S")
name = (title + "_" + string_time)
svg_build.start(name, 0, x_in, y_in, "white")

x_n = 14
y_n = 5
x_size = 1920 / x_n
y_size = 1080 / y_n
target_list = []
segment_list = []

for x in range(0, x_n + 1):
	for y in range(0, y_n + 1):
		if x % 2:
			point = [x*x_size, y*y_size]
		else:
			point = [x*x_size, (y+0.5)*y_size]
		target_list.append(point)
	
def slice(slice_shape):

	slice_list = []

	for x in range(0, len(slice_shape)):
		edge = shape.divide_line(slice_shape[x], slice_shape[(x + 1) % len(slice_shape)], 2, False)

		for y in range (0, 2):
			slice_list.append(edge[y])

	return slice_list

def kernel(kernel_list, shape_sides, recurse):
	
	for x in range(0, shape_sides):
		segment = [shape.centre(kernel_list)]				   
		segment.append(kernel_list[(2*x + 1) % len(kernel_list)])
		segment.append(kernel_list[(2*x) % len(kernel_list)])
		segment.append(kernel_list[(2*x - 1) % len(kernel_list)])
	
		if recurse == False:
			#colour = palettes.plt1[random.randint(0, 9)]
			colour = str(hex(random.randrange(11111, 14555222, 30)))
			svg_build.generate_path(segment, st_w=2, st=palettes.plt8[1], fill='#' + colour[2:])
	
		if recurse:
			segment_list.append(segment)
			kernel(slice(segment), shape_sides, recurse - 1)

height = y_size/1.15

gem_list = []

for target in range(0, len(target_list)):
	#svg_build.generate_text(target_list[target], target, size=20)
	root_sides = random.randint(5,9)
	root_shape = shape.centre_polygon(target_list[target], root_sides, height, orient=0)
	kernel(slice(root_shape), root_sides+1, random.randint(1,3))
	gem_list.append(root_shape)

#for gem in range(0, len(gem_list)):
#	svg_build.generate_path(gem_list[gem], st_w=6, st=palettes.plt8[1], fill="none")
	
#for segment in range(0, len(segment_list)):
#	svg_build.generate_path(segment_list[segment], st_w=3, st=palettes.plt8[1], fill="none")
	
svg_build.end()				