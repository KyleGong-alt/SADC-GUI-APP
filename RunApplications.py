import tkinter as tk 
from tkinter import filedialog, Text #filedialog lets us run the applications, Text is needed for printing text in UI
import os #allows us to run apps

root = tk.Tk() #holds everything
apps = [] #initalize array for apps

bool_erase = 0 #initalize bool for erasing files


if os.path.isfile('save.txt'): #checks if save file already exists
    with open('save.txt','r') as f: #open save file
        tempApps = f.read() #reads into savefile
        tempApps = tempApps.split(',') #split applications when there's a comma
        # print (tempApps)
        apps = [x for x in tempApps if x.strip()] #Erases extra whitespace and nonexisting apps
        # print ("\n", apps)
def Addfunction(): 
    for files in frame.winfo_children(): 
        files.destroy() #refreshes added files
    filename = filedialog.askopenfilename(initialdir="/", title="Select a File", #title on the top
                                          filetypes=(("Executables","*.exe"), ("all files","*.*"))) #Can only run executables or all files, 
                                          
    apps.append(filename) #adds file into apps array
    for app in apps:
        label = tk.Label(frame,text= app, bg="gray") #prints out the text
        label.pack()

def Runfunction():
    for app in apps:
        os.startfile(app) #Starts applications

def Erasefunction():
    global bool_erase #make a global variable
    for files in frame.winfo_children():
        files.destroy() #refreshes added files
    if os.path.exists("save.txt"): #check if save file exists
        os.remove("save.txt") #remove the save file
    bool_erase = 1 #boolean so we never save the files
    
#Creates the background
canvas = tk.Canvas(root,height=600, width=600, bg="#FFC0CB")
canvas.pack() #Runs the background

#Creates a frame ontop of the background
frame = tk.Frame(root,bg="white")
frame.place(relwidth = 0.8, relheight=0.6, relx=0.1, rely=0.1)

OpenFiles=tk.Button(root, text ="Open File",padx=10,pady=5, #UI for the buttons
                    fg="white",bg="#000000", command=Addfunction)
OpenFiles.pack()

RunApps = tk.Button(root, text ="Run Apps",padx=10,pady=5,
                    fg="white",bg="#000000", command=Runfunction)
RunApps.pack()

EraseSave = tk.Button(root, text ="Erase files",padx=10,pady=5,
                    fg="white",bg="#000000", command=Erasefunction)
EraseSave.pack()

for app in apps: #uses the pre-existing save.txt
    label = tk.Label(frame, text=app)
    label.pack()

root.mainloop() #Runs everything

if bool_erase == 0: #check if erase files is used
    with open('save.txt', 'w') as f: #Open save.txt
        for app in apps:
            f.write(app +',') #Write into save.txt
