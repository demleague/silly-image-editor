import numpy as np
from PIL import Image, ImageEnhance
from bisect import bisect_left
import copy

def pixelate(image, amt):
    output_path = input("Enter the output path: ")
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

    up_sampled.save(output_path)
    print("done!")

def posterize(image_path, levels):
    output_path = input("Enter the output path: ")
    im = Image.open(image_path)
    im = im.convert("RGB")
    step = 256 // levels
    for y in range(im.height):
        for x in range(im.width):
            r, g, b = im.getpixel((x, y))
            r = int((r // step) * step)
            g = int((g // step) * step)
            b = int((b // step) * step)
            im.putpixel((x, y), (r, g, b))

    im.save(output_path)
    print("done!")

def brightness(image_path, value):
    output_path = input("Enter the output path: ")
    im = Image.open(image_path)
    width, height = im.size
    im_adjusted = Image.new(im.mode, (width, height))
    for y in range(im.height):
        for x in range(im.width):
            r, g, b = im.getpixel((x, y))
            r = int(min(r * value, 255))
            g = int(min(g * value, 255))
            b = int(min(b * value, 255))
            im_adjusted.putpixel((x, y), (r, g, b))
    im_adjusted.save(output_path)
    print("done!")



print("Welcome to demleague's silly image editor!")

loop = True
while loop:
    print("Choose an option:")
    print("1. Pixelate the image")
    print("2. Posterize the image")
    print("3. Change image brightness")
    print("4. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        imagePath = input("Enter the filename of the image you would like to edit: ")

        amt = float(input("Enter the amount of downscaling: "))
        pixelate(imagePath, amt)

    elif choice == 2:
        imagePath = input("Enter the filename of the image you would like to edit: ")
        amt2 = int(input("Enter the amount of posterizing: "))
        posterize(imagePath, amt2)

    elif choice == 3:
        imagePath = input("Enter the filename of the image you would like to edit: ")
        amt3 = float(input("Enter the brightness value as a multiple of the original: "))
        brightness(imagePath, amt3)

    elif choice == 4:
        loop = False
        print("Exiting the editor.")
    else:
        print("Invalid choice.")

print("Thank you for using demleague's silly image editor!")