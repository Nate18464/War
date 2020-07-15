from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import random

# class for Cards
class Card:
    #Initialize itself with a value and a photoimage
    def __init__(self, num):
        self.value = num%13
        if self.value < 9:
            name = str(self.value + 2)
        elif self.value == 9:
            name = "Jack"
        elif self.value == 10:
            name = "Queen"
        elif self.value == 11:
            name = "King"
        else:
            name = "Ace"
        if num < 13:
            suit = "Hearts"
        elif num < 26:
            suit = "Diamonds"
        elif num < 39:
            suit = "Clubs"
        else:
            suit = "Spades"
        self.photo = ImageTk.PhotoImage(Image.open(name + " " + suit + ".jpg"))

    def photoImage(self):
        return self.photo

    def value(self):
        return self.value

def deleteScreen(*args):
    # Remove previous frame from screen
    frame1.destroy()
    # Set player name
    PlayerCardLabel["text"] = name.get() + "'s cards"
    # Set player number of cards
    playerNumCards["text"] = name.get() + "'s # of cards: " + str(len(playerdeck))
    # Rebind Enter to bring us to the third screen
    root.bind('<Return>', thirdScreen)

#function to get from the second screen after clicking the submit on the first screen
def secondScreen(*args):
    # Rebind Enter to bring us to the third screen
    root.bind('<Return>', thirdScreen)
    # Set AICard image to back of card
    AICard["image"] = cardBack
    # Set PlayerCard image to back of card
    PlayerCard["image"] = cardBack
    # Change play button text and command
    Play["text"] = "Click the button to flip your card!"
    Play["command"] = thirdScreen
    # Reset number of cards in each deck
    aiNumCards["text"] = "AI's # of cards: " + str(len(aideck))
    playerNumCards["text"] = name.get() + "'s # of cards: " + str(len(playerdeck))
    if war[0] == 1:
        # Reset display to empty string if not on war
        display["text"] = ""
        warCardDisplay["text"] == ""
    
def thirdScreen(*args):
    # Create a label for the ai's card using the top of the ai player's deck
    AICard["image"] = aideck[0].photoImage()
    # Create a label for the player's card using the top of the player's deck
    PlayerCard["image"] = playerdeck[0].photoImage()
    # Create a button that says next card and will repeat this function
    Play["text"] = "Next card"
    if Card.value(aideck[0]) > Card.value(playerdeck[0]):
        aiWin()
    elif Card.value(aideck[0]) < Card.value(playerdeck[0]):
        playerWin()
    else:
        War() 
    if Card.value(aideck[0]) != Card.value(playerdeck[0]):
        winSetup()
    anySetup()
    # Add extra padding to look better spaced
    for child in frame2.winfo_children(): child.grid_configure(padx=5, pady=5)

def War(*args):
    display["text"] = "War #" + str(war[0])
    war[0] += 1
    for c in range(4):
        if len(playerdeck) == 1:
            break
        wardeck.append(playerdeck[0])
        playerdeck.pop(0)
        
    for c in range(4):
        if len(aideck) == 1:
            break
        wardeck.append(aideck[0])
        aideck.pop(0)
    warCardDisplay["text"] = "Number of cards in the war so far: " + str(len(wardeck))

def playerWin(*args):
    display["text"] = name.get() + " won this round"
    # Add won cards to player deck
    playerdeck.append(aideck[0])
    playerdeck.append(playerdeck[0])
    for c in range(len(wardeck)-1, -1, -1):
        playerdeck.append(wardeck[c])
        wardeck.pop(c)

def aiWin(*args):
    display["text"] = "AI won this round"
    # Add won cards to ai deck
    aideck.append(aideck[0])
    aideck.append(playerdeck[0])
    for c in range(len(wardeck)-1, -1, -1):
        aideck.append(wardeck[c])
        wardeck.pop(c)
    

def winSetup(*args):
    Play["text"] = "Next round"
    # Remove the top of each deck
    aideck.pop(0)
    playerdeck.pop(0)
    # Reset war # to 1
    war[0] = 1

def anySetup(*args):
    # Rebind button to bring us to the second screen
    Play["command"] = secondScreen
    # Rebind Enter to bring us to the second screen
    root.bind('<Return>', secondScreen)
    if len(playerdeck) == 0:
        aiGame()
    if len(aideck) == 0:
        playerGame()

def aiGame(*args):
    # Rebind Enter to bring us to the game over screen
    root.bind('<Return>', gameOver)
    # Set AICard image to back of card
    AICard["image"] = cardBack
    # Remove player card
    PlayerCard.destroy()
    # Change play button text and command
    Play["text"] = "Click the button to end game"
    Play["command"] = gameOver
    # Reset number of cards in each deck
    aiNumCards["text"] = "AI's # of cards: " + str(len(aideck))
    playerNumCards["text"] = name.get() + "'s # of cards: " + str(len(playerdeck))
    # Reset display to say ai won
    display["text"] = "AI won the game!"

def playerGame(*args):
    # Rebind Enter to bring us to the game over screen
    root.bind('<Return>', gameOver)
    # Remove ai card
    AICard.destroy()
    # Set PlayerCard image to back of card
    PlayerCard.destroy()
    # Change play button text and command
    Play["text"] = "Click the button to end game"
    Play["command"] = gameOver
    # Reset number of cards in each deck
    aiNumCards["text"] = "AI's # of cards: " + str(len(aideck))
    playerNumCards["text"] = name.get() + "'s # of cards: " + str(len(playerdeck))
    # Reset display to say ai won
    display["text"] = name.get() + " won the game!"

def gameOver(*args):
    frame2.destroy()

# Create a root windown to show to the screen and title it War
root = Tk()
root.title("War")

# Create a deck of all 52 two cards, unrandomized
deck = []
for c in range(52):
    deck.append(Card(c))
# Create aideck and playerdeck with randomly shuffled cards for each player
aideck = []
playerdeck = []
for c in range(51, -1, -1):
    randnum = random.randint(0,c)
    if c%2 == 0:
        aideck.append(deck[randnum])
    else:
        playerdeck.append(deck[randnum])
    deck.pop(randnum)
# Create a frame
frame1 = ttk.Frame(root, padding = "3 3 12 12")
frame1.grid(column=0, row=0, sticky=(N, W, E, S))
# Create a second frame
frame2 = ttk.Frame(root, padding = "3 3 12 12")
frame2.grid(column=0, row=0, sticky=(N, W, E, S))
# Lower this second frame below the first frame
frame2.lower(frame1)
# Create a name label
nameLabel = ttk.Label(frame1, text = "Your Name: ").grid(row = 0, column = 0, sticky = (N, W, E, S))
# Create a string variable to hold the name of the player
name = StringVar()
# Create an text box for the player to type his or her name into
nameEntry = ttk.Entry(frame1, textvariable = name)
nameEntry.grid(row=0, column=1, sticky = (N, W, E, S))
# Create a button that will go to the second screen when pressed
Submit = ttk.Button(frame1, text = "Submit!", command = deleteScreen) 
Submit.grid(row=1, column=1, sticky = (N, W, E, S))
# Add extra spacing around each widget 
for child in frame1.winfo_children(): child.grid_configure(padx=5, pady=5)
#Create a photo image of the back of a card to be used later
cardBack = ImageTk.PhotoImage(Image.open("Card Back.jpg"))
# Create the image of the back of a card for ai's card
AICard = ttk.Label(frame2, image = cardBack)
AICard.grid(row = 1, column = 0, sticky = (N, W, E, S))
# Create a label for ai's card
AICardLabel = ttk.Label(frame2, text = "AI's Card: ").grid(row = 0, column = 0, sticky = (N, W, E, S))
# Create a label for player's card
PlayerCardLabel = ttk.Label(frame2)
PlayerCardLabel.grid(row = 0, column = 1, sticky = (N, W, E, S))
# Create the image of the back of a card for player's card
PlayerCard = ttk.Label(frame2, image = cardBack)
PlayerCard.grid(row = 1,column = 1, sticky = (N, W, E, S))
# Create display for number of cards
aiNumCards = ttk.Label(frame2, text = "AI's # of cards: " + str(len(aideck)))
aiNumCards.grid(row = 2, column = 0, sticky = (N, W, E, S))
playerNumCards = ttk.Label(frame2)
playerNumCards.grid(row = 2, column = 1, sticky = (N, W, E, S))
# Create a button to flip over the cards
Play = ttk.Button(frame2, text = "Click the button to flip your card!", command = thirdScreen) 
Play.grid(row=3, column=1)
# Create empty text labels to be used later
display = ttk.Label(frame2)
display.grid(row = 3, column = 0, sticky = (N, W, E, S))
warCardDisplay = ttk.Label(frame2)
warCardDisplay.grid(row = 4, column = 0, sticky = (N, W, E, S))
# Int to be used later
war = [1]
wardeck = []
# Start with the cursor in our textbox
nameEntry.focus()
# Bind return to also bring us to the next screen
root.bind('<Return>', deleteScreen)
# Add extra padding to look better spaced
for child in frame2.winfo_children(): child.grid_configure(padx=5, pady=5)

root.mainloop()
