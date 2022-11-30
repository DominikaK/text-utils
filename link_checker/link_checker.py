"""
This script checks for image files that are not referenced anywhere in a set of markdown files.

To run the script, copy it to directory (e.g. "documentation"), and run:
python link_checker.py <folder-name>
for example:
python link_checker.py docs
"""

import os
import sys

# Get command-line argument containing the folder name
directory_name = sys.argv[1]
image_list = {}
page_list = []

# Create dictionary of all images
for root, dirs, files in os.walk(directory_name):
    for file in files:
        if file.endswith((".png", ".jpg", ".gif", ".svg")):
            image_list[file] = root

# Create list of all markdown pages
for root, dirs, files in os.walk(directory_name):
    for file in files:
        if file.endswith(".md"):
            page_list.append(os.path.join(root, file))

used_images = []
unused_images = []

# Find all images referred to in markdown files
for image in image_list:
    for page in page_list:
        with open(page, 'r', encoding="utf8") as infile:
            for line in infile:
                if image in line:
                    used_images.append(image)

# Create list of unused imageswith fill paths
for image in image_list:
    if image not in used_images:
        unused_images.append(image_list[image] + "\\" + image)

# Print output
if unused_images:
    print('The following images are not used in any of the markdown files:')
    for unused_image in unused_images:
        print(unused_image)
