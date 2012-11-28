from Tkinter import *

def init():
	splashScreen()
	#tabFlags = dict()
	#tabFlags["home"] = True
	#tabFlags["venuePage"] = False
	#tabFlags["dateTimePage"] = False
	#tabFlags["summaryPage"] = False
	#canvas.data.tabFlags = tabFlags
	canvas.data.homeIcon = PhotoImage(file="HomeIcon.gif")
	canvas.data.eH_1 = Entry(canvas.data.root, width = 30)
	canvas.data.eH_2 = Entry(canvas.data.root, width = 30)
	canvas.data.bH_1 = Button(canvas.data.root,text = "GO",command = timeToGo1)
	canvas.data.bH_2 = Button(canvas.data.root, 
	image = canvas.data.homeIcon, command = homeScreen)
	canvas.data.eV_1 = Entry(canvas.data.root, width = 30)
	canvas.data.eV_2 = Entry(canvas.data.root, width = 30)
	canvas.data.bV_1 = Button(canvas.data.root, text = "Go", 
	command = dateTimeScreen)
	canvas.data.bV_2 = Button(canvas.data.root, text = "Search", 
	command = venueSearch)
	canvas.data.allWidgets = [canvas.data.eH_1, canvas.data.eH_2,
	canvas.data.bH_1, canvas.data.eV_1, canvas.data.eV_2, canvas.data.bV_1,
	canvas.data.bV_2]

def venueSearch(): pass

def dateTimeScreen(): pass

def timeToGo1():
	canvas.data.eventName = canvas.data.eH_1.get()
	canvas.data.eventType = canvas.data.eH_2.get()
	venueScreen1()

def venueScreen1():
	deleteAll()
	canvasWidth = canvas.data.canvasWidth
	canvasHeight = canvas.data.canvasHeight
	canvas.create_rectangle(3, 3, canvasWidth, canvasHeight, fill = "#fef6e4")
	canvas.create_text(canvasWidth/2,30, text = canvas.data.eventName, 
	font = "Helvetica 35 bold underline", fill = "#00CED1")
	canvas.create_text(canvasWidth/2, 100, text = "VENUE",
	font = "Helvetica 30 bold underline" )
	canvas.create_text(canvasWidth/2, 200, 
	text = "Please enter your own venue", font = "Helvetica 15 bold" )
	canvas.create_text(canvasWidth/2, 320, text = "OR", 
	font = "Helvetica 25 bold" )
	canvas.create_text(canvasWidth/2, 400, 
	text = "Please enter city or zipcode", font = "Helvetica 15 bold")
	canvas.data.eV_1.place(x = 170, y = 220)
	canvas.data.eV_2.place(x = 170, y = 420)
	canvas.data.bV_1.place(x = 375, y = 250)
	canvas.data.bV_2.place(x = 350, y = 450)

def deleteAll():
	canvas.delete(ALL)
	for i in xrange(len(canvas.data.allWidgets)):
		canvas.data.allWidgets[i].place_forget()

def splashScreen():
	canvasWidth = canvas.data.canvasWidth
	canvasHeight = canvas.data.canvasHeight
	canvas.create_rectangle(0, 0, canvasWidth, canvasHeight, fill = "black")
	canvas.create_text(canvasWidth/2, canvasHeight/2, fill = "purple",
	text = "EVENTIFIER", font = "Helvetica 80 bold")

def homeScreen():
	deleteAll()
	canvasWidth = canvas.data.canvasWidth
	canvasHeight = canvas.data.canvasHeight
	canvas.create_rectangle(3, 3, canvasWidth, canvasHeight, fill = "#fef6e4")
	canvas.data.eH_1.place(x = 165, y = 180)
	canvas.data.eH_2.place(x = 165, y = 330)
	canvas.data.bH_1.place(x = 370, y = 360)
	canvas.data.bH_2.place(x = 530, y = 20)
	canvas.data.eH_1.delete(0 , len(canvas.data.eH_1.get()))
	canvas.data.eH_2.delete(0 , len(canvas.data.eH_2.get()))
	canvas.create_text(canvasWidth/2, 150, fill = "black",
	text = "Name your event.", font = "Helvetica 24 bold")
	canvas.create_text(canvasWidth/2, 300, fill = "black",
	text = "What event do you want to plan?", font = "Helvetica 24 bold")
	canvas.create_text(canvasWidth/2, 50, fill = "black", 
	text = "HOME", font = "Helvetica 36 bold underline")
	canvas.data.eH_1.insert(0, "Plan A")
	canvas.data.eH_2.insert(0, "Party")


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
	delay = 1500
	canvas.after(delay, homeScreen)
	root.mainloop()

run()
