import sys
import os
from PIL import Image

folder = sys.argv[1] # taking arguments from the command line and assign them to variables
newfolder = sys.argv[2]

if not os.path.isdir(newfolder): #checking if required new folder exists to create it or not
    os.mkdir(newfolder)

os.chdir(folder) #changing current directory

files = os.listdir() #making a list with all nested files

for file in files:
   img = Image.open(file)
   root,ext = os.path.splitext(file) #separating file name from extension
   img.save(f'..\{newfolder}\{root}.png', 'png') #saving the converted image to a different folder


