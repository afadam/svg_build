class Polygon:
	def __init__(self, x1, y1, x2, y2, sides)
		self.x1 = x1
		self.y1 = y1
		self.x2 = x2
		self.y2 = y2
		self.sides = sides
		
		# create list
		points = [[x1, y1],[x2, y2]]
		
	def build(self):
	
		# fill out list with placeholders
		for pt in range(pts-2):
			points.append([0,0])

		# create angle
		angle = math.radians(((pts - 2) * 180) / pts)

		# find length of line
		x_l = (x2 - x1)
		y_l = (y2 - y1)
		length = math.sqrt((x_l * x_l) + (y_l * y_l))

		for pt in range(2, pts, 1):

			# set variables to previous vertex 
			x1 = points[pt-2][0]
			y1 = points[pt-2][1]
			x2 = points[pt-1][0]
			y2 = points[pt-1][1]

			# find gradient of previous vertex

			y_diff = (y2 - y1)
			x_diff = (x2 - x1)

			if (y_diff == 0):
				theta = math.radians(180 * (x_diff > 0))
			elif (x_diff == 0):
				theta = math.radians(90 + (180 * (y_diff > 0)))
			else:
				m = y_diff/x_diff
				theta = math.atan(m) + math.radians(180 * (x_diff > 0))

			add_angle = theta - angle 

			points[pt][0] = points[pt-1][0] + (length * math.cos(add_angle))
			points[pt][1] = points[pt-1][1] + (length * math.sin(add_angle))

	def draw(self, f = "none", s = "black", closed = 1):

		path.generate(points, f, s, c)
		
	def iterate(self, sides)