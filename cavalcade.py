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
svg_build.start(name, 0, x_in, y_in, palettes.plt8[2])

x_n = 12
y_n = 4
x_size = 1920 / x_n
y_size = 1080 / y_n
target_list = []

for x in range(0, x_n + 1):
	for y in range(0, y_n + 1):
		point = [x*x_size, y*y_size] 
		target_list.append(point)
	
for target in range(0, len(target_list)):
	svg_build.generate_text(target_list[target], target, size=20)
	
	
svg_build.end()				