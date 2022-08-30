from cx_Freeze import setup, Executable
import sys, tkinter.filedialog, tkinter

root = tkinter.Tk()
def setuper(base):
    filecompile = tkinter.filedialog.askopenfilename(title="Файл которий в exe")
    root.destroy()
    setup(
        name="UTybeLinkDownload",
        version="0.11.1",
        description="[Shakal] Glory to Ukraine, .ussian warship fuckyou",
        executables=[Executable(filecompile, base=base, icon="shak.ico", copyright="The Shakal")]
    )

x32_x64 = sys.platform

if x32_x64 == 'win32':
    base = "Win32GUI"
    setuper(base=base)
elif x32_x64 == "win64":
    base = "Win64GUI"
    setuper(base=base)
else:
    print("Error, this compile only x32 or x64 Windows")

root.mainloop()
