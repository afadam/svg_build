import datetime
import svg_build
import shape
import palettes
import random
import funcs

title = "blackandwhite2"
x_in = 1024
y_in = 1024

p = palettes.plt12

time = datetime.datetime.now()
string_time = time.strftime("%d-%m-%Y-%H-%M-%S")
name = (title + "_" + string_time)
svg_build.start(name, 0, x_in, y_in, p[0])

polygon = shape.centre_polygon([512, 512], 11, 480)
svg_build.generate_path(polygon, st=p[4], st_w=5)

segments = funcs.kernel(polygon)

for segment in range(0, len(segments)):
	svg_build.generate_path(segments[segment], st=p[4], st_w=5)
	new_segments = funcs.kernel(segments[segment])

	for new_segment in range(0, len(new_segments)):
		svg_build.generate_path(new_segments[new_segment], st=p[4], st_w=5, fill=p[(new_segment % 2)])
		if new_segment % 3 == 2:
			kernels = funcs.kernel(new_segments[new_segment])
			for kernel in range(0, len(kernels)):
				svg_build.generate_path(kernels[kernel], st="none", fill=p[(kernel % 2)])
		
svg_build.end()				