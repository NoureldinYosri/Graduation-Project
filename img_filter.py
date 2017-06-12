from os import walk
import cv2
path = "G:\\New\\aaaa";
F = [];
for (dirpath,dirnames,filenames) in walk(path):
	F.extend(filenames);
	break;

lst = None;
save_path = "G:\\New\\filter_output\\france\\";
threshold = 0.48;
F.sort();
for img_name in F:
	img = cv2.imread(path + '\\' + img_name,0);
	if lst is None:
		lst = cv2.imread(path + '\\' + img_name,0);
		cv2.imwrite(save_path + img_name,cv2.imread(path + '\\' + img_name));
	else:
		diff = sum(sum(abs(lst - img)));
		siz = img.shape[0]*img.shape[1];
		print (diff*1.0/siz);
		if diff > threshold*siz:
			lst = cv2.imread(path + '\\' + img_name,0);
			cv2.imwrite(save_path + img_name,cv2.imread(path + '\\' + img_name));
