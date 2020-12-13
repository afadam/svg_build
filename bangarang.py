import datetime
import svg_build
import shape
import palettes
import random
import funcs

title = "banganrang"
x_in = 1920
y_in = 1080

time = datetime.datetime.now()
string_time = time.strftime("%d-%m-%Y-%H-%M-%S")
name = (title + "_" + string_time)
svg_build.start(name, 0, x_in, y_in, "white")

x_n = 10
y_n = 6
x_size = x_in / x_n
y_size = y_in / y_n

target_list = []

for x in range(0, x_n + 1):
	for y in range(0, y_n + 1):
		point = [x*x_size, y*y_size] 
		target_list.append(point)

for target in range(0, len(target_list)):
	polygon = shape.centre_polygon(target_list[target], 4, 150, orient=0)
	svg_build.generate_path(polygon)
	segments = funcs.kernel(polygon)

	
	for segment in range(0, len(segments)):
		svg_build.generate_path(segments[segment])
		jam = funcs.firein(segments[segment], 9)
		for roll in range(0, len(jam)):
			svg_build.generate_path(jam[roll])
	
svg_build.end()				