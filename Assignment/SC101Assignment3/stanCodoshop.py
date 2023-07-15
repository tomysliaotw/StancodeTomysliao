"""
File: stanCodoshop.py
Name: Tom Liao
----------------------------------------------
SC101_Assignment3 Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.
"""

import os
import sys
from simpleimage import SimpleImage
import math


# return RGB-Color-Distance to Average color
def get_pixel_dist(red, redA, green, greenA, blue, blueA):
    color_distance = math.sqrt((redA-red)**2+(greenA-green)**2+(blueA-blue)**2)
    return color_distance


# get R,G,B values of pixel in position (x,y) of all images
def get_all_rgb(x, y, images):
    red = []
    blue = []
    green = []
    for i in range(len(images)):
        image = images[i].get_pixel(x,y)
        red.append(image.red)
        blue.append(image.blue)
        green.append(image.green)
    return red, green, blue


# calculate average value of a List
def avg(a):
    avg = 0
    for i in a:
        avg+=i
    avg = avg/len(a)
    return avg


# return best pixel value by taking 2 pixels with minimal distance to average value.
def get_best_pixel(x, y, images):
    red, green, blue = get_all_rgb(x, y, images)
    distance = []
    good = []
    for i in range(len(images)):
        distance.append(get_pixel_dist(red[i], avg(red), green[i], avg(green), blue[i], avg(blue)))
    sm1, sm2 = sorted(distance)[0:2]  # pick smallest 2 distances
    for i in range(len(distance)):
        if distance[i] == sm1 or distance[i] == sm2:
            good.append(i)            # find index of smallest 2 distances
    return avg([red[good[0]], red[good[1]]]), avg([green[good[0]], green[good[1]]]), avg([blue[good[0]], blue[good[1]]])


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    
    # ----- YOUR CODE STARTS HERE ----- #
    # Write code to populate image and create the 'ghost' effect
    for x in range(width):
        for y in range(height):
            r, g, b = get_best_pixel(x, y, images)
            setter = result.get_pixel(x, y)
            setter.red = r
            setter.green = g
            setter.blue = b


    # ----- YOUR CODE ENDS HERE ----- #

    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images("hoover")
    solve(images)


if __name__ == '__main__':
    main()
