import pytesseract
from PIL import Image, ImageEnhance, ImageFilter
import cv2
import argparse
from skimage import io
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
    help = "Path to the image to be scanned")
args = vars(ap.parse_args())

im = io.imread(args["image"])
#im = Image.open('output.png') # the second one 
im = im.filter(ImageFilter.MedianFilter())
enhancer = ImageEnhance.Contrast(im)
im = enhancer.enhance(2)
im = im.convert('1')
im.save('output2.png')
text = pytesseract.image_to_string(Image.open('output.png'), config='--psm 11 --oem 3 ')
print(text)