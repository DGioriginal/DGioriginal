import tkinter
from tkinter.filedialog import *
from tkinter import messagebox
from tkinter.filedialog import *
from time import sleep
from random import randint
from tkinter import scrolledtext  
    
dostart = Tk()
dostart.title("Overlow")
dostart.minsize(width= 200, height=250)
messagebox.showinfo( "Overlow",'Hello, you  on fille-low or over-low. You muss file cklick and this program check fille')
selected = IntVar() 
def save():
    sa = asksaveasfilename()
def problem():
    window = Tk()  
    window.title("Overlow")  
    window.geometry('600x700')  
    txt = scrolledtext.ScrolledText(window, width=40, height=10)  
    txt.grid(column=0, row=0)
    btn5 = Button(window, text="Save and rite me on mail.", command=save)
    btn5.grid(column=0, row=20) 
    window.mainloop()

def clickedch():  
    op = askopenfilename()
    if askopenfilename() == ' ':
        messagebox.showinfo("DANGER:               ", "problem")
    sleep(3)
    danger = randint(0, 100)
    messagebox.showinfo("DANGER:               ", danger)
    messagebox.showwarning("OVERLOW","PROFESSIONAL PROGRAM-OVERLOW")
def clickedfile():  
    op = askopenfilename()
    sleep(3)
    danger = randint(0, 100)
    messagebox.showinfo("DANGER:               ", danger)
    messagebox.showwarning("OVERLOW","PROFESSIONAL PROGRAM-OVERLOW")
def clickedinf():  
    messagebox.showinfo("INFORMATION", "THIS PROGRAMM MAKE COMPANNI: DGI.org-Danil_Gering_international.original. MAIL:smplencl@gmail.com")
    messagebox.showwarning("OVERLOW","PROFESSIONAL PROGRAM-OVERLOW")
btn1 = Button(dostart, text="site chrom", command=clickedch)
btn2 = Button(dostart, text="file", command=clickedfile)
btn3 = Button(dostart, text="information", command=clickedinf)
btn4 = Button(dostart, text="rite problem", command=problem)
btn1.grid(column=0, row=50)
btn2.grid(column=0, row=60)
btn3.grid(column=0, row=70)
btn4.grid(column=0, row=80) 

