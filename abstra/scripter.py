import datetime
import svg_build
import shape
import palettes

title = "orb_liner6"
x_in = 1920
y_in = 1080
origin = [960,540]

layer = 0

for z in range (0, 720, 1):
	svg_build.start(title, layer, x_in, y_in, palettes.plt1[2])
 
	sides = 23

	hexagon = shape.centre_polygon(origin, sides, 468)

	perimeter_list = []

	for x in range (0, len(hexagon)):
		line = shape.divide_line(hexagon[x-1], hexagon[x], 6)
		perimeter_list.extend(line)

	shape.rotate(perimeter_list, z, shape.centre(perimeter_list))

	for y in range (1, len(perimeter_list)):	
		svg_build.generate_path([perimeter_list[y],perimeter_list[int(len(perimeter_list)/2) - y]],st_w=13,st=palettes.plt1[3],layer=layer)
	
	z2 = z * 3 
	
	shape.rotate(perimeter_list, z2, shape.centre(perimeter_list))

	for y in range (1, len(perimeter_list)):	
		svg_build.generate_path([perimeter_list[y],perimeter_list[int(len(perimeter_list)/2) - y]],st_w=5,st=palettes.plt2[1],layer=layer)

	layer = layer + 1
	
svg_build.end()