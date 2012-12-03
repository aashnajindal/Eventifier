from Tkinter import *
from yelp import *
from json import dumps

class Event(object):
	def __init__(self, name = "", category = "", venue = "", 
	date = "", startTime = "", endTime = ""):
		self.name = name
		self.type = category
		self.venue = venue
		self.date = date
		self.startTime = startTime
		self.endTime = endTime

	def getTerm(self):
		return self.type

class Venue(object):
	def __init__(self, name = "", address = "", rating = -1, 
	phone = "", website = "", icon = ""):
		self.name = name
		self.address = address
		self.rating = rating
		self.phone = phone
		self.website = website
		self.icon = icon

def mousePressed(event):
	if(canvas.data.venueSearchFlag==True and event.y>=170-canvas.data.scroll):
		canvas.data.mousePressed = True
		canvas.data.y = 170-canvas.data.scroll+event.y/30
		try: 
			#if(canvas.data.keyIndex>=0):
			canvas.data.keyIndex = (event.y-170+canvas.data.scroll)/30
			canvas.data.key =  canvas.data.allVenues[canvas.data.keyIndex]["Name"]
		except: return
		venueSearchScreen()

def keyPressed(event):
	if(canvas.data.venueSearchFlag):
		if(event.keysym == "Up"):scrollUp()
		if(event.keysym == "Down"): scrollDown()

def scrollUp():
	if(canvas.data.venueSearchFlag and canvas.data.scroll >= 0):
		canvas.data.scroll-=10
		venueSearchScreen()

def scrollDown():
	if(canvas.data.venueSearchFlag):
		canvas.data.scroll+=10
		venueSearchScreen()

def init():
	splashScreen()
	canvas.data.keyIndex = -1
	canvas.data.mousePressed = False
	canvas.data.venueFlag = False
	canvas.data.scroll = 0
	canvas.data.down = 0
	canvas.data.dateTimeFlag = False
	canvas.data.overviewFlag = False
	canvas.data.venueSearchFlag = False
	canvas.data.homeIcon= PhotoImage(file="HomeIcon.gif")
	canvas.data.eH_1 = Entry(canvas.data.root, width = 30)
	canvas.data.eH_2 = Entry(canvas.data.root, width = 30)
	canvas.data.bH_1 = Button(canvas.data.root,text = "Go",command=timeToGo1)
	canvas.data.bH_2 = Button(canvas.data.root, 
	image = canvas.data.homeIcon, bg = "#fef6e4", bd = 2, command =homeScreen)
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

def venueSearch():
	canvas.data.scroll = 0
	canvas.data.allVenues = dict()
	options.term = canvas.data.event.getTerm()
	options.location = canvas.data.eV_2.get()
	url_params['term'] = options.term
	url_params["location"] = options.location
	response = request(options.host, '/v2/search', url_params, 
	options.consumer_key, options.consumer_secret, options.token, 
	options.token_secret)
	#try:
	"""for el in response["businesses"]:
		canvas.data.allVenues[el["name"]] = dict()
		if(el.get("display_phone")): 
			canvas.data.allVenues[el["name"]]["phone"] = el["display_phone"]
		if(el.get("rating")): 
			canvas.data.allVenues[el["name"]]["rating"] = el["rating"]
		if(el.get("url")): 
			canvas.data.allVenues[el["name"]]["website"] = el["url"]
		s = ""
		for i in xrange(len(el["location"]["display_address"])):
			s += el["location"]["display_address"][i] + ",\n"
		s = s[0: len(s)-2]
		canvas.data.allVenues[el["name"]]["address"] = s

	print dumps(canvas.data.allVenues)"""
	venueSearchScreen()
	#except KeyError:
	#	print"Please put in a zipcode"
	#except Exception as e:
		#print e

def venueSearchScreen():
	deleteAll()
	canvas.data.venueSearchFlag = True
	canvasWidth = canvas.data.canvasWidth
	canvasHeight = canvas.data.canvasHeight
	canvas.create_rectangle(3, 3, canvasWidth, canvasHeight, fill = "#fef6e4")
	canvas.create_text(canvasWidth/2,30-canvas.data.scroll,
	text = canvas.data.event.name, font = "Helvetica 35 bold underline",
	fill = "#00CED1")
	canvas.create_text(canvasWidth/2,80-canvas.data.scroll, text = "RESULTS", 
	font = "Helvetica 30 bold underline")
	canvas.create_text(170,150-canvas.data.scroll, 
	text = "Choose a venue or click Venue to go back", 
	font = "Helvetica 15 bold")
	space = 0
	canvas.data.allVenues = [
			 {"Name": "David Guetta",
							"Album": "Nothing But the Beat",
							"Num Tracks": "32"
							},
			{"Name": "Michael Jackson",
							"Album": "Bad",
							"Num Tracks": "10"
							},
			{"Name": "Skrillex",
							"Album": "Scary Monsters and nice Spirits",
							"Num Tracks": "9"
							},
			{"Name": "Sum 41",
							"Album": "Chuck",
							"Num Tracks": "13"
							},
			{"Name": "Seal",
							"Album": "Soul",
							"Num Tracks": "12"
							},
			{"Name": "Justin Timberlake",
							"Album": "What Goes Around... Comes Around",
							"Num Tracks": "5"
							},
			{"Name": "Red Hot Chilli Peppers",
							"Album": "Stadium Arcadium",
							"Num Tracks": "28"
							},
			{"Name": "Bruno Mars",
							"Album": "Doo-Wops and Hooligans",
							"Num Tracks": "10"
							},
			{  "Name": "Jason Mraz",
							"Album": "We Sing. We Dance. We Steal Things.",
							"Num Tracks": "12"
							}
			]
	for values in canvas.data.allVenues:
		if(canvas.data.mousePressed==False):
			print ""
			canvas.create_rectangle(3, 170+space*30-canvas.data.scroll, 
			580, 170+(space+1)*30-canvas.data.scroll)
			canvas.create_text(5, 170+(2*space+1)*15-canvas.data.scroll, 
			text = values["Name"], anchor = NW)
			space+=1
		else: 
			venueSearchScreen2()

def venueSearchScreen2():
	space = 0
	for i in xrange(len(canvas.data.allVenues)):
		if(i<canvas.data.keyIndex):
				canvas.create_rectangle(3, 170+space*30-canvas.data.scroll,
				580, 170+(space+1)*30-canvas.data.scroll)
				canvas.create_text(5, 170+(2*space+1)*15-canvas.data.scroll,
				text = canvas.data.allVenues[i]["Name"], anchor = NW)
				space+=1
		elif(i == canvas.data.keyIndex):
			canvas.create_rectangle(3, 170+space*30-canvas.data.scroll,
			580, 170+(space+3)*30-canvas.data.scroll)
			canvas.create_text(5, 170+(2*space+1)*15-canvas.data.scroll,
			text = canvas.data.allVenues[i]["Name"], anchor = NW)
			canvas.create_text(5, 170+(2*space+1)*15+20-canvas.data.scroll,
			text = canvas.data.allVenues[i]["Album"], anchor = NW)
			canvas.create_text(5, 170+(2*space+1)*15+40-canvas.data.scroll,
			text = canvas.data.allVenues[i]["Num Tracks"], anchor = NW)
			space+=1
		else:
			canvas.create_rectangle(3, 170+(space+2)*30-canvas.data.scroll,
			580, 170+(space+3)*30-canvas.data.scroll)
			canvas.create_text(5, 170+(2*space+5)*15-canvas.data.scroll,
			text = canvas.data.allVenues[i]["Name"], anchor = NW)
			space+=1




def dateTimeScreen():
	deleteAll()
	canvas.data.venueSearchFlag = False
	canvas.data.mousePressed = False
	canvasWidth = canvas.data.canvasWidth
	canvasHeight = canvas.data.canvasHeight
	canvas.create_rectangle(3, 3, canvasWidth, canvasHeight, fill = "#fef6e4")
	canvas.create_text(canvasWidth/2,30, text = canvas.data.event.name, 
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
	canvas.data.event = Event()
	canvas.data.event.name = canvas.data.eH_1.get()
	canvas.data.event.type = canvas.data.eH_2.get()
	canvas.data.venueFlag = True
	venueScreen1()

def timeToGo2():
	canvas.data.venue = Venue()
	canvas.data.venue.name = canvas.data.eV_1.get()
	canvas.data.event.venue = canvas.data.venue
	canvas.data.dateTimeFlag = True
	dateTimeScreen()

def timeToGo3():
	canvas.data.event.date = canvas.data.eD_1.get()
	canvas.data.event.startTime = canvas.data.eD_2.get()
	canvas.data.event.endTime = canvas.data.eD_3.get()
	canvas.data.overviewFlag = True
	summaryScreen()

def summaryScreen():
	deleteAll()
	canvas.data.venueSearchFlag = False
	canvas.data.mousePressed = False
	canvasWidth = canvas.data.canvasWidth
	canvasHeight = canvas.data.canvasHeight
	venueText = "Venue: " + canvas.data.venue.name
	dateText = "Date: " + canvas.data.event.date
	if(canvas.data.event.startTime==""): timeText = "Time: "
	elif(canvas.data.event.startTime!="" and canvas.data.event.endTime==""):
		timeText = "Time: " + canvas.data.event.startTime
	else:
		timeText = "Time: " + canvas.data.event.startTime + " to " + canvas.data.event.endTime
	canvas.create_rectangle(3, 3, canvasWidth, canvasHeight, fill = "#fef6e4")
	canvas.create_text(canvasWidth/2,30, text = canvas.data.event.name, 
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
	canvas.data.venueSearchFlag = False
	canvas.data.mousePressed = False
	canvasWidth = canvas.data.canvasWidth
	canvasHeight = canvas.data.canvasHeight
	canvas.create_rectangle(3, 3, canvasWidth, canvasHeight, fill = "#fef6e4")
	canvas.create_text(canvasWidth/2,30, text = canvas.data.event.name, 
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
	canvas.data.eH_2.insert(0, "Birthday Party")

def run():
	global canvas
	root = Tk()
	canvasWidth = 600
	canvasHeight = 600
	root.title("Eventifier")
	sR_1 = Scrollbar(root)
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
	canvas.after(delay, homeScreen)
	root.mainloop()

run()
