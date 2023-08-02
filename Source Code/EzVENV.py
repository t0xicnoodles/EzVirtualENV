import os
from win32 import win32api

from tkinter import *
from tkinter import ttk
from tkinter import filedialog

###############################
app = Tk()
app.geometry("400x200")
app.configure(background='#2e2e2e')
app.title('Noodles EzVirtualENV')
app.resizable(False, False)
app.overrideredirect(0)
app.eval('tk::PlaceWindow . center')
###############################

folderIcon = PhotoImage(file="./images/folderIcon.png")
submit = Label()
viewFolderLocation = Button()


def viewPath():
    global pathScreen
    pathScreen = Tk()
    pathScreen.configure(background='#2e2e2e')
    pathScreen.attributes('-topmost', True)
    pathScreen.eval('tk::PlaceWindow . center')
    pathScreen.title('Noodles EzVirtualENV')
    pathScreen.resizable(False, False)
    pathText = Label(
        pathScreen, text=f"{folderLocation}", bg="#2e2e2e", fg="white")
    pathText.pack(expand=True, fill=BOTH)
###############################


def createVenv():
    myBat = open(rf'{folderLocation}/activate.bat', 'w+')
    batFolderLocation = folderLocation.replace("/", "\\")
    myBat.write(
        f'"{batFolderLocation}\\virtualEnv\Scripts\\activate.bat" & cmd /k')
    myBat.close()
    os.system(f'"cd {folderLocation} & python -m venv virtualEnv"')

    app.destroy()
    try:
        pathScreen.destroy()
    except:
        pass
    win32api.MessageBox(0, 'VENV Creation Successful!', 'Done!')
###############################


def selectFolder():
    global folderLocation, submit, viewFolderLocation
    folderLocation = filedialog.askdirectory()
    print(folderLocation)
    if (folderLocation != ""):
        SelectfolderLocationStatus.destroy()
        viewFolderLocation = Button(app, text="View Path", command=viewPath)
        viewFolderLocation.place(anchor=CENTER, relx=.6, rely=.498)
        submit = Button(
            app, text="Create Python Virtual Environment!", command=createVenv)
        submit.place(anchor=CENTER, relx=.5, rely=.8)
        info = Label(
            app, text="The application will freeze until VENV is created.", fg="red", bg="#2e2e2e")
        info.place(anchor=CENTER, relx=.5, rely=.93)
    else:
        return


###############################
EzVenvTitle = Label(app, text="Noodle's EzVENV", bg="#2e2e2e",
                    fg="white", font=('Helvatical bold', 18))
EzVenvTitle.place(anchor=CENTER, relx=.5, rely=.1)
SelectfolderLocation = Button(
    app, command=selectFolder, bg="#2e2e2e",  activebackground="#2e2e2e",  borderwidth=0, image=folderIcon, height=64, width=64)
SelectfolderLocation.place(anchor=CENTER, relx=.2, rely=.5)
SelectfolderLocationStatus = Label(
    app, text="Please select a folder location.", fg="red", font=('Helvatical bold', 12))
SelectfolderLocationStatus.place(anchor=CENTER, relx=.6, rely=.498)
app.mainloop()
###############################

# Program Created By Noodle's

###############################
