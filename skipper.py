import os, sys
from utils import *
import shutil

def get_images(path, k):
	list = []
	for (dirpath, dirnames, filenames) in os.walk(path):
		for filename in filenames:
			if filename.endswith('.jpg'):
				list.append(join(dirpath, filename))
	return list[0::(k+1)]

def write_images(images, output_dir):
	try:
		shutil.rmtree(output_dir)
	except OSError:
		pass
	os.makedirs(output_dir)
	for i, image in enumerate(images):
		shutil.copy(image, output_dir)

if __name__ == "__main__":
	args = sys.argv
	if len(args) > 2:
		path = args[1]
		k = int(args[2])
		print(path, k)
	else:
		raise Exception('You must provide the path and the skipping factor!')

	output_dir = 'images_out'
	if len(args) > 3:
		output_dir = args[3]

	images = get_images(path, k)
	write_images(images, join_parent(output_dir))