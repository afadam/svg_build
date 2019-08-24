import svg_build
import shape
import palettes
import random

title = "tree"
x_in = 1920
y_in = 1080

origin = [(x_in/2),(y_in/2)]

frames = 1

def tree(root, size):

	end = [1,1]
	end[0] = (root[0] + (size * 0.61))
	end[1] = (root[1] + random.uniform(-2* size, 2* size))
	branch = [root, end]
	
	weight = int(size/10)
	
	svg_build.generate_path(branch, st_w = weight)
			  
	branch_size = size * 0.84	
	
	if (branch_size < 3):
		return
	else:
		branches = random.randrange(1, 3, 1)
		for x in range (0, branches, 1):
						
			branch_length = shape.divide_line(root, end, factor=10, last_pt=0)
			node = random.choice(branch_length)
		
			tree(node, branch_size)
		
for z in range (0, frames, 1):
	
	svg_build.start(title, z, x_in, y_in, fill="white")

	tree([0, 540], 540) 
		
	svg_build.end(z)
	

	