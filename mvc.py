from Tkinter import *

def mousePressed(event): pass

def keyPressed(event): pass

def init():
	splashScreen()

def splashScreen():
	canvasWidth = canvas.data.canvasWidth
	canvasHeight = canvas.data.canvasHeight
	canvas.create_rectangle(0, 0, canvasWidth, canvasHeight, fill = "black")
	canvas.create_text(canvasWidth/2, canvasHeight/2, fill = "purple",
	text = "EVENTIFIER", font = "Helvetica 80 bold")

def timerFired():pass

def redrawAll():pass

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
	init()
	root.bind("<Button-1>", mousePressed)
	root.bind("<Key>", keyPressed)
	timerFired()
	root.mainloop()

run()
