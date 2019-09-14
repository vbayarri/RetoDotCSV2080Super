import os
import shutil

from PIL import Image

source = 'samples/'
target = "samplesRGB/"

cwd = os.getcwd()

pathsource = os.path.join(cwd, source)
pathtarget = os.path.join(cwd, target)

def convertImage(r, file):
    
	img = Image.open(os.path.join(r,file)).convert('RGB')
	img.save(os.path.join(target, file))

def convertRGB():
	# Clear output directory
	shutil.rmtree(pathtarget, ignore_errors=True)
	os.mkdir(pathtarget)	

	# r=root, d=directories, f = files
	for r, d, f in os.walk(pathsource):
		for file in f:
			if '.jpg' in file:
				convertImage(r, file)

if __name__ == '__main__':
	convertRGB()