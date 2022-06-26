# Name: Rafael Diaz
# Filename: FseProject.py
# Description: Create a program that allows the staff of a movie theater to buy tickets of a movie for a customer and be able to add movies manually. 
# Date: June 6, 2022
# Author: 
# Teacher: 
from tkinter import *


class Movie(): 
  "Create the blueprint for the movie object"
  def __init__(self, name, description, time):
    self._name = name
    self._description = description
    self._time = time
    self._seats = {"L1":[0,"", "grey", NORMAL], "L2":[0,"", "grey", NORMAL],"L3":[0,"","grey", NORMAL], "L4":[0,"","grey", NORMAL],"L5":[0,"","grey", NORMAL], "L6":[0,"","grey", NORMAL],"M1":[0,"","grey", NORMAL],"M2":[0,"","grey", NORMAL],"M3":[0,"","grey", NORMAL],"M4":[0,"","grey", NORMAL],"M5":[0,"","grey", NORMAL],"M6":[0,"","grey", NORMAL],"M7":[0,"","grey", NORMAL],"M8":[0,"","grey", NORMAL],"M9":[0,"","grey", NORMAL],"R1":[0,"","grey", NORMAL],"R2":[0,"","grey", NORMAL],"R3":[0,"","grey", NORMAL],"R4":[0,"","grey", NORMAL],"R5":[0,"","grey", NORMAL],"R6":[0,"","grey", NORMAL]} #stores the data for each of the seat. 0 represents that the seat is not taken and 1 if it's taken. The "" represents the name of who boughts the seat. The NORMAL is to allow the user to select the seat then when it's chosen then it's turn disabled. 

    

movieList = [] #contains all the movie available. 
movieList.append(Movie("Avengers", "Cool movie", "2:05pm")) #sample data
movieList.append(Movie("Doctor Strange", "Cool movie", "5:05pm"))
movieList.append(Movie("Doctor test", "Cool movie", "5:05pm"))


def seatChoose(seatNum,selectedMovie):
  "make the seat (button) green if the user selects it first then grey if it is selected again"
  if selectedMovie._seats[seatNum][0] == 0: 
    selectedMovie._seats[seatNum][0] = 1 
    btnSeat[seatNum]["bg"] = "green"
  elif selectedMovie._seats[seatNum][0] == 1:
    selectedMovie._seats[seatNum][0] = 0
    btnSeat[seatNum]["bg"] = "grey"

def BuyTicket(name, cardInfo, selectedMovie):
  "perform the following actions when the user buys the seat"
  selectedSeats = []
  for key in selectedMovie._seats.keys(): #find all the taken seats 
    if selectedMovie._seats[key] == [1,"", "grey", NORMAL]:
      selectedSeats.append(key)

  for key in selectedSeats: #make all taken seats (button) and make it red and not be used anymore (disabled)
    selectedMovie._seats[key] = [1, f"{name}", "red", DISABLED]
    btnSeat[key]["bg"] = "red"
    btnSeat[key]["state"] = DISABLED

  #create the receipt window, pop up when the user clicked the buy ticket button
  receipt = Toplevel(mainScreen)
  receipt.geometry("250x100")
  lblReceipt = Label(receipt, text = f"{name},have purchase the following seats\n {str(selectedSeats)[1:-1]} \nusing the credit card number starting with\n{cardInfo[:3]}-XXX-XXX").place(x = 0, y = 0)
    
  print(selectedSeats)
def seatBuyFunc(selectedMovie):
  "create another window when the function is called"
  seatOptionScreen = Toplevel(mainScreen)
  #customize the window
  seatOptionScreen.geometry("1000x500")
  seatOptionScreen.config(bg = "#2596be")
  seatOptionScreen.title("Seats Available")
  global btnSeat
  #create the seats available 
  btnSeat = {"L1":Button(seatOptionScreen, width=5, command = lambda: seatChoose("L1",selectedMovie), bg = selectedMovie._seats["L1"][2], state = selectedMovie._seats["L1"][3]),
   "L2":Button(seatOptionScreen, width=5, command = lambda: seatChoose("L2",selectedMovie), bg = selectedMovie._seats["L2"][2], state = selectedMovie._seats["L2"][3]),
   "L3":Button(seatOptionScreen, width=5, command = lambda: seatChoose("L3",selectedMovie), bg = selectedMovie._seats["L3"][2], state = selectedMovie._seats["L3"][3]),
    "L4":Button(seatOptionScreen, width=5, command = lambda: seatChoose("L4",selectedMovie), bg = selectedMovie._seats["L4"][2], state = selectedMovie._seats["L4"][3]),
    "L5":Button(seatOptionScreen, width=5, command = lambda: seatChoose("L5",selectedMovie), bg = selectedMovie._seats["L5"][2], state = selectedMovie._seats["L5"][3]),
    "L6":Button(seatOptionScreen, width=5, command = lambda: seatChoose("L6",selectedMovie), bg = selectedMovie._seats["L6"][2], state = selectedMovie._seats["L6"][3]),
    "M1":Button(seatOptionScreen, width=5, command = lambda: seatChoose("M1",selectedMovie), bg = selectedMovie._seats["M1"][2], state = selectedMovie._seats["M1"][3]),
    "M2":Button(seatOptionScreen, width=5, command = lambda: seatChoose("M2",selectedMovie), bg = selectedMovie._seats["M2"][2], state = selectedMovie._seats["M2"][3]),
    "M3":Button(seatOptionScreen, width=5, command = lambda: seatChoose("M3",selectedMovie), bg = selectedMovie._seats["M3"][2], state = selectedMovie._seats["M3"][3]),
    "M4":Button(seatOptionScreen, width=5, command = lambda: seatChoose("M4",selectedMovie), bg = selectedMovie._seats["M4"][2], state = selectedMovie._seats["M4"][3]),
    "M5":Button(seatOptionScreen, width=5, command = lambda: seatChoose("M5",selectedMovie), bg = selectedMovie._seats["M5"][2], state = selectedMovie._seats["M5"][3]),
    "M6":Button(seatOptionScreen, width=5, command = lambda: seatChoose("M6",selectedMovie), bg = selectedMovie._seats["M6"][2], state = selectedMovie._seats["M6"][3]),
    "M7":Button(seatOptionScreen, width=5, command = lambda: seatChoose("M7",selectedMovie), bg = selectedMovie._seats["M7"][2], state = selectedMovie._seats["M7"][3]),
    "M8":Button(seatOptionScreen, width=5, command = lambda: seatChoose("M8",selectedMovie), bg = selectedMovie._seats["M8"][2], state = selectedMovie._seats["M8"][3]),
    "M9":Button(seatOptionScreen, width=5, command = lambda: seatChoose("M9",selectedMovie), bg = selectedMovie._seats["M9"][2], state = selectedMovie._seats["M9"][3]),
    "R1":Button(seatOptionScreen, width=5, command = lambda: seatChoose("R1",selectedMovie), bg = selectedMovie._seats["R1"][2], state = selectedMovie._seats["R1"][3]),
    "R2":Button(seatOptionScreen, width=5, command = lambda: seatChoose("R2",selectedMovie), bg = selectedMovie._seats["R2"][2], state = selectedMovie._seats["R2"][3]),
    "R3":Button(seatOptionScreen, width=5, command = lambda: seatChoose("R3",selectedMovie), bg = selectedMovie._seats["R3"][2], state = selectedMovie._seats["R3"][3]),
    "R4":Button(seatOptionScreen, width=5, command = lambda: seatChoose("R4",selectedMovie), bg = selectedMovie._seats["R4"][2], state = selectedMovie._seats["R4"][3]),
    "R5":Button(seatOptionScreen, width=5, command = lambda: seatChoose("R5",selectedMovie), bg = selectedMovie._seats["R5"][2], state = selectedMovie._seats["R5"][3]),
    "R6":Button(seatOptionScreen, width=5, command = lambda: seatChoose("R6",selectedMovie), bg = selectedMovie._seats["R6"][2], state = selectedMovie._seats["R6"][3])}
  #output the seats
  btnSeat["L1"].place(x = 20, y = 130)
  btnSeat["L2"].place(x = 20, y = 160)
  btnSeat["L3"].place(x = 20, y = 190)
  btnSeat["L4"].place(x = 80, y = 130)
  btnSeat["L5"].place(x = 80, y = 160)
  btnSeat["L6"].place(x = 80, y = 190)
  btnSeat["M1"].place(x = 200, y = 130)
  btnSeat["M2"].place(x = 200, y = 160)
  btnSeat["M3"].place(x = 200, y = 190)
  btnSeat["M4"].place(x = 260, y = 130)
  btnSeat["M5"].place(x = 260, y = 160)
  btnSeat["M6"].place(x = 260, y = 190)
  btnSeat["M7"].place(x = 320, y = 130)
  btnSeat["M8"].place(x = 320, y = 160)
  btnSeat["M9"].place(x = 320, y = 190)
  btnSeat["R1"].place(x = 440, y = 130)
  btnSeat["R2"].place(x = 440, y = 160)
  btnSeat["R3"].place(x = 440, y = 190)
  btnSeat["R4"].place(x = 500, y = 130)
  btnSeat["R5"].place(x = 500, y = 160)
  btnSeat["R6"].place(x = 500, y = 190)

  #create the label for the window
  lblNameBuyer = Label(seatOptionScreen, text = "Name:",bg = "#2596be").place(x = 750, y =130)
  lblCardName = Label(seatOptionScreen, text = "Credit Card number:", bg = "#2596be").place(x = 680, y =160)
  lblChosenSeatEx = Label(seatOptionScreen, text = "- Seat Chosen", font = ("","10", "bold"), bg = "#2596be").place(x=250, y = 0)
  lblAvailableSeatEx = Label(seatOptionScreen, text = "- Available Seat", font = ("","10", "bold"), bg = "#2596be").place(x=450, y = 0)
  lblTakenSeatEx = Label(seatOptionScreen, text = "- Seat Chosen", font = ("","10", "bold"), bg = "#2596be").place(x=650, y = 0)
  
  #create the entry for the window
  entNameBuyer = Entry(seatOptionScreen); entNameBuyer.place(x = 800, y = 130)
  entCardName = Entry(seatOptionScreen); entCardName.place(x = 800, y = 160)

  #create the button for the window
  btnBuyTicket = Button(seatOptionScreen, text = "Buy Ticket!", command = lambda: BuyTicket(entNameBuyer.get(),entCardName.get(), selectedMovie)).place(x = 800, y = 190)
  btnChosenSeatEx = Button(seatOptionScreen, bg = "green",width= 5 ,state= DISABLED).place(x=200, y = 0)
  btnAvailableSeatEx = Button(seatOptionScreen, bg = "grey",width= 5 ,state= DISABLED).place(x=400, y = 0)
  btnTakenSeatEx = Button(seatOptionScreen, bg = "red",width= 5 ,state= DISABLED).place(x=600, y = 0)
  





def movieOptionFunc():
  "create another window when function is called"
  ycoord = 80 #the starting y coordinate for the label, radiubton and for the button is relative to this coordinate. 
  movieOptionScreen = Toplevel(mainScreen)
  #customize the window
  movieOptionScreen.geometry("700x500")
  movieOptionScreen.config(bg= "#2596be")
  movieOptionScreen.title("Movies Available")
  var = IntVar()

  lblMoviesAvailable = Label(movieOptionScreen, text = "Choose from the available movies", font = ("","20", "bold"), bg = "#2596be").place(x = 120, y = 20)
  movieCounter = 0 #represents the number of the movies available
  for movie in movieList: #loop through all the movies available and output them onto the screen.
    lblmovieoutput = Label(movieOptionScreen, bg = "#2596be" ,text = f"Movie name: {movie._name}  Movie description: {movie._description}    Movie time: {movie._time}").place(x = 0, y = ycoord)
    radioBtn = Radiobutton(movieOptionScreen, variable=var, value = movieCounter, bg = "#2596be").place(x=650,y=ycoord)
    movieCounter += 1 
    ycoord += 50
  btnSelectMovie =  Button(movieOptionScreen, text = "Buy ticket", command = lambda: seatBuyFunc(movieList[var.get()])).place(x=350, y = ycoord)
   


def addMovInClass(name, description, time):
  global movieList
  movieList.append(Movie(name,description,time))

def addMovieFunc():
  "create another window function is called"
  addMovieScreen = Toplevel(mainScreen)
  #customize the window 
  addMovieScreen.geometry("500x500")
  addMovieScreen.config(bg = "#2596be")
  addMovieScreen.title("Add Movies")

  #create the label for the window
  lblAddMovie = Label(addMovieScreen, text = "Add Movies", font = ("","20", "bold"), bg = "#2596be").place(x = 180, y = 50)
  lblNameMovie = Label(addMovieScreen, text = "Name of the movie:", bg = "#2596be").place(x = 100, y = 150)
  lblDescrMovie = Label(addMovieScreen, text = "Description of the movie:", bg ="#2596be").place(x = 70, y = 200)
  lblTimeMovie = Label(addMovieScreen, text = "Time Slot of the Movie: (ex. 9:30pm)", bg = "#2596be").place(x = 20, y = 250)

  #create the entry for the window
  entNameMovie = Entry(addMovieScreen); entNameMovie.place(x=220,y = 150) 
  entDescrpMovie = Entry(addMovieScreen); entDescrpMovie.place(x=220,y = 200) 
  entTimeMovie = Entry(addMovieScreen); entTimeMovie.place(x=220,y = 250)

  #create the button for the window
  btnAddMovie = Button(addMovieScreen, text = "Add movie!", command= lambda: addMovInClass(entNameMovie.get(),entDescrpMovie.get(),entTimeMovie.get())).place(x = 200,y = 300)





mainScreen = Tk() #creates the main screen 

#customize the setting of the window
mainScreen.geometry("500x500")
mainScreen.title("Windsor Movie Theater")
mainScreen.config(bg="#2596be")

#create the label for the main screen
lblWelcome = Label(mainScreen, text = "   Welcome \n To \n  Windsor Movie Theater", font = ("","20", "bold"), bg = "#2596be").place(x = 80, y = 20)

#create the button for the main screen
btnTicketScreen = Button(mainScreen, text = "Check movies", command= lambda: movieOptionFunc()).place(x=160,y=150)
btnAddMovieScreen = Button(mainScreen, text = "Add movie", command = lambda: addMovieFunc()).place(x = 260, y = 150)


mainScreen.mainloop()