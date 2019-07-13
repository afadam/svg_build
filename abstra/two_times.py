import svg_build
import shape
import palettes

import random

r = lambda: random.randint(0,255)

colour = '#%02X%02X%02X' % (r(),r(),r())

title = "mondays2"

x_in = 1920
y_in = 1080

corners = [[0,0],[x_in,0],[x_in,y_in],[0,y_in]]
perimeter_list = []

for x in range (0, 4):
	line = shape.divide_line(corners[x-1], corners[x], 128, False)
	perimeter_list.extend(line)
	print(corners[x])
	
print(len(perimeter_list))
print(perimeter_list)

for x in range(0, len(perimeter_list)):
	
	svg_build.start(title, x, x_in, y_in, fill='#%02X%02X%02X' % (r(),r(),r()))
	
	for y in range(0, len(perimeter_list), 16):
		for z in range(0, 16):
			pt1 = perimeter_list[y+z] 
			pt2 = perimeter_list[-y-z]

			path=[pt1,pt2]

			svg_build.generate_path(path, st_w=16, st='#%02X%02X%02X' % (r(),r(),r()), layer=x)

for x in range(0, len(perimeter_list)):
	svg_build.end(x)