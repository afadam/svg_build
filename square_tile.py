import datetime
import svg_build
import shape

title = "squaretile"
x_in = 1024
y_in = 1024
origin = [0,0]

time = datetime.datetime.now()
string_time = time.strftime("%d-%m-%Y-%H-%M-%S")

name = (title + "_" + string_time)

svg_build.start(name, 0, x_in, y_in, "white")

shapes = []
root_square = shape.polygon([0,0],[128,0],4)
shape.move(root_square)
shapes.append(root_square)
origin = shape.centre(root_square)
rt1 = root_square[3]
rt2 = root_square[2]
y_c = 1

while origin[0] < x_in:

	while origin[1] < y_in:
		new_square = shape.polygon(rt1, rt2, 4)
		shapes.append(new_square)
		origin = shape.centre(new_square)
		rt1 = new_square[3]
		rt2 = new_square[2]
		print(new_square)
		y_c += 1

	last_start = shapes[len(shapes) - y_c]
	new_start = shape.polygon(last_start[2], last_start[1], 4)
	shape.rotate(new_start, 90)
	shapes.append(new_start)
	origin = shape.centre(new_start)
	
	rt1 = new_start[3]
	rt2 = new_start[2]
	y_c = 1

for x in range(len(shapes)):
	if x % 2 == 0:
		svg_build.generate_path(shapes[x], fill="black")
	elif x % 2 != 0:
		svg_build.generate_path(shapes[x], fill="none")

svg_build.end()