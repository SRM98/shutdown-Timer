import tkinter
import os
from tkinter import ttk, font

############################## WINDOW ###################################

top = tkinter.Tk()
top.configure(background="#252525")
top.title("Timer Shutdown")
top.geometry("300x380")

############################### TABS ####################################

# tabParent = ttk.Notebook(top)

# shutDownTab = ttk.Frame(tabParent)

# tabParent.add(shutDownTab, text = "Shutdown")

############################### Buttons #################################

def timerShutdown(time):
    time = int(time * 3600)
    value = {"timeShutDown": time}

    os.system("shutdown /s /t {timeShutDown}".format(**value))

def timerRestart(time):
    time = int(time * 3600)
    value = {"timeShutDown": time}
    os.system("shutdown /r /t {timeShutDown}".format(**value))

def stopTimer():
    os.system("shutdown /a")

myFont = font.Font(family = "Helvetica", size = 16, weight = "bold")

Button30minShut = tkinter.Button(top, text = "30 min", command = lambda: timerShutdown(0.5), width = 20, height = 1, font = myFont, bg = "#4bb015", bd = 3)
Button1hShut = tkinter.Button(top, text = "1h", command = lambda: timerShutdown(1), width = 20, height = 1, font = myFont, bg = "#4bb015", bd = 3)
Button1h30Shut = tkinter.Button(top, text = "1h 30", command = lambda: timerShutdown(1.5), width = 20, height = 1, font = myFont, bg = "#4bb015", bd = 3)
Button2hShut = tkinter.Button(top, text = "2h", command = lambda: timerShutdown(2), width = 20, height = 1, font = myFont, bg = "#4bb015", bd = 3)
Button2h30Shut = tkinter.Button(top, text = "2h 30", command = lambda: timerShutdown(2.5), width = 20, height = 1, font = myFont, bg = "#4bb015", bd = 3)
Button3hShut = tkinter.Button(top, text = "3h", command = lambda: timerShutdown(3), width = 20, height = 1, font = myFont, bg = "#4bb015", bd = 3)



ButtonStopTimer = tkinter.Button(top, text = "STOP Timer", command = stopTimer, width = 10, height = 1, font = myFont, bg = "#e21d10", bd = 3)


############################### Show ####################################
# tabParent.pack(expand = 1, fill = "both")

Button30minShut.pack(pady = (15,4))
Button1hShut.pack(pady = 4)
Button1h30Shut.pack(pady = 4)
Button2hShut.pack(pady = 4)
Button2h30Shut.pack(pady = 4)
Button3hShut.pack(pady = 4)

ButtonStopTimer.pack(pady = 4)

top.mainloop()