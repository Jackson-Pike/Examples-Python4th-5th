# Format Input Jupyter Notebook | Jackson Pike | Sept 2018


#Get String To Input
from tkinter import *
from tkinter import ttk
from tkinter import font

root = Tk()
root.configure(background="CadetBlue")
root.bind("<Escape>", quit)
fnt = font.Font(family="Helvetica", size=60, weight="bold")
txt = StringVar()
lbl = ttk.Label(root, textvariable=txt, font=fnt, foreground="DarkSlateGray", background="DarkGoldenrod")
lbl.place(relx=0.5, rely=0.5, anchor=CENTER)
root.mainloop()
