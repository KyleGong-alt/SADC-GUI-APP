import tkinter as tk
from tkinter import filedialog, Text #helps pick files, prints text
import os #allows us to run apps

root = tk.Tk() #holds everything
apps = []

bool_erase = 0

if os.path.isfile('save.txt'): #checks if save file already exists
    with open('save.txt','r') as f:
        tempApps = f.read() #reads into savefile
        tempApps = tempApps.split(',') #split applications when there's a comma
        apps = [x for x in tempApps if x.strip()] #Erases extra whitespace and nonexisting apps
        
def AddApps():
    for files in frame.winfo_children():
        files.destroy() #refreshes added files

    filename = filedialog.askopenfilename(initialdir="/", title="Select a File",
                                          filetypes=(("Executables","*.exe"), ("all files","*.*")))
    apps.append(filename) #adds file into apps
    for app in apps:
        label = tk.Label(frame,text= app, bg="gray")
        label.pack()

def RunApps():
    for app in apps:
        os.startfile(app)

def EraseSave():
    global bool_erase
    for files in frame.winfo_children():
        files.destroy() #refreshes added files
    if os.path.exists("save.txt"): #check if save file exists
        os.remove("save.txt") #remove the save file
    bool_erase = 1 #boolean so we never save the files
    



#BACKGROUND CODING
canvas = tk.Canvas(root,height=600, width=600, bg="#FFC0CB")
canvas.pack() #Runs the background

#Creates a frame ontop of the background
frame = tk.Frame(root,bg="white")
frame.place(relwidth = 0.8, relheight=0.6, relx=0.1, rely=0.1)

OpenFiles=tk.Button(root, text ="Open File",padx=10,pady=5,
                    fg="white",bg="#000000", command=AddApps)
OpenFiles.pack()

RunApps = tk.Button(root, text ="Run Apps",padx=10,pady=5,
                    fg="white",bg="#000000", command=RunApps)
RunApps.pack()

EraseSave = tk.Button(root, text ="Erase files",padx=10,pady=5,
                    fg="white",bg="#000000", command=EraseSave)
EraseSave.pack()

for app in apps: #uses the pre-existing save.txt
    label = tk.Label(frame, text=app)
    label.pack()

root.mainloop() #starts everything

if bool_erase == 0: #check if erase files is used
    with open('save.txt', 'w') as f: #Save text files
        for app in apps:
            f.write(app +',')



    









