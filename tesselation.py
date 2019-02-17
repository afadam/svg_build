import datetime
import svg_build
import shape
import palettes

title = "tesselation"
x_in = 1920
y_in = 1080
origin = [0,0]

time = datetime.datetime.now()
string_time = time.strftime("%d-%m-%Y-%H-%M-%S")

name = (title + "_" + string_time)

svg_build.start(name, 0, x_in, y_in, "white")

pattern = [[3,2,4],[0,3,3],[2,1,4],[3,2,3],[2,1,4],[0,3,6]]
column = ["a","b"]
palette = palettes.plt0
size = 24

p_i = 0
y_c = 1
col = 1

shapes = []

root_poly = shape.centre_polygon(origin, 6, size, -150)
shapes.append(root_poly)
rt = [root_poly[3],root_poly[2]]
										 
while origin[0] < x_in + size:
	col += 1
	col = col % len(column)
	
	while origin[1] < y_in + size/2:
		new_poly = shape.polygon(rt[0], rt[1], pattern[p_i][2])
		origin = shape.centre(new_poly)	
		shapes.append(new_poly)

		p_i = (p_i + 1) % len(pattern)
		rt_x = new_poly[pattern[p_i][0]]
		rt_y = new_poly[pattern[p_i][1]]
		rt = [rt_x, rt_y]
		y_c += 1

	if column[col] == "a":
		last_start = shapes[len(shapes) - y_c]
		new_start = shape.polygon(last_start[2], last_start[1], 4)
		shape.rotate(new_start, 90)
		shapes.append(new_start)
		origin = shape.centre(new_start)
	
		rt = [new_start[3],new_start[2]]
		y_c = 1
		p_i = 3
		
	if column[col] == "b":
		last_start = shapes[len(shapes) - y_c]
		new_start = shape.polygon(last_start[2], last_start[1], 6)
		shape.rotate(new_start, 120)
		shapes.append(new_start)
		origin = shape.centre(new_start)
		
		rt = [new_start[3],new_start[2]]
		y_c = 1
		p_i = 0

for _ in range(len(shapes)):
	if len(shapes[_]) == 6:
		svg_build.generate_path(
			shapes[_], fill=palette[3], st_w=4, st=palette[0])
		
	elif len(shapes[_]) == 4:
		svg_build.generate_path(
			shapes[_], fill=palette[1], st_w=4, st=palette[0])
		
	elif len(shapes[_]) == 3:
		svg_build.generate_path(
			shapes[_], fill=palette[2], st_w=4, st=palette[0])

svg_build.end()