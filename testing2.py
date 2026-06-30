import tkinter, os, sys
from PIL import ImageTk, Image
def resourcePath(relPath):
    try: base = sys._MEIPASS
    except Exception: base = os.path.abspath(".")
    return os.path.join(base, relPath)
root = tkinter.Tk()
root.configure(background="black")
BG = "Black"
FG="White"
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
img = Image.open(fp=resourcePath("yg.png")).resize([1200, 650])
root.ref = realimg = ImageTk.PhotoImage(image=img)
wallpaper = tkinter.Label(root, image=realimg)
wallpaper.ref = realimg
wallpaper.grid(row=0, column=0)
holderFrame = tkinter.Frame(root)
holderFrame.grid(row=0, column=0)
tkinter.Label(root, background=BG, foreground=FG, text="Enter your username or email:").place(x=465, y=240)
tkinter.Label(root, background=BG, foreground=FG, text="Enter your password:").place(x=465, y=290)
username = tkinter.Entry(root, background=BG, foreground=FG, width=25, font=("Arial Rounded MT Bold", 15))
username.place(x=465, y=265)
password = tkinter.Entry(root, background=BG, foreground=FG, width=25, show="*", font=("Arial Rounded MT Bold", 15))
password.place(x=465, y=315)
loginBtn = tkinter.Button(root, background=FG, foreground=BG, width=25, height=2, text="Login", anchor=tkinter.CENTER, font=("Arial Rounded MT Bold", 15))
loginBtn.place(x=465, y=365)
root.mainloop()