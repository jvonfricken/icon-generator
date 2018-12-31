from PIL import Image

import argparse
import json
import sys

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", help="file name of icon")
parser.add_argument("-n", "--newfile",
                    help="overrides the file name during saving")


def get_file_name():
    args = parser.parse_args()

    if args.newfile:
        return args.file, args.newfile

    if args.file:
        return args.file, args.file


def main():
    file_name, new_file_name = get_file_name()

    image = Image.open(file_name)

    image_width, image_height = image.size

    for i in range(1, 4):
        devisor = 4 - i
        resized_image = image.resize(
            (int(image_width/devisor), int(image_height/devisor)), Image.LANCZOS)
        resized_image.save(new_file_name.replace(
            ".png", "@{size}x.png".format(size=str(i))))


if __name__ == "__main__":
    main()
