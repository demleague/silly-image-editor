import numpy as np
from PIL import Image
from bisect import bisect_left
import copy

def pixelate(image, amt):
    im = Image.open(image)
    w, h = im.size
    new_w = w * amt
    new_h = h * amt

    new_w = np.round(new_w)
    new_w = int(new_w)
    new_h = np.round(new_h)
    new_h = int(new_h)

    down_sampled = im.resize((new_w, new_h))
    up_sampled = down_sampled.resize((w, h), resample=4)

    up_sampled.save(image)
    print("done!")

def posterize(image_path, levels):
    'will do later lol...'


print("Welcome to demleague's silly image editor!")
imagePath = input("Enter the filename of the image you would like to edit: ")
print("If you want to pixelate the image enter 1")
print("If you want to posterize the image enter 2")
loop = True
while loop:
    x = int(input("Enter your choice: "))
    if x not in {1,2}:
        print("not a valid choice!")
    elif x == 1:
        amt = float(input("Enter the amount of downscaling: "))
        pixelate(imagePath, amt)
        loop = False
    elif x == 2:
        amt2 = int(input("Enter the amount of posterizing: "))
        posterize(imagePath, amt2)
        loop = False

print("Thank you for using demleague's silly image editor!")