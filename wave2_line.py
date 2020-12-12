import datetime
import svg_build
import shape
import palettes
import random

title = "divide"
x_in = 1024
y_in = 1024
origin = [512,512]

time = datetime.datetime.now()
string_time = time.strftime("%d-%m-%Y-%H-%M-%S")

name = (title + "_" + string_time)

svg_build.start(name, 0, x_in, y_in, palettes.plt0[0])

shape.divide_line([-2,-2], [2,2], 8)

hexagon = shape.centre_polygon(origin, 12, 368)

perimeter_list = []

for x in range (0, len(hexagon)):
	line = shape.divide_line(hexagon[x-1], hexagon[x], 6)
	perimeter_list.extend(line)

print(perimeter_list)
print(len(perimeter_list))

for x in range (1, 12):
	
	for y in range (1, len(perimeter_list)):	
		svg_build.generate_path([perimeter_list[y],perimeter_list[len(perimeter_list) - y]],st_w=random.randint(4, 8),st=palettes.plt4[random.randint(1, 3)])
	
		shape.rotate(perimeter_list, random.randint(10, 170), shape.centre(perimeter_list))

svg_build.end()