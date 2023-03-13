from cx_Freeze import setup, Executable
import sys, tkinter.filedialog, tkinter

ico="Lineage 2.ico"

root = tkinter.Tk()
def setuper(base, name, version, descript, icon, author):
    filecompile = tkinter.filedialog.askopenfilename(title="Файл которий в exe")
    if filecompile[len(filecompile)-3:] == ".py":
        root.destroy()
        setup(
            name=name,
            version=version,
            description=descript,
            executables=[Executable(filecompile, base=base, icon=icon, copyright=author)]
        )
    else:
        print("ERROR, chose compile file *.py")
        
tkinter.Label(root, text="Text product name").pack()
name = tkinter.Entry(root)
name.pack()
tkinter.Label(root, text="Version, 1.1").pack()
version = tkinter.Entry(root)
version.pack()
tkinter.Label(root, text="Description:").pack()
description = tkinter.Entry(root, width=40)
description.pack()
tkinter.Label(root, text="Copyrights").pack()
copyrights = tkinter.Entry(root)
copyrights.pack()
icon = tkinter.Label(root, text='chose icon format .ico')
icon.pack()
def choice():
    global ico
    ico = tkinter.filedialog.askopenfilename(title="ICO file")
    if ico[len(ico)-4:] == ".ico":
        icon["text"]=ico
    else:
        icon["text"]="ERROR format not .ico"
    
tkinter.Button(root, text="choice", command=choice).pack()


def config():
    x32_x64 = sys.platform

    if x32_x64 == 'win32':
        base = "Win32GUI"
        setuper(base=base, name=name.get(), version=version.get(), descript=description.get(), icon=ico, author=copyrights.get())
    elif x32_x64 == "win64":
        base = "Win64GUI"
        setuper(base=base, name=name.get(), version=version.get(), descript=description.get(), icon=ico, author=copyrights.get())
    else:
        print("Error, this compile only x32 or x64 Windows")

tkinter.Button(root, text="Compile", command=config).pack(side="bottom")
root.mainloop()
