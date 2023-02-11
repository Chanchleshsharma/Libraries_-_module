###########  GUI Graphical User interface###########   CUI----> Character user interface

## Types----->
# 1.Desktop based gui  application
# 2.Web based gui
# 3.Mobil based gui
# 
#  
#tkinter library
# Tkinter libraby provide facilities to create a desktop based gui application in python
#  
#
from tkinter import *
win=Tk()       # here create window of our destop application

win.geometry("400x300")
win.configure(bg="yellow")
# class Button:

b1=Button(win,text="Submit")
b2=Button(win,text="Ok")
b1.place(x=250,y=150)
b2.place(x=100,y=150)
win.mainloop()     # make window visible













# win.mainloop()
