import svg_build
import shape
import palettes
import random

title = "tree"
x_in = 1920
y_in = 1080

origin = [(x_in/2),(y_in/2)]

frames = 1

planted = [960, 1080]

def tree(root, size):

	end = [1,1]
	end[0] = (root[0] + random.uniform(-2* size, 2* size))
	end[1] = (root[1] - (size * 0.38))

	branch = [root, end]
	
	weight = int(size/10)
	
	svg_build.generate_path(branch, st_w = weight)
			  
	branch_size = size * 0.84	
	
	if (branch_size < 32):
		return
	else:
		
		tree(end, branch_size)
		
		branches = random.randrange(0, 3, 1)
		for x in range (0, branches, 1):
						
			branch_length = shape.divide_line(root, end, factor=10, last_pt=0)
			node = random.choice(branch_length)
		
			tree(node, branch_size)
			
		
for z in range (0, frames, 1):
	
	svg_build.start(title, z, x_in, y_in, fill="white")

	tree(planted, 540) 
		
	svg_build.end(z)
	

	