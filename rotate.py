from os import listdir
from PIL import Image as PImage
import cv2
import numpy as np
from skimage.io import imread

def loadImages(path):
    # return array of images

    imagesList = listdir(path)
    loadedImages = []
    op=[]
    i=1
    for image in imagesList:
        #img=PImage.open(path + image)
        cI=PImage.open(path + image)
        rot=cI.rotate(12.5)
        #rot.save('./20/r.jpg')
        #img=PImage.open('./20/r.jpg')
        area =(679,639,6998,7208)
        cr=rot.crop(area)
        area1 =(4050,900,5200,2650)
        cr1=cr.crop(area1)
        n='./Mum_rotated/2019/'+image
        cr1.save(n)
        i=i+1
        #loadedImages.append(cam1)

    return loadedImages,op

path = "./MUMBAI/2019/"

# your images in an array
opt = loadImages(path)
