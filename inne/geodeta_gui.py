import tkinter
import tkinter.messagebox
from tkinter import *

import init

# create the main window
root = tkinter.Tk()
root.title('Geodeta 1.0')
root.geometry('300x900')  # size of the window
root['bg'] = 'HotPink1'

# button 1, generowanie raportu
def func1():
    import DPR_gui
    openFile()
    tkinter.messagebox.showinfo("Wykonano raport DPR", "Raport DPR gotowy")


def openFile():
    f = open('zwrot.txt', 'r', encoding='utf-8')
    data = f.read()
    txtarea.insert(END, data)
    f.close()


btn1 = Button(root, text="DPR", width=39, height=2, bg="DeepPink2",
              activebackground='Orchid3', command=func1)
btn1.place(x=10, y=10)


txtarea = Text(root, width=35, height=40)
# txtarea.place(x=10, y=90)
txtarea['bg'] = "maroon1"
txtarea.pack(pady=60)



# running the loop that works as a trigger
root.mainloop()
