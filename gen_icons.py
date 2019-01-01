from PIL import Image

import argparse
import json
import sys

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", help="file name of icon")
parser.add_argument("-n", "--newfile",
                    help="overrides the file name during saving")
parser.add_argument("-c", "--config", help="utilizes config file to generate icons and icon names", action="store_true")


def get_file_name():
    args = parser.parse_args()

    if args.newfile:
        return args.file, args.newfile

    if args.file:
        return args.file, args.file

def use_config_file():
    args = parser.parse_args()

    return args.config

def generate_icons_config(image):

    config = {}
    with open("config.json", "r") as file:
        data = file.read()

        config = json.loads(data)

    for size in config["sizes"]:
        resized_image = image.resize((size["res"], size["res"]), Image.LANCZOS)
        resized_image.save(size["name"])

def generate_icons(file_name, new_file_name, image):
    image_width, image_height = image.size

    for i in range(1, 4):
        height = width = int((image_width/3)*i)

        resized_image = image.resize((width, height), Image.LANCZOS)
        resized_image.save(new_file_name.replace(
            ".png", "@{size}x.png".format(size=str(i))))

def main():
    file_name, new_file_name = get_file_name()
    image = Image.open(file_name)
    if use_config_file:
        generate_icons_config(image)
    else:
        generate_icons(file_name, new_file_name, image)



if __name__ == "__main__":
    main()
