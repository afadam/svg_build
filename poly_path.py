import datetime
import svg_build
import shape

title = "poly_path"
x_in = 1024
y_in = 1024
origin = [512,512]

time = datetime.datetime.now()
string_time = time.strftime("%d-%m-%Y-%H-%M-%S")

name = (title + "_" + string_time)

svg_build.start(name, 0, x_in, y_in, "white")

sides = 4

polygon = shape.centre_polygon(origin, sides, 256)

""" svg_build.generate_path(polygon, closed=True, fill="none", st_w=1, st="black", layer=0)"""

polygon_n1 = []
for _ in range(0, len(polygon)):
	vertex = shape.divide_line(polygon[_], polygon[_-1], 3)	
	if (_ % 2 == 1):
		polygon_n1.extend(vertex)
print(polygon_n1)

for _ in range(0, len(polygon_n1), 2):
	
	svg_build.generate_path(polygon_n1)

svg_build.end()