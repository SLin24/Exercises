""" 
Using the two blocks of code below, create a window that creates a folder, and creates a file with content from the window.

"""
# https://automatetheboringstuff.com/2e/chapter9/

# Using pathlib and OS to create directories and add files
from pathlib import Path
import os



# using tkinter to create a usable window
#Import the required Libraries
from tkinter import *
from tkinter import ttk

#Create an instance of tkinter frame
win = Tk()
#Set the geometry of tkinter frame
win.geometry("750x250")

#Define a function to show a message
def myclick():
    # get all the values from the input boxes
    message= "File Supposedly Created?"
    folderName = entryFolder.get()
    fileName = entryFile.get()
    txt = entryTxt.get()
    fileType = entryFileType.get()
    filePath = entryDir.get()

    label= Label(frame, text= message, font= ('Times New Roman', 14, 'italic'))
    entryFolder.delete(0, 'end')
    entryFile.delete(0, 'end')
    entryTxt.delete(0, 'end')
    entryFileType.delete(0, 'end')
    entryDir.delete(0, 'end')

    # creating the file and preventing the creation of duplicate folders / files
    os.chdir(filePath)
    path = filePath + '\\' + folderName + '\\'
    if (not os.path.exists(path)):
        os.makedirs(path)

    os.chdir(path)
    
    file = fileName + "." + fileType
    path += file

    if (os.path.exists(path)):
        os.remove(path)

    p = Path(file)
    p.write_text(txt)
    p.read_text()
    

    

   


    label.pack(pady=30)


#Creates a Frame
frame = LabelFrame(win, width= 400, height= 180, bd=5)
frame.pack()
#Stop the frame from propagating the widget to be shrink or fit
frame.pack_propagate(False)

#Create an Entry widget in the Frame
entryFolder = ttk.Entry(frame, width= 40)
entryFolder.insert(INSERT, "Enter Your Folder Name...")
entryFolder.pack()

# define the entry boxes
entryFile = ttk.Entry(frame, width= 40)
entryFile.insert(INSERT, "Enter Your File Name...")
entryFile.pack()

entryTxt = ttk.Entry(frame, width= 40)
entryTxt.insert(INSERT, "Enter Your Text...")
entryTxt.pack()

entryFileType = ttk.Entry(frame, width= 40)
entryFileType.insert(INSERT, "Enter Your FileType...")
entryFileType.pack()

entryDir = ttk.Entry(frame, width= 40)
entryDir.insert(INSERT, "Enter Your Directory...")
entryDir.pack()

#Create a Button
ttk.Button(win, text= "Click", command= myclick).pack(pady=20)
win.mainloop()

