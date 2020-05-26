#Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process enable allow
import os
import sys
import random

vipshome = 'C:\\Program Files\\vips\\bin'
os.environ['PATH'] = vipshome + ';' + os.environ['PATH']
import pyvips
import argparse


parser = argparse.ArgumentParser(description='Get image dimensions')
parser.add_argument('-p',"--path_in", required=True, type = str,
	help="path to input image")
parser.add_argument('-dpi', type = int,
	help="svg DPI loading of ingnput image")
inputs = parser.parse_args()

if inputs.dpi is not None:
    dpi= inputs.dpi
else:
    dpi = 1440

path = inputs.path_in
if  path.endswith('.svg') and os.path.isfile(path):
	img = pyvips.Image.svgload(path, dpi = dpi)
else:	
	img = pyvips.Image.new_from_file(path)
path= path.lower()

print("width_px:", img.width)
print("height_px:", img.height)
print("dpmm_x:", img.xres)
print("dpmm_y:", img.yres)
print("width_mm:", img.width/img.xres)
print("height_mm:", img.height/img.yres)
print("dpi_x:", img.xres/(1/25.40))
print("dpi_y:", img.yres/(1/25.40))