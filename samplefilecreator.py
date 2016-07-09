#!/usr/bin/env python

import argparse
import textwrap
import os
from sys import argv
from PIL import Image

def create_bg_file(path, filenames):
    print("[*] Creating bg file...")
    file_path = path + "bg.txt"
    img_path = path + "neg/"
    with open(file_path, "w") as f:
        for img in filenames:
            str_to_write = "neg/" + img + "\n"

            f.write(str_to_write)
            print("\tAdded: ", str_to_write, end="")

def create_positive_file(path, filenames):
    print("[*] Creating positive file...")
    print("\tAssuming object covers the whole picture and just one object...")

    # only add if it contains just one object!
    file_path = path + "info.dat"
    img_path = path + "pos/"
    with open(file_path, "w") as f:
        for img in filenames:
            next_img = img_path + img
            size = get_image_size(next_img)
            str_to_write = "pos/" + img + " 1" + " 0 0 " + str(size[0]) + " " + str(size[1]) + "\n"

            f.write(str_to_write)
            print("\tAdded: ", str_to_write, end="")

def get_image_size(img_path):
    with Image.open(img_path) as im:
        return im.size

def get_all_png_files(dir_path):
    print("[*] Getting all png files at: ", dir_path)
    png_files = []
    for f in os.listdir(dir_path):
        if f.endswith(".png"):
            png_files.append(f)
            print("Found: ", f)

    return png_files

def get_all_jpg_files(dir_path):
    print("[*] Getting all jpg files at: ", dir_path)
    jpg_files = []
    for f in os.listdir(dir_path):
        if f.endswith(".jpg") or f.endswith(".jpeg"):
            jpg_files.append(f)
            print("\tFound: ", f)

    return jpg_files

def get_mean_size(dir_path, filenames):
    print("[*] Getting mean size of images...")
    sum_width = 0
    sum_height = 0
    img_count = 0
    mean_width = 0
    mean_height = 0

    for filename in filenames:
        img_path = dir_path + filename
        size = get_image_size(img_path)
        sum_width += size[0]
        sum_height += size[1]
        img_count += 1

    if img_count < 1:
        print("[!] Error in get_mean_size: No images given.")
        return(1)

    mean_width = sum_width / img_count
    mean_height = sum_height / img_count
    print("\tMean in (width, height)")
    print("\tFloat:   ({}, {})".format(mean_width, mean_height))
    print("\tInteger: ({}, {})".format(round(mean_width), round(mean_height)))

    return [round(mean_width), round(mean_height)]


def resize_images(path, dir_path, filenames, new_size):
    print("[*] Resizing positive images...")
    print("\tNew size is:", new_size)
    # do not overwrite images, so create another dir where to save them if it does not exists
    new_dir = path + "pos_resized/"
    if not os.path.exists(new_dir):
        os.makedirs(new_dir)
    # writes new images in pos_resized, only resizing positive images right now
    for filename in filenames:
        img_path = dir_path + filename
        img_new_path = new_dir + filename
        with Image.open(img_path) as img_in:
            img_out = img_in.resize(new_size)
            img_out.save(img_new_path)

    print("\tFinished resizing.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(add_help=False, formatter_class=argparse.RawDescriptionHelpFormatter, description=textwrap.dedent('''\
        Directory structure:
            /dir
                /neg
                    img1.jpg
                    img2.jpg
                /pos
                    img1.jpg
                    img2.jpg
        '''))
    parser.add_argument("--help", action="help", help="show this help message and exit")
    parser.add_argument("-p", "--path", nargs="?", default=os.getcwd(), type=str, help="path to dir to process or current path of script is used")
    parser.add_argument("--jpg", action="store_true", help="file output is jpg (default)")
    parser.add_argument("--png", action="store_true", help="file output is png")
    parser.add_argument("--neg", action="store_true", help="generate bg file for negative images")
    parser.add_argument("--pos", action="store_true", help="generate file for positive images (default)")
    parser.add_argument("-w", "--width", nargs="?", default=0, type=int, help="width of resized images")
    parser.add_argument("-h", "--height", nargs="?", default=0, type=int, help="height of resized images")
    parser.add_argument("-m", "--mean", action="store_true", help="use mean size of old images for resized images")

    parser.print_help()
    args = parser.parse_args()

    path = args.path
    if not path.endswith("/"):
        path = path + "/"
    width = args.width
    height = args.height

    if args.neg:
        dir_path = path + "neg/" # generate the bg file
    else:
        dir_path = path + "pos/" # generate the info.dat file

    if args.png:
        filenames = get_all_png_files(dir_path)
    else:
        filenames = get_all_jpg_files(dir_path)

    if args.neg:
        create_bg_file(path, filenames) # generate the bg file
    else:
        create_positive_file(path, filenames) # generate the info.dat file

    # only resize positive images
    if args.pos:
        if (width is 0) or (height is 0):
            if args.mean:
                resize_size = get_mean_size(dir_path, filenames)
                width = resize_size[0]
                height = resize_size[1]

        if ((width is not 0) and (height is not 0)):
            resize_images(path, dir_path, filenames, (width, height))