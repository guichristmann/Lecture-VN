# Lecture-VN
Project for converting Lecture Slides into a more interactive format -- Lecture Visual Novels using Ren'Py. The idea is to adapt [Prof. Jacky Baltes' Lecture Slides](https://sites.google.com/site/jackybaltes/home/jacky-baltes-teaching) into Visual Novels, using the slides as backgrounds for interactive stories with nicely drawn characters from Prof. Guerra.
This is a WIP. This README should be updated as new ideas and functionalities are added.

# Structure
- `Projects/` -- The projects folder. Each lecture slide will be converted into a different project.
- `Resources/` -- Contains the resource files: the characters drawings.
	- `../ProfJB/` -- Images for **Prof. JB**. The only character we have for now.
- `Slides/` -- Contains the PDF slides, exported from Google Slides.
	
## Current Method
Google Slides can be exported as PDF files. PDF files can be converted into high quality .PNG images using *ghostscript* in Linux.

Run `convertPDFSlidesToPng.py` to extract .png images from the .pdf files inside `Slides/` into their own folder. 

#### Dependencies

- `pip install ghostscript`