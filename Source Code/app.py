import os
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
###############################
app = Tk()
app.geometry("478x443")
app.configure(background='#2e2e2e')
app.title('Noodles EzVirtualENV')
app.resizable(False, False)
app.overrideredirect(0)
app.eval('tk::PlaceWindow . center')
###############################
def viewPath():
    global pathScreen
    pathScreen = Tk()
    pathScreen.configure(background='#2e2e2e')
    pathScreen.title('Noodles EzVirtualENV')
    pathScreen.resizable(False, False)
    pathText = Label(pathScreen, text=f"{folderLocation}", bg="#2e2e2e", fg="white")
    pathText.pack(expand=True, fill=BOTH)
###############################
def createVenv():
        myBat = open(rf'{folderLocation}/activate.bat','w+')
        batFolderLocation = folderLocation.replace("/", "\\")
        myBat.write(f'"{batFolderLocation}\\virtualEnv\Scripts\\activate.bat" & cmd /k')
        myBat.close()
        os.system(f'"cd {folderLocation} & python -m venv virtualEnv"')
        popup = Tk()
        popup.configure(background='#2e2e2e')
        popup.title('Noodles EzVirtualENV')
        popup.resizable(False, False)
        label = Label(popup, text="Done!", bg="#2e2e2e", fg="white")
        label.pack(side="top", fill="x", pady=10)
        B1 = ttk.Button(popup, text="Okay", command = popup.destroy)
        B1.pack()
        app.destroy()
        try:
             pathScreen.destroy()
        except:
             pass
###############################
def selectFolder():
    global folderLocation
    folderLocation = filedialog.askdirectory()
    print(folderLocation)
    if(folderLocation != ""):
        SelectfolderLocationStatus.destroy()
        viewFolderLocation = Button(app, text="View Path", command=viewPath)
        viewFolderLocation.place(anchor = CENTER, relx = .6, rely = .498)
        submit = Button(app, text="Create Python Virtual Environment!", command=createVenv)
        submit.place(anchor = CENTER, relx = .5, rely = .8)
        info = Label(app, text="App will freeze, then close when it's done.")
    else:
        return
###############################
EzVenvTitle = Label(app, text="Noodle's EzVENV", bg="#2e2e2e", fg="white", font=('Helvatical bold',18))
EzVenvTitle.place(anchor = CENTER, relx = .5, rely = .1)
SelectfolderLocation = Button(app, text="Select VENV Location", command=selectFolder)
SelectfolderLocation.place(anchor = CENTER, relx = .2, rely = .5)
SelectfolderLocationStatus = Label(app, text="Please select a folder location.", fg="red", font=('Helvatical bold',12))
SelectfolderLocationStatus.place(anchor = CENTER, relx = .6, rely = .498)
app.mainloop()
###############################

#Program Created By Noodle's 

###############################