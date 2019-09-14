import os
import shutil

from PIL import Image, ImageDraw, ImageFont

source = 'samples/'
target = "target/"

cwd = os.getcwd()

pathsource = os.path.join(cwd, source)
pathtarget = os.path.join(cwd, target)

fnt = ImageFont.truetype('/Library/Fonts/Arial_Bold.ttf', 36)

def generateImage(code):
    img = Image.new('RGB', (200, 50), color='white')

    d = ImageDraw.Draw(img)
    d.text((30, 5), code, font=fnt, fill=(0, 0, 0))

    img.save(os.path.join(target, str(code) + ".jpg"))

def generateImages():
	# Clear output directory
	shutil.rmtree(pathtarget, ignore_errors=True)
	os.mkdir(pathtarget)	

	# r=root, d=directories, f = files
	for r, d, f in os.walk(pathsource):
		for file in f:
			if '.jpg' in file:
				filename, file_extension = os.path.splitext(file)
				generateImage(filename)

if __name__ == '__main__':
	generateImages()