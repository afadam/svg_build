import datetime
import svg_build
import shape
import palettes
import random
import funcs

title = "hamfisted"
x_in = 1024
y_in = 1024
origin = [512, 512]

p = palettes.plt12

time = datetime.datetime.now()
string_time = time.strftime("%d-%m-%Y-%H-%M-%S")
name = (title + "_" + string_time)
svg_build.start(name, 0, x_in, y_in, p[0])


polygon = shape.centre_polygon(origin, 17, 480)
funcs.point_plotter(polygon)
kerneled = funcs.kernel(polygon, 0)

#svg_build.generate_path(polygon, st=p[4], st_w=2)

for f in range(0, len(kerneled)):
	svg_build.generate_path(kerneled[f], st=p[4], st_w=5, fill=p[2])
	svg_build.generate_path(funcs.star(kerneled[f]), st=p[4], st_w=5, fill=p[1])
#new_polygon = funcs.star(polygon)
					
#svg_build.generate_path(new_polygon, st=p[4], st_w=5)

svg_build.end()				