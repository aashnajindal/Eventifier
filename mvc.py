from Tkinter import *

def init():
	splashScreen()
	canvas.data.venueFlag = False
	canvas.data.dateTimeFlag = False
	canvas.data.overviewFlag = False
	canvas.data.homeIcon = PhotoImage(file="HomeIcon.gif")
	canvas.data.eH_1 = Entry(canvas.data.root, width = 30)
	canvas.data.eH_2 = Entry(canvas.data.root, width = 30)
	canvas.data.bH_1 = Button(canvas.data.root,text = "Go",command = timeToGo1)
	canvas.data.bH_2 = Button(canvas.data.root, 
	image = canvas.data.homeIcon, command = homeScreen)
	canvas.data.eV_1 = Entry(canvas.data.root, width = 30)
	canvas.data.eV_2 = Entry(canvas.data.root, width = 30)
	canvas.data.bV_1 = Button(canvas.data.root, text = "Go", 
	command = timeToGo2)
	canvas.data.bV_2 = Button(canvas.data.root, text = "Search", 
	command = venueSearch)
	canvas.data.eD_1 = Entry(canvas.data.root, width = 30)
	canvas.data.eD_2 = Entry(canvas.data.root, width = 30)
	canvas.data.eD_3 = Entry(canvas.data.root, width = 30)
	canvas.data.bD_1 = Button(canvas.data.root, text = "Go", 
	command = timeToGo3)
	canvas.data.bT_1 = Button(canvas.data.root, text = "Venue",
	command = goToVenue)
	canvas.data.bT_2 = Button(canvas.data.root, text = "Date/Time",
	command = goToDateTime)
	canvas.data.bT_3 = Button(canvas.data.root, text = "Overview",
	command = goToOverview)
	canvas.data.allWidgets = [canvas.data.eH_1, canvas.data.eH_2,
	canvas.data.bH_1, canvas.data.eV_1, canvas.data.eV_2, canvas.data.bV_1,
	canvas.data.bV_2, canvas.data.eD_1, canvas.data.eD_2, canvas.data.eD_3,
	canvas.data.bD_1]

def venueSearch(): pass

def dateTimeScreen():
	deleteAll()
	canvasWidth = canvas.data.canvasWidth
	canvasHeight = canvas.data.canvasHeight
	canvas.create_rectangle(3, 3, canvasWidth, canvasHeight, fill = "#fef6e4")
	canvas.create_text(canvasWidth/2,30, text = canvas.data.eventName, 
	font = "Helvetica 35 bold underline", fill = "#00CED1")
	canvas.create_text(canvasWidth/2, 100, text = "DATE & TIME",
	font = "Helvetica 30 bold underline" )
	canvas.create_text(113, 200, text = "Date: ", 
	font = "Helvetica 25 bold")
	canvas.create_text(82, 300, text = "Start Time: ", 
	font = "Helvetica 25 bold")
	canvas.create_text(85, 400, text = "End Time: ", 
	font = "Helvetica 25 bold")
	canvas.data.eD_1.place(x = 170, y = 190)
	canvas.data.eD_2.place(x = 170, y = 290)
	canvas.data.eD_3.place(x = 170, y = 390)
	canvas.data.bD_1.place(x = 270, y = 470)
	canvas.data.bT_1.place(x = 10, y = 550)
	canvas.data.bT_2.place(x = 80, y = 550)
	canvas.data.bT_3.place(x = 180, y = 550)


def goToVenue():
	if(canvas.data.venueFlag == True): timeToGo1()

def goToDateTime(): 
	if(canvas.data.venueFlag == True): timeToGo2()
	if(canvas.data.dateTimeFlag == True): timeToGo2()

def goToOverview():
	if(canvas.data.dateTimeFlag == True): timeToGo3()
	if(canvas.data.overviewFlag == True): timeToGo3()

def timeToGo1():
	canvas.data.eventName = canvas.data.eH_1.get()
	canvas.data.eventType = canvas.data.eH_2.get()
	canvas.data.venueFlag = True
	venueScreen1()

def timeToGo2():
	canvas.data.eventVenue = canvas.data.eV_1.get()
	canvas.data.dateTimeFlag = True
	dateTimeScreen()

def timeToGo3():
	canvas.data.eventDate = canvas.data.eD_1.get()
	canvas.data.eventStartTime = canvas.data.eD_2.get()
	canvas.data.eventEndTime = canvas.data.eD_3.get()
	canvas.data.overviewFlag = True
	summaryScreen()

def summaryScreen():
	deleteAll()
	canvasWidth = canvas.data.canvasWidth
	canvasHeight = canvas.data.canvasHeight
	venueText = "Venue: " + canvas.data.eventVenue
	dateText = "Date: " + canvas.data.eventDate
	if(canvas.data.eventStartTime==""): timeText = "Time: "
	elif(canvas.data.eventStartTime!="" and canvas.data.eventEndTime==""):
		timeText = "Time: " + canvas.data.eventStartTime
	else:
		timeText = "Time: " + canvas.data.eventStartTime + " to " + canvas.data.eventEndTime
	canvas.create_rectangle(3, 3, canvasWidth, canvasHeight, fill = "#fef6e4")
	canvas.create_text(canvasWidth/2,30, text = canvas.data.eventName, 
	font = "Helvetica 35 bold underline", fill = "#00CED1")
	canvas.create_text(canvasWidth/2, 100, text = "OVERVIEW",
	font = "Helvetica 30 bold underline")
	canvas.create_text(50, 200, text = venueText, 
	font = "Helvetica 20 bold", anchor = NW)
	canvas.create_text(50, 300, text = dateText, 
	font = "Helvetica 20 bold", anchor = NW)
	canvas.create_text(50, 400, text = timeText, 
	font = "Helvetica 20 bold", anchor = NW)
	canvas.data.bT_1.place(x = 10, y = 550)
	canvas.data.bT_2.place(x = 80, y = 550)
	canvas.data.bT_3.place(x = 180, y = 550)


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
	canvas.data.bT_1.place(x = 10, y = 550)
	canvas.data.bT_2.place(x = 80, y = 550)
	canvas.data.bT_3.place(x = 180, y = 550)

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
	root.title("Eventifier")
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
