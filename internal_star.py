import datetime
import svg_build
import shape

title = "divide"
x_in = 1024
y_in = 1024
origin = [512,512]

time = datetime.datetime.now()
string_time = time.strftime("%d-%m-%Y-%H-%M-%S")

name = (title + "_" + string_time)

svg_build.start(name, 0, x_in, y_in, "white")

sides = 8
division = 3

hexagon = shape.centre_polygon(origin, sides, 256)

perimeter_list = []

for x in range (0, len(hexagon)):
	line = shape.divide_line(hexagon[x], hexagon[x-1], division)
	print(line)
	svg_build.generate_path(line)
	perimeter_list.extend(line)

	
start = 0
end = 1

print(perimeter_list)

for side in range(0, len(perimeter_list), division):
	line = [perimeter_list[side + start], perimeter_list[side - end]]
	svg_build.generate_path(line)
	

svg_build.end()