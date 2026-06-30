import tkinter, sys, os
from PIL import Image, ImageTk
from tkinter.ttk import Progressbar

def resourcePath(relPath):
    try: base = sys._MEIPASS
    except Exception: base = os.path.abspath(".")
    return os.path.join(base, relPath)
class UI:
    def __init__(self):
        self.txtClr = "white"
        self.font = "Segoe UI"
        self.root = tkinter.Tk()
        self.root.title("Magma Client")
        self.baseimg = Image.open(fp=resourcePath("bg.png")).resize(size=(int(self.root.winfo_screenwidth()//1.5), int(self.root.winfo_screenheight()//1.5)))
        self.root.geometry(f"{self.baseimg.width}x{self.baseimg.height}")
        tkimg = ImageTk.PhotoImage(self.baseimg)
        self.canvas= tkinter.Canvas(self.root, width=self.baseimg.width, height=self.baseimg.height, highlightthickness=0)
        self.canvas.grid(row=0, column=0)
        self.canvas.REF = tkimg
        self.canvas.BASE_REF = self.baseimg
        self.canvas.create_image(0,0,image=tkimg,anchor="nw")

        self.canvas.create_text(170, 25, text="MAGMA Client Install Wizard", fill=self.txtClr, font=(self.font, 18))
        #pg1 = []
        #welcP1 = self.canvas.create_text(550, 75, text="Welcome to the Magma Client Install Wizard!", fill=self.txtClr, font=(self.font, 15))
        
        # sidebar brah
        self.sidebar_t1 = self.canvas.create_text(100, 125, text=" - Introduction...", fill=self.txtClr, font=(self.font, 14))
        #self.sidebar_t1 = self.canvas.create_text(126, 125, text=" - Introduction...DONE", fill=self.txtClr, font=(self.font, 14))
        self.sidebar_t2 = self.canvas.create_text(165, 160, text=" - Salient Features and Details...", fill=self.txtClr, font=(self.font, 14))
        self.sidebar_t3 = self.canvas.create_text(70, 195, text=" - EULA...", fill=self.txtClr, font=(self.font, 14))
        self.sidebar_t4 = self.canvas.create_text(87, 230, text=" - Installing...", fill=self.txtClr, font=(self.font, 14))
        self.sidebar_t5 = self.canvas.create_text(101, 265, text=" - Finishing Up...", fill=self.txtClr, font=(self.font, 14))
        self.showPg1()
        self.root.mainloop()
    def updateDone(self, num):
        MAP = {1: self.sidebar_t1, 2: self.sidebar_t2, 3: self.sidebar_t3, 4: self.sidebar_t4, 5: self.sidebar_t5}
        try:
            curText = str(self.canvas.itemcget(MAP[num], "text"))
            if curText.endswith("DONE"): return
            self.canvas.itemconfig(MAP[num], text=self.canvas.itemcget(MAP[num], "text")+"DONE")
            self.canvas.move(MAP[num], 26, 0)
        except Exception as EXP: print(EXP)
    def showPg1(self):
        self._deleteCurrentPg()
        pg1 = []
        welcP1 = self.canvas.create_text(550, 75, text="Welcome to the Magma Client Install Wizard!", fill=self.txtClr, font=(self.font, 15))
        descP1 = self.canvas.create_text(578, 195, text="This Install Wizard will guide you through the setup\nprocess of installing the Magma client in your system.\n\nTo begin with the installation, Click Next.", font=(self.font, 14), fill=self.txtClr)
        nextBtn = self.canvas.create_window(850, 420, window=tkinter.Button(self.canvas, text="Next", background="#d93c0d", foreground=self.txtClr, padx=20, command=self.showPg2))
        pg1.extend([welcP1, descP1, nextBtn])
        self.currentPg = pg1
    def showPg2(self):
        self.updateDone(1)
        self._deleteCurrentPg()
        text1 = """The Magma Client is one of the best clients for playing Minecraft\nIt comes preinstalled with lots of optimization mods and shaders.\nExclusively comes with X-Ray and other cheats!"""
        desc1=  self.canvas.create_text(628, 140, text=text1, fill=self.txtClr, font=(self.font, 14))
        text2= """It doesn't stop with just cheats and FPS improvements,\nbut it also drastically improves your playing experience,\nby improving the key UI elements and features such as the\n-HUD\n-F3 Menu\n-Mod Menu\n-Minimap\n-And many more!..."""
        desc2 = self.canvas.create_text(595, 285, text=text2, fill=self.txtClr, font=(self.font, 14))
        nextBtn = self.canvas.create_window(850, 420, window=tkinter.Button(self.canvas, text="Next", background="#d93c0d", foreground=self.txtClr, padx=20, command=self.showPg3))
        backBtn = self.canvas.create_window(398, 420, window=tkinter.Button(self.canvas, text="<< Back", background="#d93c0d", foreground=self.txtClr, padx=20, command=self.showPg1))
        self.currentPg = [desc1, nextBtn, backBtn, desc2]
    def showPg3(self):
        self.updateDone(2)
        self._deleteCurrentPg()
        content = None
        with open(resourcePath("eula.txt")) as reader: content= reader.read()
        textWdw = tkinter.Text(self.canvas, background=self.txtClr, foreground="black", width=50, height=12)
        textWdw.insert(tkinter.END, content )
        textWdw.configure(state="disabled")
        wdw = self.canvas.create_window(600, 250, window=textWdw,)
        acceptBtn = self.canvas.create_window(850, 420, window=tkinter.Button(self.canvas, text="Accept", background="#d93c0d", foreground=self.txtClr, padx=20, command=self.showPg4))
        backBtn = self.canvas.create_window(398, 420, window=tkinter.Button(self.canvas, text="<< Back", background="#d93c0d", foreground=self.txtClr, padx=20, command=self.showPg2))
        aboveTxt = self.canvas.create_text(530, 110, text="Read the below provided EULA and accept!\nIf you want to decline, quit the program!", fill=self.txtClr, font=(self.font, 14))
        self.currentPg = [wdw, acceptBtn, backBtn, aboveTxt]
    def showPg4(self):
        self._deleteCurrentPg()
        self.updateDone(3)
        instText = self.canvas.create_text(440, 175, text="Installing the client...", fill=self.txtClr, font=(self.font, 14))
        pgbar =  Progressbar(self.canvas, mode="indeterminate", orient="horizontal", length=400)
        pgbar.start()
        pgbarDp = self.canvas.create_window(552, 200, window=pgbar)
    def _deleteCurrentPg(self):
        try:
            for id in self.currentPg: self.canvas.delete(id)
        except: pass
UI()