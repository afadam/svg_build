"""shape contains functions to build & manipulates lists of points representing
shapes and line segments.

pt 		- point 		- [x,y]
pt_list - point list	- [[x,y],[x1,y1],...,[xn,yn]]
"""
import math

def move(pt_list, x_shift=0, y_shift=0):
	"""
	pt_list,
	x_shift=0, y_shift=0
	"""
	if x_shift == 0 and y_shift == 0:
		print("Can't shift " + str(pt_list) + " by 0 in both dimensions.")
	else:
		for pt in pt_list:
			# increase each dimension by given shift
			pt[0] = pt[0] + x_shift
			pt[1] = pt[1] + y_shift

def rotate(pt_list, degrees, axis=[0,0]):
	"""
	pt_list, 
	degrees, 
	axis=[0,0]
	"""
	print(pt_list)
	if axis[1] == 0 and axis[0] == 0:
		axis = centre(pt_list)
	
	angle = math.pi/180 * degrees
	cos_t = math.cos(angle)	# cos theta 
	sin_t = math.sin(angle)	# sin theta
		
	for pt in pt_list:
		x_pt = (cos_t * (pt[0] - axis[0])) - (sin_t * (pt[1] - axis[1])) + axis[0]
		y_pt = (sin_t * (pt[0] - axis[0])) + (cos_t * (pt[1] - axis[1])) + axis[1]

		pt[0] = x_pt
		pt[1] = y_pt
		
def scale(pt_list, scale):
	"""
	pt_list, 
	scale
	"""
	print("scale function")
	origin = centre(pt_list)
	new_polygon = []
	
	for pt in range(0, len(pt_list)):
		
		new_pt = mid_point(pt_list[pt], origin)
		new_polygon.append(new_pt)
	
	return new_polygon

		
def centre(pt_list):
	"""Find and return the geometric centre point (average) of a list of points
	
	pt_list
	"""
	pts = len(pt_list)
	
	x_sum = 0
	y_sum = 0
	
	for pt in range(pts):
		x_sum += pt_list[pt][0]
		y_sum += pt_list[pt][1]
		
	centre = [x_sum / pts, y_sum / pts]
		
	return centre

def mid_point(pt1, pt2, factor=2):
	"""Find and return the point halfway between two other points
	
	pt1, pt2
	"""
	x_mid = (pt1[0] + pt2[0]) / factor
	y_mid = (pt1[1] + pt2[1]) / factor
	
	return [x_mid, y_mid]

def divide_line(pt1, pt2, factor=2, last_pt=True):
	"""Divide a line segment into equal lengths and return as a list of points.
	
	pt1, pt2,
	factor,
	curtail=False
	"""
	pt_list = [pt1]
	
	x_inc = (pt1[0] - pt2[0]) / factor
	y_inc = (pt1[1] - pt2[1]) / factor
	
	x_position_prev = pt1[0]
	y_position_prev = pt1[1]

	for new_pt in range (factor-1):
		
		x_position_prev -= x_inc
		y_position_prev -= y_inc
		
		pt_list.append([x_position_prev, y_position_prev])
	
	if last_pt:
		pt_list.append(pt2)
	
	return pt_list

def polygon(pt0, pt1, sides, flip=False):
	"""Draw a polygon of given sides when given two root points
	
	pt0, pt1,
	sides,
	flip=False
	"""
	# create list to hold points, reversing root if required	
	if flip:
		pt_list = [[pt1[0], pt1[1]],[pt0[0], pt0[1]]]
	else:	
		pt_list = [[pt0[0], pt0[1]],[pt1[0], pt1[1]]]
	
	# fill out list with placeholders
	for pt in range(sides-2):
		pt_list.append([0,0])
		
	# create angle
	angle = (math.pi * (sides - 2)) / sides
	
	# find length of side
	x_diff = (pt_list[1][0] - pt_list[0][0])
	y_diff = (pt_list[1][1] - pt_list[0][1])
	length = math.sqrt((x_diff*x_diff) + (y_diff*y_diff))

	# find the next point for every new side
	for pt in range(2, sides, 1):
		# examine previous line
		y_diff = (pt_list[pt-1][1] - pt_list[pt-2][1])
		x_diff = (pt_list[pt-1][0] - pt_list[pt-2][0])
		# find direction of previous vertex
		if (y_diff == 0):
			# y_diff of 0 is a horizontal line, x_diff gives direction
			theta = math.pi * (x_diff > 0)
		elif (x_diff == 0):
			# x_diff of 0 is a vertical line, y_diff gives direction
			theta = (math.pi/2) + (math.pi * (y_diff > 0))
		else:
			# otherwise use gradient to calculate direction
			m = y_diff/x_diff
			theta = math.atan(m) + (math.pi * (x_diff > 0))
		
		# final angle is difference of new and previous vertex
		add_angle = theta - angle 
		
		# calculate new point using trigonometry	
		pt_list[pt][0] = pt_list[pt-1][0] + (length * math.cos(add_angle))
		pt_list[pt][1] = pt_list[pt-1][1] + (length * math.sin(add_angle))

	return pt_list
	
def centre_polygon(origin, sides, height, orient=0):
	"""
	origin, 
	sides, 
	height,
	orient=0
	"""
	# create list to hold points of root line
	pt_list = [[0,0],[0,0]]
	
	# find internal angle of polygon, divide by two
	angle = math.pi / sides
	# convert orientation to radians
	orient = math.radians(orient) + math.pi/2
	
	# find root points using two back to back triangles of given height
	pt_list[0][0] = origin[0] + (height * math.cos(orient - angle))
	pt_list[0][1] = origin[1] + (height * math.sin(orient - angle))
	pt_list[1][0] = origin[0] + (height * math.cos(orient + angle))
	pt_list[1][1] = origin[1] + (height * math.sin(orient + angle))
	
	# pass root points to polygon() to populate polygon's points
	pt_list = polygon(pt_list[0], pt_list[1], sides)
	
	return pt_list

def triangle(pt0, pt1, height):
	"""
	pt0, pt1,
	height
	"""
	# create list to hold points, reversing root points if required	
	pt_list = [[pt0[0], pt0[1]]]
	
	# find midpoint of root line and add as third point
	pt_list.append(mid_line(pt0, pt1))
	
	# find angle of root line
	y_diff = (pt_list[1][1] - pt_list[0][1])
	x_diff = (pt_list[1][0] - pt_list[0][0])
	
	if (y_diff == 0):
		# y_diff of 0 is a horizontal line	
		theta = math.radians(180 * (x_diff > 0))
	elif (x_diff == 0):
		# x_diff of 0 is a vertical line
		theta = math.radians(90 + (180 * (y_diff > 0)))
	else:
		# otherwise use gradient to calculate
		m = y_diff/x_diff
		theta = math.atan(m) + math.radians(180 * (x_diff > 0))
	
	# perpendicular angle is theta + pi/2
	perp_angle = theta + (math.pi / 2)

	# calculate new point using trigonometry	
	pt_list[2][0] = pt_list[2][0] + (height * math.cos(perp_angle))
	pt_list[2][1] = pt_list[2][1] + (height * math.sin(perp_angle))
	
	return pt_list

def rhombus(pt0, pt1, angle, flip=False):
	"""
	pt0, pt1, 
	angle,
	flip=False
	"""
	if (angle >= math.pi):
		print(str(angle) + " is not an angle in a rhombus")
	elif (angle == math.pi/2):
		print("square")
		s_angle = math.pi/2
		p_angle = math.pi/2
	elif (angle != math.pi/2):
		p_angle = angle
		s_angle = math.pi - angle
	else:
		print(str(angle) + " is not an angle in a rhombus")
	
	# create list to hold points, reversing root if required	
	if flip:
		pt_list = [[pt1[0], pt1[1]],[pt0[0], pt0[1]]]
	else:	
		pt_list = [[pt0[0], pt0[1]],[pt1[0], pt1[1]]]
	
	# fill out list with placeholders
	for pt in range(2):
		pt_list.append([0,0])
	
	# find length of side
	x_diff = (pt_list[1][0] - pt_list[0][0])
	y_diff = (pt_list[1][1] - pt_list[0][1])
	length = math.sqrt((x_diff * x_diff) + (y_diff * y_diff))

	# examine root line
	y_diff = (pt_list[1][1] - pt_list[0][1])
	x_diff = (pt_list[1][0] - pt_list[0][0])
	# find direction of root line
	if (y_diff == 0):
		# y_diff of 0 is a horizontal line, x_diff gives direction
		theta = math.radians(180 * (x_diff > 0))
	elif (x_diff == 0):
		# x_diff of 0 is a vertical line, y_diff gives direction
		theta = math.radians(90 + (180 * (y_diff > 0)))
	else:
		# otherwise use gradient to calculate direction
		m = y_diff/x_diff
		theta = math.atan(m) + math.radians(180 * (x_diff > 0))
		
	# final primary angle is difference of new and previous vertex
	add_p_angle = theta - p_angle 
	add_s_angle = theta
	
	# calculate new points using trigonometry	
	pt_list[2][0] = pt_list[1][0] + (length * math.cos(add_p_angle))
	pt_list[2][1] = pt_list[1][1] + (length * math.sin(add_p_angle))
	pt_list[3][0] = pt_list[2][0] + (length * math.cos(add_s_angle))
	pt_list[3][1] = pt_list[2][1] + (length * math.sin(add_s_angle))

	return pt_list