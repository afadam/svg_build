import datetime
import svg_build
import shape

title = "divide"
x_in = 1920
y_in = 1080
origin = [960, 540]

time = datetime.datetime.now()
string_time = time.strftime("%d-%m-%Y-%H-%M-%S")

name = (title + "_" + string_time)

svg_build.start(name, 0, x_in, y_in, "white")

sides = 6
division = 3

hexagon = shape.centre_polygon(origin, sides, 480)

perimeter_list = []

for x in range (0, len(hexagon)):
	line = shape.divide_line(hexagon[x], hexagon[(x+1) % len(hexagon)], division, last_pt=False)
	perimeter_list.extend(line)

for y in range (1, len(perimeter_list)+1):
	svg_build.generate_text(perimeter_list[y-1], y, size=36)

svg_build.end()