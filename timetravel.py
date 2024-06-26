import datetime
import svg_build
import shape
import palettes
import random
import funcs

title = "timetravel"
x_in = 1920
y_in = 1080

time = datetime.datetime.now()
string_time = time.strftime("%d-%m-%Y-%H-%M-%S")
name = (title + "_" + string_time)
svg_build.start(name, 0, x_in, y_in, "black")

x_n = 16
y_n = 9
x_size = x_in / x_n
y_size = y_in / y_n

target_list = []

for x in range(0, x_n + 1):
	for y in range(0, y_n + 1):
		#if y % 2:
			#point = [(x*x_size) + (x_size /2), y*y_size]
		#else:
			point = [x*x_size, y*y_size]
			target_list.append(point)

for target in range(0, len(target_list)):
	polygon = shape.centre_polygon(target_list[target], 6, 48)
	svg_build.generate_path(polygon, st="white")
	segments = funcs.kernel(polygon)

	

svg_build.end()				