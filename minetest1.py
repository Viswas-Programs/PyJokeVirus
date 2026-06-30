import customtkinter, sys, os
from PIL import Image, ImageTk

def resourcePath(relPath):
    try: base = sys._MEIPASS
    except Exception: base = os.path.abspath(".")
    return os.path.join(base, relPath)
root = customtkinter.CTk()
baseimg = Image.open(fp=resourcePath("bg.png")).resize(size=(int(root.winfo_screenwidth()//1.5), int(root.winfo_screenheight()//1.5)))
root.geometry(f"{baseimg.width}x{baseimg.height}")
image = customtkinter.CTkImage(baseimg, size=(baseimg.width, baseimg.height))
tkimg = ImageTk.PhotoImage(baseimg)
bgimg = customtkinter.CTkLabel(root, image=image, text="",  width=baseimg.width, height=baseimg.height)
bgimg.REF = image
bgimg.BASE_REF = baseimg
bgimg.place(x=0, y=0)
#mainFrame=  customtkinter.CTkFrame(root, fg_color="transparent", bg_color="transparent")
#mainFrame.grid(row=0, column=0)
canvas= customtkinter.CTkCanvas(root, width=baseimg.width, height=baseimg.height, highlightthickness=0)
canvas.grid(row=0, column=0)
canvas.REF = tkimg
canvas.BASE_REF = baseimg
canvas.create_image(0,0,image=tkimg,anchor="nw")

canvas.create_text(400, 50, text="Welcome to Magma Client", fill="white")
#customtkinter.CTkLabel(root, text="Welcome to Magma Client", text_color="white").grid(row=0, column=0)
#customtkinter.CTkLabel(root, text="Get the best performing Launcher right now, from one install away!").grid(row=1, column=0, pady=5)
#customtkinter.CTkLabel(root, text="This installer will provide you the launcher and the best performance enhancing mods right to you!").grid(row=2, column=0, pady=2)

root.mainloop()