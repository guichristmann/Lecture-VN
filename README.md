# Lecture-VN
Project for converting Lecture Slides into a more interactive format -- Lecture Visual Novels using Ren'Py. The idea is to adapt [Prof. Jacky Baltes' Lecture Slides](https://sites.google.com/site/jackybaltes/home/jacky-baltes-teaching) into Visual Novels, using the slides as backgrounds for interactive stories with nicely drawn characters from Prof. Guerra.
This is a WIP. This README should be updated as new ideas and functionalities are added.

# Structure
- `Projects/` -- The projects folder. Each lecture slide will be converted into a different project.
- `Resources/` -- Contains the resource files: the characters drawings.
	- `../ProfJB/` -- Images for **Prof. JB**. The professor character.
	- `../MrC/` -- Images for **Mr. C**. One of the student characters.
	- `../templateProject/` -- The template project. All generated projects come from this one.
- `Slides/` -- Contains the PDF and extracted PNG slides.
	
## Current Method
Google Slides can be exported as PDF files. PDF files can be converted into high quality .PNG images using *ghostscript* in Linux.

Run `convertPDFSlidesToPng.py` to extract .png images from the .pdf files inside `Slides/` into their own folder. 

Run `createRenPyProjectFromSlides.py <PNG-slides-folder> <project-name>` to create a new project from the PNG images.

To edit a project open `"ProjectName"/game/script.rpy`. All characters and slides should already be included.

#### Dependencies

- `pip install ghostscript`
