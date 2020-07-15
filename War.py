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

    def Value(self):
        return self.value


#function to get from the second screen after clicking the submit on the first screen
def secondScreen(*args):
    # Remove previous frame from screen
    frame1.destroy()
    # Create a label for ai's card
    AICardLabel = ttk.Label(frame2, text = "AI's Card: ").grid(row = 0, column = 0, sticky = (N, W, E, S))
    # Create a label for player's card
    PlayerCardLabel = ttk.Label(frame2, text = name.get() + "'s Card: ").grid(row = 0, column = 1, sticky = (N, W, E, S))
    # Rebind Enter to bring us to the third screen
    root.bind('<Return>', thirdScreen)
    for child in frame2.winfo_children(): child.grid_configure(padx=5, pady=5)

def thirdScreen(*args):
    # Create a label for the ai's card using the top of the ai player's deck
    AICard["image"] = aideck[0].photoImage()
    # Create a label for the player's card using the top of the player's deck
    PlayerCard["image"] = playerdeck[0].photoImage()
    # Create a button that says next card and will repeat this function
    Play["text"] = "Next card"
    # Move the card to the back of ai's deck
    aideck.append(aideck[0])
    aideck.pop(0)
    # Move the top card to the back of player's deck
    playerdeck.append(playerdeck[0])
    playerdeck.pop(0)
    # Add extra padding to look better spaced
    for child in frame2.winfo_children(): child.grid_configure(padx=5, pady=5)

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
Submit = Button(frame1, text = "Submit!", command = secondScreen) #command = command to go to the next screen?
Submit.grid(row=1, column=1, sticky = (N, W, E, S))
# Add extra spacing around each widget 
for child in frame1.winfo_children(): child.grid_configure(padx=5, pady=5)
#Create a photo image of the back of a card to be used later
CardBack = ImageTk.PhotoImage(Image.open("Card Back.jpg"))
# Create the image of the back of a card for ai's card
AICard = ttk.Label(frame2, image = CardBack)
AICard.grid(row = 1, column = 0, sticky = (N, W, E, S))
# Create the image of the back of a card for player's card
PlayerCard = ttk.Label(frame2, image = CardBack)
PlayerCard.grid(row = 1,column = 1, sticky = (N, W, E, S))
# Create a button to flip over the cards
Play = ttk.Button(frame2, text = "Click the button to flip your card!", command = thirdScreen) 
Play.grid(row=2, column=1)
# Start with the cursor in our textbox
nameEntry.focus()
# Bind return to also bring us to the next screen
root.bind('<Return>', secondScreen)
# Add extra padding to look better spaced
for child in frame2.winfo_children(): child.grid_configure(padx=5, pady=5)

root.mainloop()
