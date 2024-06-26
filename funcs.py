import shape

def firein(polygon, levels):
	
	point_list = []
	origin = shape.centre(polygon)
	
	for pt in range(0, len(polygon)):
		
		axle = shape.divide_line(polygon[pt], origin, levels, last_pt=False)
		
		for new_pt in range(0, len(axle)):
			point_list.append(axle[new_pt])
	
	polygon_list = []
	
	for level in range(1, levels):
		
		new_polygon = []		
		for pt in range(level, len(point_list), levels):
			new_polygon.append(point_list[pt])
	
		polygon_list.append(new_polygon)
	
	return polygon_list

def kernel(kernel_list, recurse):
	
	sides = len(kernel_list)
	
	segment_list = []
	
	for x in range(0, sides):
		segment = []
		segment.append(shape.centre(kernel_list))
		segment.append(kernel_list[(x - 1) % sides])
		segment.append(kernel_list[(x) % sides])
		
		if recurse > 0:
			recurse_n = recurse - 1
			kernel(segment, recurse_n)
		else:
			segment_list.append(segment)
				   
	return segment_list

def slice(slice_shape):

	slice_list = []

	for x in range(0, len(slice_shape)):
		edge = shape.divide_line(slice_shape[x], slice_shape[(x + 1) % len(slice_shape)], 2, False)

		for y in range (0, 2):
			slice_list.append(edge[y])

	return slice_list
	
def grid(x):
	x_in = 1920
	y_in = 1080

	time = datetime.datetime.now()
	string_time = time.strftime("%d-%m-%Y-%H-%M-%S")
	name = (title + "_" + string_time)
	svg_build.start(name, 0, x_in, y_in, "white")

	x_n = 12
	y_n = 4
	x_size = x_in / x_n
	y_size = y_in / y_n

	target_list = []

	for x in range(0, x_n + 1):
		for y in range(0, y_n + 1):
			point = [x*x_size, y*y_size] 
			target_list.append(point)	

def star(polygon):
	
	new_polygon = []
	origin = shape.centre(polygon)
	
	for edge in range(0, len(polygon)):
		segment = [polygon[edge],origin,polygon[(edge+1) % len(polygon)]]
		
		middle = shape.centre(segment)
		new_polygon.append(segment[0])
		new_polygon.append(middle)
		
	return new_polygon