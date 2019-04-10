import sys
import os
from glob import glob
import shutil
from distutils.dir_util import copy_tree
import re

class RenPyProjectCreator:
    """
    This class creates a project using the exported colab files, based on
    the template project at Resources/templateProject
    """

    TEMPLATE_PROJECT_PATH = "Resources/templateProject/"
    PROJECTS_PATH = "Projects/" # Root output directory

    def __init__(self, colabExportPath, renpyProjectName):
        # Folder contaning the exported files from colab (scripts and slide
        # images)
        self.colabExportPath = colabExportPath
        # Name of the project to be created
        self.renpyProjectName = renpyProjectName

        self.destinationPath = os.path.join(self.PROJECTS_PATH,
                renpyProjectName)

    def createProject(self):
        # First copy the template project to destination folder, essentially
        # creating the new project
        copy_tree(self.TEMPLATE_PROJECT_PATH, self.destinationPath)
        
        # Now copy the files exported from colab
        copy_tree(self.colabExportPath, self.destinationPath)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: python {sys.argv[0]} <colab-export-folder> <RenPy-project-name>")
        sys.exit(1)

    r = RenPyProjectCreator(sys.argv[1], sys.argv[2])
    r.createProject()
