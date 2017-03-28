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
    def __init__(self, name, image):
        # rooms have a name, exits (e.g. south), exit locations (e.g. to the south is room n),
        # items (e.g. table), item descriptions (for each item), and grabbables (things that can
        # be taken into inventory)
        # NEED TO EDIT TO INCLUDE IMAGES
        # EDIT FOR DICTIONARIES
        # KEEP THE ADDITIONAL THINGIES
        self.name = name
        self.image = image # added images - Santiago
        self.exits = {} # dictionary for exits
        self.items = {} # dictionary for items
        #self.usables = {} # dictionary for usables, since they are exclusive to particular rooms - Santiago
        self.kickables = [] # definitely a list here - Santiago
        #self.openable = {} # again, only for the box down that hallway - Santiago
        self.grabbables = [] # list for grabbables
        # not sure if these would still be lists or if they could be dictionaries...

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
        return self._image
        
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
    
    # kickables! - Santiago
    @property
    def kickables(self):
        return self._kickables
    
    @kickables.setter
    def kickables(self, value):
        self._kickables = value
        

    # add stuff as this proves to work - Santiago

    # glad that that's over. now to add things to build up the game
    
    # adds an exit to the room
    # this exit is a string
    # the room is an instance of the room
    def addExit(self, exit, room):
        # appends the exit and room to the appropriate dictionary - Santiago
        self._exits[exit] = room
        
    # adds an item to the room; item is a string
    # description is a string to describe the item
    def addItem(self, item, desc):
        # append the item and description to the appropriate dictionary
        self._items[item] = desc

    # adds a grabbable item from the room
    # this is also a string
    def addGrabbable(self, item):
        # append to the list
        self._grabbables.append(item)
    # removes grabbable from the room
    def delGrabbable(self, item):
        # delete from the list
        self._grabbables.remove(item)
    # adds usable once certain items are picked up or certain rooms are entered
    
    # kickables! - Santiago
    def addKickable(self, item):
        self._kickables.append(item)
    def delKickable(self, item):
        self._kickables.remove(item)

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
        for exit in self.exits.keys(): # modified for dictionary
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
        
    def createRooms(self):
        # r1-r4 are the four rooms in the alleged mansion
        # I may add more rooms as time goes on
        # currentRoom is the room we're currently in. It can be any of the four
        # this needs to be global since it's changed in the main part of the program
        global currentRoom
        # add gifs later - Santiago
        # adding all the rooms - Santiago
        r1 = Room("Room 1", "room1.gif")
        r2 = Room("Room 2", "room2.gif")
        r3 = Room("Room 3", "room3.gif")
        r4 = Room("Room 4", "room4.gif")
        r5 = Room("the basement", "basement1.gif")
        r6 = Room("the basement", "poster.gif")
        r7 = Room("the basement", "basement1.gif")
        r8 = Room("the attic","attic1.gif") ### This room needs to be more defined, I just added it to fix somethign below - Aguillard
        r9 = Room("the attic", "attic1.gif")
        r10 = Room("the attic", "attic1.gif")
        r11 = Room(" ", "badend.gif")
        r12 = Room("a tunnel", "tunnel.gif")
        r13 = Room("a tunnel", "tunnel.gif")
        r14 = Room("a tunnel", "tunnel.gif")
        r15 = Room(" ", "goodend.gif")
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
        r1.addItem("table", "It appears to be made of mahogany. A brass key\nlays on it, close to the left edge as though\ntossed there carelessly.") 
        #add exits to room 2    ###I'm gonna format the lines like the ones above^^^ so they don't cut words in half in the window - Aguillard
        r2.addExit("west", r1)
        r2.addExit("south", r4)
        r2.addKickable("rug") #added the kickable - Santiago
        r2.addItem("rug", "It looks like one of those Persian rugs your\ngrandmother has. One of the edges has rolled up.\nYou think you see something underneath.")
        # there will be a trapdoor under the rug. Add input so that rug can be removed
        r2.addItem("fireplace", "It's a stone fireplace, with nothing but ashes in it. There is currently no fire lit.")
        #add exits to room 3
        r3.addExit("north", r1)
        r3.addExit("east", r4)
        # add grabbables
        r3.addGrabbable("journal")
        r3.addGrabbable("flashlight")
        # add items
        r3.addItem("bookshelves", "One shelf has its books organized by series. Another shelf is filled\nwith knick-knacks. The others are empty.")
        # may add knick-knacks to be picked up
        r3.addItem("statue", "You're unsure whether it's supposed to be a Greek bust, or if something knocked its head off.")
        r3.addItem("desk", "A faded red journal rests upon the mahogany surface.") # there should be a read option, so that you can gaze upon cryptic recipes for beer.
        # took readable and moved it down, so that you can't read the journal before picking it up - Santiago
        # adds exits to room 4
        r4.addExit("north", r2)
        r4.addExit("west", r3)
        r4.addExit("south", None) # that exit may be your doom
        r4.addExit("up", r8)    ### I added a room 8 above but there's nothing to it yet. -Aguillard
        # add grabbables
        r4.addGrabbable("6-pack")
        # add items
        r4.addItem("brew_rig", "You have no idea how to brew anything, but now\nyou know whose house you've broken into. A 6-pack of some\nexperimental batch is resting beside it. This is what you came for.")
        r4.addItem("painting", "The painting is of a gray-haired fellow, his head surrounded\nby a golden halo. The background is of a cloudy sky. You know very wellthat this is a\ndepiction of Our Gourd and Savior.")
        r4.addItem("ladder", "It's a metal ladder, bolted to the left wall.")
        r4.addItem("window", "It's an open window on the far side of the room. You should really watch your step.")
        # now adding the other rooms - Santiago
        r5.addExit("up", r2)
        r5.addExit("east", r6)
        r5.addItem("light", "It's a bare bulb on a string.\nIt doesn't provide a lot to see by.")
        r5.addItem("cobweb", "It's a dusty web.\nYou're hoping that there isn't a massive spider in it.")\
        
        r6.addExit("west", r5)
        r6.addExit("east", r7)
        r6.addItem("old_poster", "It's a faded poster of a beautiful woman; it seems familiar for some reason.\nIt's stuck to the wall with glue. You think you can hear the wind\nblowing behind it. You could use something to tear it.")
        
        r7.addExit("west", r6)
        r7.addItem("box", "It's a small, wooden box atop a pedestal.\nYou're pretty sure it used to hold cigars.\nIt is locked.")
        r7.addItem("overhead_lamp", "A large lamp hangs over the pedestal.")
        
        r8.addExit("down", r4)
        r8.addExit("west", r9)
        r8.addExit("south", r10)
        
        r9.addExit("east", r8)
        r9.addItem("rock", "It's a small, round stone laying on the wooden floor. If you flip it over,\nyou can see that someone painted a face on it. Either way, it's excellent for throwing\nat things, especially things that tear.")
        
        r10.addExit("north", r8)
        r10.addExit("south", None)
        r10.addItem("window", "It is an open window. If you go up to it and look down, you can see\n a ladder leaning up against the side of the house. It's a way out!")
        r10.addItem("hockey_stick", "It's a hockey stick, long and curved at the end. Considering you're\nin the South, and it's about 80 degrees Fahrenheit outside,\nyou wonder why this is even here.")
        
        r12.addExit("south", r6)
        r12.addExit("north", r13)
    
        r13.addExit("south", r12)
        r13.addExit("north", r14)

        r14.addExit("south", r13)
        
        Game.currentRoom = r1 # changed this and inventory - Santiago
        Game.inventory = [] # inventory is now here - Santiago
        
    def setupGUI(self): # - Santiago
        #organize the GUI
        self.pack(fill=BOTH, expand=1)
        #setup the player input at the bottom of the GUI
        #widget is a Tkinter Entry
        #background is white; bind return key to function process in class
        Game.player_input = Entry(self, bg="white")
        Game.player_input.bind("<Return>", self.process)
        Game.player_input.pack(side=BOTTOM, fill=X)
        Game.player_input.focus()
        
        # setup image to the left of GUI
        # widget is a Tkinter label
        # don't let image control width's size
        img = None
        Game.image = Label(self, width=WIDTH / 2, image = img)
        Game.image.image = img
        Game.image.pack(side=LEFT, fill=Y)
        Game.image.pack_propagate(False)
        
        # setup text to right of GUI
        # first, place frame where the text will be displayed
        text_frame = Frame(self, width=WIDTH / 2)
        # widget - same deal as above
        # disable by default
        # don't let it control frame's size # is there any way to put the text in the middle? Having it to the left
        Game.text = Text(text_frame, bg="lightgrey", state=DISABLED)
        Game.text.pack(fill=Y, expand=1)
        text_frame.pack(side=RIGHT, fill=Y)
        text_frame.pack_propagate(False)
        
    def setRoomImage(self): # - Santiago
        if (Game.currentRoom == None):
            # if dead, SKULL
            Game.img = PhotoImage(file="skull.gif")
        else:
            Game.img = PhotoImage(file=Game.currentRoom.image)
        # display image to left
        Game.image.config(image=Game.img)
        Game.image.image = Game.img
    
    #sets the status displayed on right of GUI
    def setStatus(self, status):
        # enable text widget, clear it, set it, disable it
        Game.text.config(state=NORMAL)
        Game.text.delete("1.0", END)
        if (Game.currentRoom == None):
            # if dead, let player know
            Game.text.insert(END, "You've met with a terrible fate, haven't you? \n")
            # i'd love to add the try again function back in - Santiago      
        else:
            # display appropriate status
            Game.text.insert(END, str(Game.currentRoom) +\
                             "\nYou are carrying: " + str(Game.inventory) +\
                             "\n\n" + status)
            Game.text.config(state=DISABLED)
    # plays the game - Santiago
    def play(self):
        # add rooms to the game
        self.createRooms()
        # configure GUI
        self.setupGUI()
        #set current room
        self.setRoomImage()
        # set the current status
        self.setStatus("")
           
    # processes the player's input
    def process(self, event): # - Santiago
        # grab player's input from bottom of GUI
        action = Game.player_input.get()
        # set user's input to lowercase to make it easier
        # to compare verb and noun to known values
        action = action.lower()
        # default response
        response = "I don't understand. Try the format <verb> <noun>. Valid verbs are go, look, take, and kick.\nType help me for more assistance." ### I added a help response -Aguillard
                      
        # exit the game if player wants to leave
        # supports quit, exit, and bye, felicia
        if (action == "quit" or action == "exit" or action == "bye"):
            exit(0)
        
        # if player is dead if they went south from room 4 or west from room 1
        if (Game.currentRoom == None):
            # clear input
            Game.player_input.delete(0, END)
            return
        
        # split user input into words and store words in a list
        words = action.split()
        
        # game only understands two-word inputs
        if (len(words) == 2):
            verb = words[0]
            noun = words[1]
            
            # verb is: go
            if (verb == "go"):
                response = "Invalid exit."
                # check for valid exits
                if (noun in Game.currentRoom.exits):
                    #change room to one associated with specific exit
                    Game.currentRoom =\
                        Game.currentRoom.exits[noun]
                    # response of success
                    response = "You have entered another room."
            # note to self - add more verb. - Santiago
            # verb is: look
            elif (verb == "look"):
                # set default response
                response = "There's nothing like that here."
                # check for valid items
                if (noun in Game.currentRoom.items):
                    # if one found, set response to item's description
                    response = Game.currentRoom.items[noun]
            # verb is: take
            elif (verb == "take"):
                # default response
                response = "What am I even supposed to pick up?"
                # check for valid grabbales in the current room
                for grabbable in Game.currentRoom.grabbables:
                    if (noun == grabbable):
                        # add to player's inventory
                        Game.inventory.append(grabbable)
                        # remove grabbable from the room
                        Game.currentRoom.delGrabbable(grabbable)
                        # set succesful response
                        response = "{} is now in your inventory.".format(grabbable)
                        # put code here to delete item descriptions in room and replace them
                        # once the item is taken
                        # also, code to add to other lists and stuff - Santiago
                        break
            elif (verb == "kick"): # added kicking back! - Santiago
                # default response
                response = "Violence isn't always the answer, so quit trying to kick everything."
                # check for valid kickables
                for kickable in Game.currentRoom.kickables:
                    if (noun == kickable):
                        # response here
                        response = "You've kicked the rug away, or rather,\nyou've shuffled it out of the way.\nYou've discovered a trapdoor!"
                        Game.currentRoom.addItem("trapdoor", "It is a wooden door with a circular handle.\nThe handle folds into the floor.")
            #### Help me function provides more assitance to the user -Aguillard
            ### Also \n formats the text in tkinter to a new line, I went through and made sure the text all fit 
                ### within the lines of the window.
            elif (verb == "help"):
                if (noun == "me"):
                    response = "The object of the game is to fulfill an \n" \
                                "unconventional beer run--rather than go to \n" \
                                "Walgreen's, you've instead gained access to one \n" \
                                "of your professor's houses to get an excellent \n" \
                                "small-batch brew. \n" \
                                "Type <verb><noun> to do things. \n" \
                                "Correct spelling is a must. \n" \
                                "Valid verbs include: look, go, and take. \n"\
                                "Valid nouns include things such as directions, \n" \
                                "objects in the room, and even certain \n" \
                                "items within descriptions. \n" \
                                "If one action doesn't work on something, \ntry a different one. \n" \
                                "Some things/actions are limited to certain rooms. Keep that in mind. \n" \
                                "Remember to revisit places you've been. An action you've performed in one" \
                                "room can cause changes in others. \n" \
                                "Good luck and have fun!"
        # display response to right of GUI
        # display room's image on the left
        # clear player's input
        self.setStatus(response)
        self.setRoomImage()
        Game.player_input.delete(0, END)
###########################################################################################
# the default size of the GUI is 800x600
WIDTH = 800
HEIGHT = 600

# create the window
window = Tk()
window.title("Room Adventure")

# create the GUI as a Tkinter canvas inside the window
g = Game(window)
# play the game
g.play()

# wait for the window to close
window.mainloop()
##########################################################################################
# go!
# this street has really dangerous litter
            
        

