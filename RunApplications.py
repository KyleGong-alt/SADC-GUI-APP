import tkinter as tk
from tkinter import filedialog, Text #helps pick files, prints text
import os #allows us to run apps

root = tk.Tk() #holds everything
apps = []

def AddApps():
    for files in frame.winfo_children():
        files.destroy() #freshes added files

    filename = filedialog.askopenfilename(initialdir="/", title="Select a File",
                                          filetypes=(("Executables","*.exe"), ("all files","*.*")))
    apps.append(filename) #adds file into apps
    for app in apps:
        label = tk.Label(frame,text= app, bg="gray")
        label.pack()

def RunApps():
    for app in apps:
        os.startfile(app)


#BACKGROUND CODING
canvas = tk.Canvas(root,height=700, width=700, bg="#FFC0CB")
canvas.pack() #Runs the background

#Creates a frame ontop of the background
frame = tk.Frame(root,bg="white")
frame.place(relwidth = 0.8, relheight=0.7, relx=0.1, rely=0.1)

OpenFiles=tk.Button(root, text ="Open File",padx=10,pady=5,
                    fg="white",bg="#000000", command=AddApps)
OpenFiles.pack()

RunApps = tk.Button(root, text ="Run Apps",padx=10,pady=5,
                    fg="white",bg="#000000", command=RunApps)
RunApps.pack()


root.mainloop() #starts everything








