"""
This script performs a replace over all markdown files in a directory nd its subdirectories.
It replaces *single words* with *single words* from a list provided in "name_changes.txt", in the form:

word newword
another_word_to_change another_new_word

To run the script, copy it to your directory (e.g. "documentation"), and run:
python replacer.py <folder-name>
for example:
python replacer.py docs
"""

import os
import sys

# Read list of terms to replace from file
map = {}
with open('name_changes.txt') as map_file:
    for line in map_file:
        (key, val) = line.split()
        map[key] = val

# Get command-line argument containing the folder name
directory_name = sys.argv[1]

# List all files in directory
for root, dirs, files in os.walk(directory_name):
    for filename in files:
        if filename.endswith(".md"):
            # Create full path for each markdown file
            path = os.path.join(root, filename)
            with open(path, 'r') as file:
                try:
                    # Read and replace terms from the list
                    filedata = file.read()
                    for key, value in map.items():
                        filedata = filedata.replace(key, value)
                except:
                    print("Problem with file " + filename)
            with open(path, 'w') as file:
                # Write changes to file
                file.write(filedata)
