#from PIL import Image
from Tkinter import *


def mousePressed(event):pass
	#redrawAll()

def keyPressed(event): pass
	#redrawAll()

def init():
	splashScreen()

def splashScreen():
	canvasWidth = canvas.data.canvasWidth
	canvasHeight = canvas.data.canvasHeight
	canvas.create_rectangle(0, 0, canvasWidth, canvasHeight, fill = "black")
	canvas.create_text(canvasWidth/2, canvasHeight/2, fill = "purple",
	text = "EVENTIFIER", font = "Helvetica 80 bold")

def timerFired():
	redrawAll()
	#delay = 250
	#canvas.after(delay, timerFired)

def redrawAll():
	canvasWidth = canvas.data.canvasWidth
	canvasHeight = canvas.data.canvasHeight
	canvas.create_rectangle(0, 0, canvasWidth, canvasHeight, fill = "grey")
	homeIcon = PhotoImage(file="HomeIcon.gif")
	canvas.data.e1 = Entry(canvas.data.root, width = 30)
	canvas.data.e2 = Entry(canvas.data.root, width = 30)
	canvas.data.e1.place(x = 150, y = 180)
	canvas.data.e2.place(x = 150, y = 330)
	canvas.create_image(500, 20 , image = homeIcon, anchor = NW)
	canvas.data.t = canvas.create_text(canvasWidth/2, 150, fill = "black",
	text = "Name your event.", font = "Helvetica 24 bold")
	canvas.create_text(canvasWidth/2, 300, fill = "black",
	text = "What event do you want to plan?", font = "Helvetica 24 bold")
	canvas.create_text(canvasWidth/2, 50, fill = "black", 
	text = "HOME", font = "Helvetica 36 bold underline")




def run():
	global canvas
	root = Tk()
	canvasWidth = 600
	canvasHeight = 600
	canvas = Canvas(root, width = canvasWidth, height = canvasHeight)
	canvas.pack()
	root.resizable(width=0, height=0)
	root.canvas = canvas.canvas = canvas
	class Struct: pass
	canvas.data = Struct()
	canvas.data.canvasWidth = canvasWidth
	canvas.data.canvasHeight = canvasHeight
	canvas.data.root = root
	init()
	root.bind("<Button-1>", mousePressed)
	root.bind("<Key>", keyPressed)
	delay = 1500
	canvas.after(delay, timerFired)
	root.mainloop()

run()
