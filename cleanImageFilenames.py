''' Each component of a character (i.e. eyes, arms, etc.) is a different layer
    in ProCreate. In order to get separate images for each layer, the drawing
    is imported into Photoshop, and then each layer is exported as a separate
    image. The problem is that Photoshop saves the filenames in the format
    NAME_XXXX_LAYERNAME.png, where XXXX is a number. So if a new layer is made
    and the whole export process is done again, it will change the filename.
    This script receives a folder as an argument and removes the XXXX number.
    It's also safe to run several times on the same folder.
'''

import sys
import glob
import os
import re

if len(sys.argv) != 2:
    print("Usage: {} <folder containing images>".format(sys.argv[0]))
    sys.exit(1)

REGEX = '\_+\w[0-9]+' # Matches '_XXXX', where XXXX is any number

# Get folder path from cmd line
folder_path = sys.argv[1]

# Retrieve the full path for all images in folder
images_path = glob.glob(sys.argv[1] + "/*.png") # Checking only for .PNG images

# Iterate over all images
for img_path in images_path:
    # Get filename for current img
    img_fn = img_path.split('/')[-1]
    # Remove the XXXX number using regex
    new_fn = re.sub(REGEX, '', img_fn)
    # Rename the file
    os.rename(folder_path + img_fn, folder_path + new_fn)
