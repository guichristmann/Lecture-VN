""" 
    This is an utility script to convert PDF slides to PNG images.
    When this is run it looks for every PDF inside "Slides/" folder,
    creates a new folder with the same filename and generates .PNG
    images for each page of the PDF.
"""

import sys
import os
from os import path
from glob import glob
import ghostscript
from PIL import Image

RENPY_RES = (1280, 720)

def pdf2png(pdf_input_path, output_path):
    # Set up arguments for conversion. Note that ghostscript requires
    # bytes and not strings. Kinda bothersome

    # Output path is encoded as bytes. Also using the %d notation
    # for generating image files.
    output_arg = str.encode("-o" + output_path + "/slide%000d.png")
    args = [b"",
            b"-dNOPAUSE",         # Don't pause between pages
            b"-sDEVICE=pngalpha", # Export format
            b"-r200",             # Resolution
            b"-dTextAlphaBits=4", # Antialiasing for text
            output_arg,           # Output argument
            str.encode(pdf_input_path)] # Byte encoded input
    # Call ghostscript
    ghostscript.Ghostscript(*args)

# Resize the images in specified folder to RenPy size (1280x720)
def resizePNGs(images_path):
    # Retrieve all .png inside folder
    image_fns = glob(images_path + "/*.png")

    for fn in image_fns:
        img = Image.open(fn)
        # TODO: I'm not sure the results will be good for images that are not
        # 16x8 already. Check other methods later, something that adds padding
        img.thumbnail(RENPY_RES, Image.ANTIALIAS)
        img.save(fn, "PNG")

# Folder to look for the PDFs
slides_path = "Slides/"

# Retrieve files and directories inside slides_path
dir_content = os.listdir(slides_path)

# Separate and retrieve directories and files
pdf_fns = []
directories = []
for e in dir_content:
    full_path = path.join(slides_path, e)
    if path.isfile(full_path):
        pdf_fns.append(full_path)
    elif path.isdir(full_path):
        directories.append(full_path)

# For each PDF file
for f in pdf_fns:
    # Directory name should be the same name as the filename, minus the .pdf
    # extension
    dir_path = f[:-4]
    if dir_path not in directories:
        print("Matching directory not found for {}.".format(f))
        print("Calling ghostscript to generate PNGs.\n")
        # Create the directory
        os.mkdir(dir_path)

        # Generate .PNGs from PDF using ghostscript
        pdf2png(f, dir_path)

        print("Resizing images to RenPy size...")
        # Resize the images to RenPy size (1280x720)
        resizePNGs(dir_path)
        print("Done.")
    else:
        print("Skipping {}. Matching directory found.\n".format(f))
