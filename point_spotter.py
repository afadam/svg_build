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

x_n = 120
y_n = 48
x_size = x_in / x_n
y_size = y_in / y_n

target_list = []

for x in range(0, x_n + 1):
	for y in range(0, y_n + 1):
		point = [x*x_size, y*y_size] 
		target_list.append(point)

svg_build.point_spotter(target_list)
	
svg_build.end()				