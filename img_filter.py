import os
from utils import *
import cv2,sys
if len(sys.argv) > 2:
	path = sys.argv[1];
	threshold = float(sys.argv[2])
else:
	raise Exception('Please provide the input path & threshold as system arguements')
F = [];
for (dirpath,dirnames,filenames) in os.walk(path):
	F.extend(filenames);
	break;

lst = None;
save_path = join_parent("filter_output");
make_dir(save_path)
F.sort();
for img_name in F:
	img = cv2.imread(join(path, img_name), 0);
	if lst is None:
		lst = cv2.imread(join(path, img_name), 0);
		cv2.imwrite(join(save_path, img_name), cv2.imread(join(path, img_name)));
	else:
		diff = sum(sum(abs(lst - img)));
		siz = img.shape[0]*img.shape[1];
		print (diff*1.0/siz);
		if diff > threshold*siz:
			lst = cv2.imread(join(path, img_name), 0);
			cv2.imwrite(join(save_path, img_name), cv2.imread(join(path, img_name)));
