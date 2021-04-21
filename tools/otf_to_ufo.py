#!/usr/bin/python
# -*- coding: utf-8 -*-

# uses functionality of defcon: https://pypi.org/project/defcon/
# pip install --upgrade defcon

import argparse
import extractor
import defcon


def main():

	parser = argparse.ArgumentParser()
	parser.add_argument("file", help="path input otf file")
	args = parser.parse_args()

	ufo = defcon.Font()
	extractor.extractUFO(args.file, ufo)
	outputfileName = args.file.replace(".otf", ".ufo")
	
	print("saving %s to %s\n" % (args.file, outputfileName))
	ufo.save(outputfileName)

if __name__ == '__main__':
	main()
