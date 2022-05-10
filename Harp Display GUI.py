#Program written by Connor Bluedorn
#Last modified 9 May 2022

from tkinter.font import BOLD
from turtle import back #May not be needed?
import tkinter as tk
from functools import partial
from tkinter import messagebox

printable = True    #Global var to prevent spam of on_press functionality.
pedalpositionlist = [0,0,0,0,0,0,0] #Global var to track position of pedals

#Creates display window
window = tk.Tk()
window.title("Pedal Display")
window.config(background="white")

#Displays for pedal positions. Top row is initialized to black as the starting position. Tpedal = top row, Mpedal = middle row, Bpedal = bottom row
tpedal0 = tk.Label(text="PEDAL",background="black",foreground="black",font=("Arial",25))
tpedal0.grid(column=1,row=0)
tpedal1 = tk.Label(text="PEDAL",background="black",foreground="black",font=("Arial",25))
tpedal1.grid(column=3,row=0)
tpedal2 = tk.Label(text="PEDAL",background="black",foreground="black",font=("Arial",25))
tpedal2.grid(column=5,row=0)
tpedal3 = tk.Label(text="PEDAL",background="black",foreground="black",font=("Arial",25))
tpedal3.grid(column=8,row=0)
tpedal4 = tk.Label(text="PEDAL",background="black",foreground="black",font=("Arial",25))
tpedal4.grid(column=10,row=0)
tpedal5 = tk.Label(text="PEDAL",background="black",foreground="black",font=("Arial",25))
tpedal5.grid(column=12,row=0)
tpedal6 = tk.Label(text="PEDAL",background="black",foreground="black",font=("Arial",25))
tpedal6.grid(column=14,row=0)

mpedal0 = tk.Label(text="PEDAL",background="white",foreground="white",font=("Arial",20))
mpedal0.grid(column=1,row=2)
mpedal1 = tk.Label(text="PEDAL",background="white",foreground="white",font=("Arial",20))
mpedal1.grid(column=3,row=2)
mpedal2 = tk.Label(text="PEDAL",background="white",foreground="white",font=("Arial",20))
mpedal2.grid(column=5,row=2)
mpedal3 = tk.Label(text="PEDAL",background="white",foreground="white",font=("Arial",20))
mpedal3.grid(column=8,row=2)
mpedal4 = tk.Label(text="PEDAL",background="white",foreground="white",font=("Arial",20))
mpedal4.grid(column=10,row=2)
mpedal5 = tk.Label(text="PEDAL",background="white",foreground="white",font=("Arial",20))
mpedal5.grid(column=12,row=2)
mpedal6 = tk.Label(text="PEDAL",background="white",foreground="white",font=("Arial",20))
mpedal6.grid(column=14,row=2)

bpedal0 = tk.Label(text="PEDAL",background="white",foreground="white",font=("Arial",20))
bpedal0.grid(column=1,row=4)
bpedal1 = tk.Label(text="PEDAL",background="white",foreground="white",font=("Arial",20))
bpedal1.grid(column=3,row=4)
bpedal2 = tk.Label(text="PEDAL",background="white",foreground="white",font=("Arial",20))
bpedal2.grid(column=5,row=4)
bpedal3 = tk.Label(text="PEDAL",background="white",foreground="white",font=("Arial",20))
bpedal3.grid(column=8,row=4)
bpedal4 = tk.Label(text="PEDAL",background="white",foreground="white",font=("Arial",20))
bpedal4.grid(column=10,row=4)
bpedal5 = tk.Label(text="PEDAL",background="white",foreground="white",font=("Arial",20))
bpedal5.grid(column=12,row=4)
bpedal6 = tk.Label(text="PEDAL",background="white",foreground="white",font=("Arial",20))
bpedal6.grid(column=14,row=4)



def update_pedal(pedalnum,pedalval): #Configures relevant pedal row to update position.
    if(pedalval == 0):  #Value of the pedal position determines which row is black, with the others being set to white.
        tcolor = "black"
        mcolor = "white"
        bcolor = "white"
    if(pedalval == 1):
        tcolor = "white"
        mcolor = "black"
        bcolor = "white"
    if(pedalval == 2):
        tcolor = "white"
        mcolor = "white"
        bcolor = "black"

    if(pedalnum == 0):                          #Configure relevant pedal.
        tpedal0.configure(bg=tcolor, fg=tcolor)
        mpedal0.configure(bg=mcolor, fg=mcolor)
        bpedal0.configure(bg=bcolor, fg=bcolor)
    if(pedalnum == 1):
        tpedal1.configure(bg=tcolor, fg=tcolor)
        mpedal1.configure(bg=mcolor, fg=mcolor)
        bpedal1.configure(bg=bcolor, fg=bcolor)
    if(pedalnum == 2):
        tpedal2.configure(bg=tcolor, fg=tcolor)
        mpedal2.configure(bg=mcolor, fg=mcolor)
        bpedal2.configure(bg=bcolor, fg=bcolor)
    if(pedalnum == 3):
        tpedal3.configure(bg=tcolor, fg=tcolor)
        mpedal3.configure(bg=mcolor, fg=mcolor)
        bpedal3.configure(bg=bcolor, fg=bcolor)
    if(pedalnum == 4):
        tpedal4.configure(bg=tcolor, fg=tcolor)
        mpedal4.configure(bg=mcolor, fg=mcolor)
        bpedal4.configure(bg=bcolor, fg=bcolor)
    if(pedalnum == 5):
        tpedal5.configure(bg=tcolor, fg=tcolor)
        mpedal5.configure(bg=mcolor, fg=mcolor)
        bpedal5.configure(bg=bcolor, fg=bcolor)
    if(pedalnum == 6):
        tpedal6.configure(bg=tcolor, fg=tcolor)
        mpedal6.configure(bg=mcolor, fg=mcolor)
        bpedal6.configure(bg=bcolor, fg=bcolor)

def decrementpedal(pedalnum):   
    global pedalpositionlist                #Decrement relevant pedal (Increasing count decreases position as rows/columns grow downward/rightward in GUI)
    if(pedalpositionlist[pedalnum])<=1:     #If at bottom position, saturate and do not continue decrementing
        pedalpositionlist[pedalnum] += 1
    update_pedal(pedalnum,pedalpositionlist[pedalnum]) #Call update_pedal to reflect change in GUI

def incrementpedal(pedalnum):
    global pedalpositionlist
    if(pedalpositionlist[pedalnum])>=1:     #Increment relevant pedal (Decreasing count increases position as rows/columns grow downward/rightward in GUI)
        pedalpositionlist[pedalnum] -= 1    #If at top position, saturate and do not change.
    update_pedal(pedalnum,pedalpositionlist[pedalnum]) #Call update_pedal to reflect change in GUI

def buttonpressed(event):   #When a binded key is pressed, evaluate and call relevant increment/decrement.
    if(event.char == 'w'):
        incrementpedal(0)
    if(event.char == 'e'):
        incrementpedal(1)
    if(event.char == 'r'):
        incrementpedal(2)
    if(event.char == 'y'):
        incrementpedal(3)
    if(event.char == 'u'):
        incrementpedal(4)
    if(event.char == 'i'):
        incrementpedal(5)
    if(event.char == 'o'):
        incrementpedal(6)

    if(event.char == 's'):
        decrementpedal(0)
    if(event.char == 'd'):
        decrementpedal(1)
    if(event.char == 'f'):
        decrementpedal(2)
    if(event.char == 'h'):
        decrementpedal(3)
    if(event.char == 'j'):
        decrementpedal(4)
    if(event.char == 'k'):
        decrementpedal(5)
    if(event.char == 'l'):
        decrementpedal(6)

#Up and Down Buttons for changing position through clicking, also provide info on which keys are bound to what functionality
up0 = tk.Button(window, text=" Up  [W]",command=partial(incrementpedal,0),font=("Arial",15))
up0.grid(column=1,row=1)
up1 = tk.Button(window, text=" Up  [E]",command=partial(incrementpedal,1),font=("Arial",15))
up1.grid(column=3,row=1)
up2 = tk.Button(window, text=" Up  [R]",command=partial(incrementpedal,2),font=("Arial",15))
up2.grid(column=5,row=1)
up3 = tk.Button(window, text=" Up  [Y]",command=partial(incrementpedal,3),font=("Arial",15))
up3.grid(column=8,row=1)
up4 = tk.Button(window, text=" Up  [U]",command=partial(incrementpedal,4),font=("Arial",15))
up4.grid(column=10,row=1)
up5 = tk.Button(window, text=" Up  [I]",command=partial(incrementpedal,5),font=("Arial",15))
up5.grid(column=12,row=1)
up6 = tk.Button(window, text=" Up  [O]",command=partial(incrementpedal,6),font=("Arial",15))
up6.grid(column=14,row=1)

down0 = tk.Button(window,text="Down [S]",command=partial(decrementpedal,0),font=("Arial",15))
down0.grid(column=1,row=3)
down1 = tk.Button(window,text="Down [D]",command=partial(decrementpedal,1),font=("Arial",15))
down1.grid(column=3,row=3)
down2 = tk.Button(window,text="Down [F]",command=partial(decrementpedal,2),font=("Arial",15))
down2.grid(column=5,row=3)
down3 = tk.Button(window,text="Down [H]",command=partial(decrementpedal,3),font=("Arial",15))
down3.grid(column=8,row=3)
down4 = tk.Button(window,text="Down [J]",command=partial(decrementpedal,4),font=("Arial",15))
down4.grid(column=10,row=3)
down5 = tk.Button(window,text="Down [K]",command=partial(decrementpedal,5),font=("Arial",15))
down5.grid(column=12,row=3)
down6 = tk.Button(window,text="Down [L]",command=partial(decrementpedal,6),font=("Arial",15))
down6.grid(column=14,row=3)

#Spacers to position pedals
spacer0 = tk.Label(text="PEDAL",background="white",foreground="white",font=("Arial",10))
spacer0.grid(column=2,row=0)
spacer1 = tk.Label(text="PEDAL",background="white",foreground="white",font=("Arial",10))
spacer1.grid(column=4,row=0)
spacer2 = tk.Label(text="PEDAL",background="white",foreground="white",font=("Arial",10))
spacer2.grid(column=6,row=0)
spacer3 = tk.Label(text="PEDAL",background="white",foreground="white",font=("Arial",10))
spacer3.grid(column=7,row=0)
spacer4 = tk.Label(text="PEDAL",background="white",foreground="white",font=("Arial",10))
spacer4.grid(column=9,row=0)
spacer5 = tk.Label(text="PEDAL",background="white",foreground="white",font=("Arial",10))
spacer5.grid(column=11,row=0)
spacer6 = tk.Label(text="PEDAL",background="white",foreground="white",font=("Arial",10))
spacer6.grid(column=13,row=0)

#Pedal Labels
dlabel = tk.Label(text="D",background="white",foreground="black",font=("Arial",20,'bold'))
dlabel.grid(column=1,row=6)
clabel = tk.Label(text="C",background="white",foreground="black",font=("Arial",20,'bold'))
clabel.grid(column=3,row=6)
blabel = tk.Label(text="B",background="white",foreground="black",font=("Arial",20,'bold'))
blabel.grid(column=5,row=6)
elabel = tk.Label(text="E",background="white",foreground="black",font=("Arial",20,'bold'))
elabel.grid(column=8,row=6)
flabel = tk.Label(text="F",background="white",foreground="black",font=("Arial",20,'bold'))
flabel.grid(column=10,row=6)
glabel = tk.Label(text="G",background="white",foreground="black",font=("Arial",20,'bold'))
glabel.grid(column=12,row=6)
alabel = tk.Label(text="A",background="white",foreground="black",font=("Arial",20,'bold'))
alabel.grid(column=14,row=6)
#Esc functionality info
escinfo = tk.Label(text="Press Esc to Close",background="white",foreground="black",font=("Arial",10))
escinfo.grid(column=1,row=7)

#Collection of bound keys to call buttonpressed
#Incrementing keys
window.bind('w',buttonpressed)
window.bind('e',buttonpressed)
window.bind('r',buttonpressed)
window.bind('y',buttonpressed)
window.bind('u',buttonpressed)
window.bind('i',buttonpressed)
window.bind('o',buttonpressed)
#Decrementing keys
window.bind('s',buttonpressed)
window.bind('d',buttonpressed)
window.bind('f',buttonpressed)
window.bind('h',buttonpressed)
window.bind('j',buttonpressed)
window.bind('k',buttonpressed)
window.bind('l',buttonpressed)

#Ask for confirmation before closing. 
def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        window.destroy()
#Ask for confirmation on Esc close, needs seperate handler as window.bind passes in event and clicking the close does not. 
def esc_closing(e):
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        window.destroy()

#Binds escape to allow closing.
window.bind('<Escape>', esc_closing)
#Bind window deletion to confirmation
window.protocol("WM_DELETE_WINDOW", on_closing)
#Main loop for GUI
window.mainloop()
