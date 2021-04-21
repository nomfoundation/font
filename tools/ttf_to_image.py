#!/usr/bin/python
# -*- coding: utf-8 -*-
# import string
# import UnicodeUtilities
# 

# uses PIL aka Pillow (Python Imaging Library) to generate images from a TTF
# PIL documentation: https://pypi.org/project/Pillow/

import sys, codecs, argparse, os, errno
from PIL import Image, ImageDraw, ImageFont


def drawOneGlyph(uchar, code, font, color_scheme, image_format, draw, output_dir):
	w, h = draw.textsize(uchar, font=font)
	im = Image.new(color_scheme, (w, h))
	ImageDraw.Draw(im).text((-2, 0), uchar, font=font, fill="#000000")
	#im.show()
	image_name = output_dir+"/"+code+"."+image_format
	try:
		os.makedirs(output_dir)
	except OSError as e:
		if e.errno != errno.EEXIST:
			raise
	im.save(image_name)
	


def main():

	# for now, just assume some values
	point_size = 128
	color_scheme = "RGBA"
	image_format = "png"

	parser = argparse.ArgumentParser()
	parser.add_argument("char_and_code_file", help="tsv file with unicode characters and code points from which to generate images")
	parser.add_argument("font_name", help="name of the font to use, assume it's already installed")
	parser.add_argument("dir_name", help="name of directory to store the generated images")

	args = parser.parse_args()

	font = ImageFont.truetype(args.font_name, point_size)
	im = Image.new(color_scheme, (point_size, point_size))
	draw = ImageDraw.Draw(im)

	fileHandle = codecs.open(args.char_and_code_file, "r", "utf-8")
	for line in fileHandle.readlines():
		line = line.rstrip()
		fields = line.split("\t")
		uchar = fields[0]
		code = fields[1]
		drawOneGlyph(uchar, code, font, color_scheme, image_format, draw, args.dir_name)
		
	fileHandle.close()

if __name__ == '__main__':
	main()
