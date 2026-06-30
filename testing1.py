import tkinter
import tkinterweb_tkhtml_extras
from tkinterweb import HtmlFrame
import os, sys
from PIL import Image, ImageTk

def resourcePath(relPath):
    try: base = sys._MEIPASS
    except Exception: base = os.path.abspath(".")
    return os.path.join(base, relPath)
root = tkinter.Tk()

def _testing(e=None, *args):
    print("Args: ", args, "and e=", e)
    print(frame.document.getElementById("username").value)
    print(frame.document.getElementById("pwd").value)

root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

img = Image.open(fp="image.png")
tkimg = ImageTk.PhotoImage(image=img)
lbl = tkinter.Label(root, background="Black", foreground="White", image=tkimg)
lbl.REF = tkimg
lbl.grid(row=0, column=0)


frame = HtmlFrame(root, messages_enabled=True, width=455, height=455)
frame.grid(row=0, column=0)
frame.load_file(resourcePath('main2.html'))
frame.document.getElementById("loginbtn").bind("<Button-1>", _testing )
root.mainloop()