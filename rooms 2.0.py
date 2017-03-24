###########################################################################################
# Names: Andre Aguillard, Samantha Santiago
# Date: 3/24/2017
# Description: Rooms 2.0, now with pictures!
###########################################################################################
from Tkinter import *

# the blueprint for a room
# room class
# NEED TO EDIT TO FULLY IMPLEMENT DICTIONARIES - SANTIAGO
class Room(object):
    # constructor
    def __init__(self, name):
        # rooms have a name, exits (e.g. south), exit locations (e.g. to the south is room n),
        # items (e.g. table), item descriptions (for each item), and grabbables (things that can
        # be taken into inventory)
        # NEED TO EDIT TO INCLUDE IMAGES
        # EDIT FOR DICTIONARIES
        # KEEP THE ADDITIONAL THINGIES
        self.name = name
        self.image = image # added images - Santiago
        self.exits = {}
        self.items = {}
        self.grabbables = []
        # these are all lists

    # getters and setters for the instance variables
    # these stay the same
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    # image getter   
    @property
    def image(self):
        returnself._image
    # image getter
    @image.setter
    def image(self, value):
        self._image = value

    # salidas
    @property
    def exits(self):
        return self._exits
    
    # exits
    @exits.setter
    def exits(self, value):
        self._exits = value

    # items!
    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        self._items = value

    # grab and go products
    @property
    def grabbables(self):
        return self._grabbables

    @grabbables.setter
    def grabbables(self, value):
        self._grabbables = value

    # add stuff as this proves to work - Santiago

    # glad that that's over. now to add things to build up the game
    
    # adds an exit to the room
    # this exit is a string
    # the room is an instance of the room
    def addExit(self, exit, room):
        # appends the exit and room to the appropriate dictionary - Santiago
        self._exits[exits] = room
        
    # adds an item to the room; item is a string
    # description is a string to describe the item
    def addItem(self, item, desc):
        # append the item and description to the appropriate lists
        self._items.[item] = desc

    # adds a grabbable item from the room
    # this is also a string
    def addGrabbable(self, item):
        # append to the list
        self._grabbables.append(item)
    # removes grabbable from the room
    def delGrabbable(self, item):
        # delete from the list
        self._grabbables.remove(item)
    def __str__(self):
        # room name
        s = "You are in {}.\n".format(self.name)
        
        #items in the room
        s += "You see: "
        for item in self.items.keys(): # modified for dictionary - Santiago
            s += item + "... "
        s += "\n"

        # exits from the room
        s += "Exits: "
        for exit in self.exits.keys(): # midofied for dictionary
            s += exit + "... "

        return s


###########################################################################################
# creates the rooms
# THIS FUNCTION NOW GOES IN THE GAME CLASS - SANTIAGO
class Game(Frame):
    # constructor - Santiago
    def __init__(self, parent):
        # calls constructor in superclass
        Frame.__init__(self, parent)
        
def createRooms():
    # r1-r4 are the four rooms in the alleged mansion
    # I may add more rooms as time goes on
    # currentRoom is the room we're currently in. It can be any of the four
    # this needs to be global since it's changed in the main part of the program
    global currentRoom

    r1 = Room("Room 1")
    r2 = Room("Room 2")
    r3 = Room("Room 3")
    r4 = Room("Room 4")


    # adds exits to room 1
    r1.addExit("east", r2) # to the east of room 1 is room 2
    r1.addExit("south", r3)
    r1.addExit("west", None) # this is the window that you broke to get in. -Santiago
    # add grabbables
    r1.addGrabbable("key")
    # edit so that when key is taken, another message for the table pops up.
    # add items
    r1.addItem("window", "The window is shattered, and there are shards of glass on the floor. This is how you got into the house.")
    r1.addItem("chair", "It's a chair. It's timeworn and ripped on one side, but looks comfy nonetheless.")
    r1.addItem("table", "It appears to be made of mahogany. A brass key lays on it, close to the left edge as though tossed there carelessly.")
    
    #add exits to room 2
    r2.addExit("west", r1)
    r2.addExit("south", r4)
    # add kickable
    r2.addItem("rug", "It looks like one of those Persian rugs your grandmother has. One of the edges has rolled up. You think you see something underneath.")
    # there will be a trapdoor under the rug. Add input so that rug can be removed
    r2.addItem("fireplace", "It's a stone fireplace, with nothing but ashes in it. There is currently no fire lit.")

    #add exit to room 3
    r3.addExit("north", r1)
    r3.addExit("east", r4)
    # add grabbables
    r3.addGrabbable("journal")
    r3.addGrabbable("flashlight")
    # add items
    r3.addItem("bookshelves", "One shelf has its books organized by series. Another shelf is filled with knick-knacks. The others are empty.")
    # may add knick-knacks to be picked up
    r3.addItem("statue", "You're unsure whether it's supposed to be a Greek bust, or if something knocked its head off.")
    r3.addItem("desk", "A faded red journal rests upon the mahogany surface.") # there should be a read option, so that you can gaze upon cryptic recipes for beer.
    # took readable and moved it down, so that you can't read the journal before picking it up - Santiago
    
    # adds exits to room 4
    r4.addExit("north", r2)
    r4.addExit("west", r3)
    r4.addExit("south", None) # that exit may be your doom
    r4.addExit("up", r8)
    # add grabbables
    r4.addGrabbable("6-pack")
    # add items
    r4.addItem("brew_rig", "You have no idea how to brew anything, but now you know whose house you've broken into. A 6-pack of some experimental batch is resting beside it. This is what you came for.")
    r4.addItem("painting", "The painting is of a gray-haired fellow, his head surrounded by a golden halo. The background is of a cloudy sky. You know very well that this is a depiction of Our Gourd and Savior.")
    r4.addItem("ladder", "It's a metal ladder, bolted to the left wall.")
    r4.addItem("window", "It's an open window on the far side of the room. You should really watch your step.")
    
    currentRoom = r1
 
# displays an appropriate "message" when the player dies
# yes, this is intentionally obfuscated!
def death():
    print " " * 17 + "u" * 7
    print " " * 13 + "u" * 2 + "$" * 11 + "u" * 2
    print " " * 10 + "u" * 2 + "$" * 17 + "u" * 2
    print " " * 9 + "u" + "$" * 21 + "u"
    print " " * 8 + "u" + "$" * 23 + "u"
    print " " * 7 + "u" + "$" * 25 + "u"
    print " " * 7 + "u" + "$" * 25 + "u"
    print " " * 7 + "u" + "$" * 6 + "\"" + " " * 3 + "\"" + "$" * 3 + "\"" + " " * 3 + "\"" + "$" * 6 + "u"
    print " " * 7 + "\"" + "$" * 4 + "\"" + " " * 6 + "u$u" + " " * 7 + "$" * 4 + "\""
    print " " * 8 + "$" * 3 + "u" + " " * 7 + "u$u" + " " * 7 + "u" + "$" * 3
    print " " * 8 + "$" * 3 + "u" + " " * 6 + "u" + "$" * 3 + "u" + " " * 6 + "u" + "$" * 3
    print " " * 9 + "\"" + "$" * 4 + "u" * 2 + "$" * 3 + " " * 3 + "$" * 3 + "u" * 2 + "$" * 4 + "\""
    print " " * 10 + "\"" + "$" * 7 + "\"" + " " * 3 + "\"" + "$" * 7 + "\""
    print " " * 12 + "u" + "$" * 7 + "u" + "$" * 7 + "u"
    print " " * 13 + "u$\"$\"$\"$\"$\"$\"$u"
    print " " * 2 + "u" * 3 + " " * 8 + "$" * 2 + "u$ $ $ $ $u" + "$" * 2 + " " * 7 + "u" * 3
    print " u" + "$" * 4 + " " * 8 + "$" * 5 + "u$u$u" + "$" * 3 + " " * 7 + "u" + "$" * 4
    print " " * 2 + "$" * 5 + "u" * 2 + " " * 6 + "\"" + "$" * 9 + "\"" + " " * 5 + "u" * 2 + "$" * 6
    print "u" + "$" * 11 + "u" * 2 + " " * 4 + "\"" * 5 + " " * 4 + "u" * 4 + "$" * 10
    print "$" * 4 + "\"" * 3 + "$" * 10 + "u" * 3 + " " * 3 + "u" * 2 + "$" * 9 + "\"" * 3 + "$" * 3 + "\""
    print " " + "\"" * 3 + " " * 6 + "\"" * 2 + "$" * 11 + "u" * 2 + " " + "\"" * 2 + "$" + "\"" * 3
    print " " * 11 + "u" * 4 + " \"\"" + "$" * 10 + "u" * 3
    print " " * 2 + "u" + "$" * 3 + "u" * 3 + "$" * 9 + "u" * 2 + " \"\"" + "$" * 11 + "u" * 3 + "$" * 3
    print " " * 2 + "$" * 10 + "\"" * 4 + " " * 11 + "\"\"" + "$" * 11 + "\""
    print " " * 3 + "\"" + "$" * 5 + "\"" + " " * 22 + "\"\"" + "$" * 4 + "\"\""
    print " " * 5 + "$" * 3 + "\"" + " " * 25 + "$" * 4 + "\""

###########################################################################################
# go!
inventory = [] # we don't have anything yet
createRooms() # create the rooms

#play forever or until player dies or quits
while(True):
    # set the status so player has situational awareness
    status = "{}\nYou are carrying : {}\n".format(currentRoom, inventory)

    # if current room is none, player is dead
    if (currentRoom == None):
        status = "You've met with a terrible fate, haven't you? "
    if (currentRoom == r11):
        status = "You've made it out of Dr. Gourd's house with the 6-pack of the experimental brew. The party shall go on."
        badwin() #displays some text that says you've won -Aguillard
        action = raw_input("Try again? (yes or no) ")
        if (action == "yes"):
            # starts you over
            inventory = []
            createRooms()
            status = "{}\nYou are carrying : {}\n".format(currentRoom, inventory)
            print "================================"
            print status
        elif (action == "no"):
            break
        else:
            break
    if(currentRoom == r15):
        status = "You've made it out of Dr. Gourd's house with the 6-pack of the experimental brew. The party shall go on."
        win()
        action = raw_input("Try again? (yes or no) ")
        if (action == "yes"):
            # starts you over
            inventory = []
            createRooms()
            status = "{}\nYou are carrying : {}\n".format(currentRoom, inventory)
            print "================================"
            print status
        elif (action == "no"):
            break
        else:
            break
        
    # this only happens if player goes south in room 4
    # edit: or, if you exit through the window in room 1. It quits the game.
    # display the status
    
    print "================================"
    print status
    print "Type 'help me' if needed"
    print " "
    # exit game
    # Santiago: I changed the code here so that if you die, you can just
    # start over with nothing, all the way back in room 1
    # by regenerating everything, I don't have to reset lists and stuff :p
    if (currentRoom == None):
        death() # calls the death function, cause if you quit you die, it's just one of those thing that happens -Aguillard
        action = raw_input("Try again? ")
        if (action == "yes"):
            # starts you over
            inventory = []
            createRooms()
            status = "{}\nYou are carrying : {}\n".format(currentRoom, inventory)
            print "Type 'Help me' to get help." # add a function to bring up key words and objective at any time - Santiago
            print "================================"
            print status
        elif (action == "no"):
            # quits the game; breaks
            break
        else:
            break

    #prompt for player input
    # the game supports a simple language of <verb>, <noun>
    # valid verbs are go, look, and take
    # Santiago: I should add use... cross that bridge when I get to it
    # man, I could add a lot of actions here...
    # valid nouns depend the verb
    # use raw_input here to treat the input as a string instead of an expression
    action = raw_input("What to do? ")

    # set the user's input to lowercase to make it easier to compare
    # the verb and noun to known values
    action = action.lower()

    # exit the game if the player wants to leave (supports quit, exit, and bye)
    if (action == "quit" or action == "bye" or action == "exit"):
        break
    # set default response
    response = "I'm afraid I don't understand. Try <verb, noun>. Valid verbs are go, look, take, kick, open, use, and read." # will add 'use' at some point # and 'read', for the book
    #split unser input into words
    words = action.split()
    # the game only understands two user inputs
    # if you see any response = " ", leave it. It's just to hold a place instead of printing the default response. - Santiago
    if (len(words) == 2):
        verb = words[0]
        noun = words[1]
        # verb is go
        if (verb == "go"):
            response = "Invalid exit."
            # check for valid exits
            # this works now
            for i in range(len(currentRoom.exits)):
                # a valid exit is found
                if (noun == currentRoom.exits[i]):
                    #change room to one associated with specific exit
                    currentRoom = currentRoom.exitLocations[i]
                    response = "You have entered another room." # changed speech a little bit
                    if(currentRoom == r11 or currentRoom == r15): # for the ends - Santiago
                        response = "You've made it out of Gourd's house."
                        print " "
                    break
        # verb is look
        # look works perfectly.
        elif (verb == "look"):
            response = "There's nothing like that here."
            for i in range(len(currentRoom.items)):
                if (noun == currentRoom.items[i]):
                    response = currentRoom.itemDescriptions[i]
                    break
        # verb is take
        # stuff gets taken, so this works
        elif (verb == "take"):
            response = "What am I even supposed to pick up?"
            for grabbable in currentRoom.grabbables:
                if (noun == grabbable):
                    inventory.append(grabbable)
                    currentRoom.delGrabbable(grabbable)
                    response = "{} is now in your inventory.".format(grabbable)
                    if (currentRoom == r1):
                        currentRoom.delItem("table", "It appears to be made of mahogany. A brass key lays on it, close to the left edge as though tossed there carelessly.")
                        currentRoom.addItem("table", "Nothing lays upon the mahogany surface.")
                    if (currentRoom == r3):
                        # readable added when book is grabbed. It can now be read anywhere, but not without getting the journal to begin with - Santiago
                        # modifies appearance of the desk and fireplace - Santiago
                        currentRoom.delItem("desk", "A faded red journal rests upon the mahogany surface.")
                        currentRoom.addItem("desk", "The desk is bare.")
                        r2.delItem("fireplace", "It's a stone fireplace, with nothing but ashes in it. There is currently no fire lit.")
                        r2.addItem("fireplace", "It's still a stone fireplace, but where there were only ashes, there is now a roaring fire.")
                    if (currentRoom == r4):
                        # modifies appearance of the bookshelves. An event has been triggered! - Santiago
                        r3.delItem("bookshelves", "One shelf has its books organized by series. Another shelf is filled with knick-knacks. The others are empty.")
                        r3.addItem("bookshelves", "One shelf has its books organized by series. Another shelf is filled with knick-knacks. However, one of the empty shelves now has a laptop on it.")
                        r4.delItem("brew_rig", "You have no idea how to brew anything, but now you know whose house you've broken into. A 6-pack of some experimental batch is resting beside it. This is what you came for.")
                        r4.addItem("brew_rig", "You still don't know how to brew beer, but you've already taken the fruits of its labors.")
                        response = "You hear a thud from the west of you, followed by footsteps. Finally, you hear another door slam shut. Somebody else is here as well. You wonder if they moved anything around."
                    break

    print "\n{}".format(response)

    # this street has really dangerous litter
            
        

