"""
    This is an utility script to generate a template Ren'Py project. After
    generating PNG image files, pass the folder as argument to this script.
    A project will be created with resources already imported, including
    characters, slides (backgrounds) and a basic template for the game.
    The new project will be created under Projects/, and to edit it, it is only
    needed to modify the script.rpy file.
"""

import sys
import os
from glob import glob
import shutil
import re

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    '''
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]

if len(sys.argv) != 3:
    print("Usage: python {} <PNG-slides-folder> <project-name>"\
          .format(sys.argv[0]))
    sys.exit(1)

TEMPLATE_PROJECT_PATH = "Resources/templateProject/"
PROJECTS_PATH = "Projects/"

# Relative to project root
BACKGROUNDS_SCRIPT_PATH = "game/backgrounds.rpy" 
MAIN_SCRIPT_PATH = "game/script.rpy" 
BACKGROUNDS_PATH = "game/images/Backgrounds/" 

# Folder containing the slides in .png format
slides_path = sys.argv[1]
# Name for the project
project_name = sys.argv[2]
# Path for every slide in .png
images_path = glob(slides_path + "/*.png")

# Root of the newly created proect
destination_path = os.path.join(PROJECTS_PATH, project_name) 

print("Copying template files to {}...".format(destination_path))
shutil.copytree(TEMPLATE_PROJECT_PATH, destination_path)

print("Copying images (slides) to {}".format(destination_path))
# Open backgrounds.rpy file to include the location of the copied slides
backgrounds_script = open(os.path.join(destination_path, 
                                       BACKGROUNDS_SCRIPT_PATH),
                          "a")

# Also open script.rpy to include some template text and transitions for all
# the slides
main_script = open(os.path.join(destination_path, MAIN_SCRIPT_PATH), "a")

# Iterate over all images
for f in sorted(images_path, key=natural_keys):
    fn = f.split('/')[-1] # Filename of copied slide
    shutil.copy(f, os.path.join(destination_path, BACKGROUNDS_PATH)) # Copy
                                                                     # slide

    # Include slide in backgrounds.rpy, so it can be used in the project
    line = "image bg " + fn.strip('.png') + " = \"images/Backgrounds/" + fn +\
           "\"\n"

    # Write new background
    backgrounds_script.write(line)

    fn = fn.strip('.png')
    # Text template for script.rpy
    text = "\nlabel {}:".format(fn)
    text += "\n    scene bg {} with fade".format(fn)
    text += '\n    jb "This is {}"'.format(fn)
    text += "\n"

    main_script.write(text)
