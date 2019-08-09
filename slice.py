import os
from PIL import Image
import image_slicer
#slicing of cropped image into 100 parts
tiles=image_slicer.slice('./201/01-17-2018.jpg', 70, save=False)
image_slicer.save_tiles(tiles, directory='./201/01-17-2018/',\
	prefix='01', format='jpeg')
