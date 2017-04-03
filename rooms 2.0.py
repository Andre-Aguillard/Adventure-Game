###########################################################################################
# Names: Samantha Santiago, Andre Aguillard
# Date: 3/24/2017
# Description: Adventure is out there!
###########################################################################################
from Tkinter import *
import winsound

# the blueprint for a room
# room class
# be sure to correct spacing issues - Santiago
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
        self.images = [] # list for images
        self.exits = {} # dictionary for exits
        self.items = {} # dictionary for items
        self.usables = [] # list for usables, since they are exclusive to particular rooms - Santiago
        self.kickables = [] # definitely a list here - Santiago
        self.grabbables = [] # list for grabbables
        self.readables = [] # list for the journal - Santiago
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
    def images(self):
        return self._images        
    # image getter
    @images.setter
    def images(self, value):
        self._images = value
        
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
    # openables - Santiago
    @property
    def openables(self):
        return self._openables
    @openables.setter
    def openables(self, value):
        self._openables = value
    # usables
    @property
    def usables(self):
        return self._usables
    @usables.setter
    def usables(self, value):
        self._usables = value
    # readables - Santiago
    @property
    def readables(self):
        return self._readables
    @readables.setter
    def readables(self, value):
        self._readables = value

    # add stuff as this proves to work - Santiago
    # Adds images to a dictionary of possible images for a room.
    def addImage (self, image):
        self._images.append(image)
        
    # adds an exit to the room
    # this exit is a string
    # the room is an instance of the room
    def addExit(self, exit, room):
        # appends the exit and room to the appropriate dictionary - Santiago
        self._exits[exit] = room
    def delExit(self, exit, room):
        del self._exits[exit]      
    # adds an item to the room; item is a string
    # description is a string to describe the item
    def addItem(self, item, desc):
        # append the item and description to the appropriate dictionary
        self._items[item] = desc
    def delItem(self, item, desc):
        del self._items[item]
        
    # adds a grabbable item from the room
    # this is also a string
    def addGrabbable(self, item):
        # append to the list
        self._grabbables.append(item)
    # removes grabbable from the room
    def delGrabbable(self, item):
        # delete from the list
        self._grabbables.remove(item)   
    # kickables! - Santiago
    def addKickable(self, item):
        self._kickables.append(item)
    def delKickable(self, item):
        self._kickables.remove(item)
    # usables - Santiago
    def addUsable(self, item):
        self._usables.append(item)
    def delUsable(self, item):
        self._usables.remove(item)
    # readables - Santiago
    def addReadable(self, item):
        self._readables.append(item)
    def delReadable(self, item):
        self._readables.remove(item)
        
    # forget the openables, dude. Better to keep this to just the usables -  the key, the usb, and the drive. You use them, it's one and done.
    # I don't feel like opening additional dialogues - Santiago

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
        global r1
        global r2
        global r3
        global r4
        global r5
        global r6
        global r7
        global r8
        global r10
        global r11
        global r12
        global r13
        global r14
        global r15
        # add gifs later - Santiago
        # adding all the rooms - Santiago
        r1 = Room("Room 1")
        r2 = Room("Room 2")
        r3 = Room("Room 3")
        r4 = Room("Room 4")
        r5 = Room("the basement")
        r6 = Room("the basement")
        r7 = Room("the basement")
        r8 = Room("the attic") ### This room needs to be more defined, I just added it to fix somethign below - Aguillard
        r10 = Room("the attic")
        r11 = Room(" ")
        r12 = Room("a tunnel")
        r13 = Room("a tunnel")
        r14 = Room("a tunnel")
        r15 = Room(" ")
        ########################
        # Note: only add the initial images for each room in the createRooms function.
        #       add/ delete other images later on in the code. 
        ########################
        
        #adds initial image to room 1
        r1.addImage("room1.gif") 
        # adds exits to room 1
        r1.addExit("east", r2) # to the east of room 1 is room 2
        r1.addExit("south", r3)
        r1.addExit("west", None) # this is the window that you broke to get in. -Santiago
        # add grabbables
        r1.addGrabbable("key")
        # edit so that when key is taken, another message for the table pops up.
        # add items
        r1.addItem("window", "The window is shattered, and there are shards of glass on the floor. This is how you got into the house.")
        r1.addItem("chair", "It's a chair. It's timeworn and ripped on one\nside, but looks comfy nonetheless.")
        r1.addItem("table", "It appears to be made of mahogany. A brass key\nlays on it, close to the left edge as though\ntossed there carelessly.") 

        #Initial image for room 2
        r2.addImage("r2OG.gif")
        #add exits to room 2    ###I'm gonna format the lines like the ones above^^^ so they don't cut words in half in the window - Aguillard
        r2.addExit("west", r1)
        r2.addExit("south", r4)
        #added kickable - Santiago
        r2.addKickable("rug") #added the kickable - Santiago
        r2.addItem("rug", "It looks like one of those Persian rugs your\ngrandmother has. One of the edges has rolled up.\nYou think you see something underneath.")
        # there will be a trapdoor under the rug. Add input so that rug can be removed
        r2.addItem("fireplace", "It's a stone fireplace, with nothing but ashes in it. There is currently no fire lit.")

        #Initial image for room 3
        r3.addImage("r3OC.gif")
        #add exits to room 3
        r3.addExit("north", r1)
        r3.addExit("east", r4)
        # add grabbables
        r3.addGrabbable("journal")
        # add items
        r3.addItem("bookshelves", "One shelf has its books organized by series.\nAnother shelf is filled with knick-knacks. The others are empty.")
        # may add knick-knacks to be picked up
        r3.addItem("mannequin", "You're unsure whether it came like that, or if somebody knocked the limbs off.")
        r3.addItem("desk", "A faded red journal rests upon the surface.") # there should be a read option, so that you can gaze upon cryptic recipes for beer.

        #Initial image for room 4
        r4.addImage("room4.gif")        
        # adds exits to room 4
        r4.addExit("north", r2)
        r4.addExit("west", r3)
        r4.addExit("south", None) # that exit may be your doom
        r4.addExit("up", r8)    ### I added a room 8 above but there's nothing to it yet. -Aguillard
        # add grabbables
        r4.addGrabbable("6-pack")
        # add items
        r4.addItem("brew_rig", "You have no idea how to brew anything, but now\nyou know whose house you've broken into. A 6-pack of some experimental batch is resting beside it. This is what you came for.")
        r4.addItem("painting", "The painting is of a gray-haired fellow, his head surrounded by a golden halo. The background is of a cloudy sky. You know very well that this is a depiction of Our Gourd and Savior.")
        r4.addItem("ladder", "It's a metal ladder, bolted to the left wall.")
        r4.addItem("window", "It's an open window on the far side of the room. You should really watch your step.")

        #Initial image for room 5
        r5.addImage("r5.gif")
        # now adding the other rooms - Santiago
        r5.addExit("up", r2)
        r5.addExit("east", r6)
        # added items - Santiago
        r5.addItem("light", "It's a bare bulb on a string.\nIt doesn't provide a lot to see by.")
        r5.addItem("cobweb", "It's a dusty web.\nYou're hoping that there isn't a massive spider in it.")\

        #Initial image for room 6
        r6.addImage("r6NC.gif")
        # adding exits to r6 - Santiago
        r6.addExit("west", r5)
        r6.addExit("east", r7)
        # added item - Santiago
        r6.addItem("old_poster", "It's an old poster of Dominique Wilkins. It's stuck to the wall with glue. You think you can hear the wind blowing behind it. You could use something to tear it.")      

        #Initial image for room 7
        r7.addImage("room7NC.gif")
        # adding to r7 - Santiago
        r7.addExit("west", r6)
        # items to r7 - Santiago
        r7.addItem("box", "It's a small, wooden box atop a pedestal.\nYou're pretty sure it used to hold cigars.\nIt is locked.")
        r7.addItem("overhead_lamp", "A large lamp hangs over the pedestal.")

        #Initial image for room 8
        r8.addImage("attic.gif")
        # r8 now - Santiago
        r8.addExit("down", r4)
        r8.addExit("south", r10)
        # item
        r8.addItem("flag", "It's a flag with a maple leaf. You wonder where the hockey sticks and poutine are at.")
        r8.addItem("rock", "It's a small, round stone laying on the wooden\nfloor. If you flip it over, you can see that someone\npainted a face on it. Either way, it's excellent for throwing at things, especially things that tear.")
        r8.addGrabbable("rock")

        #Initial image for room 10 -Aguillard
        r10.addImage("attic.gif")
        # last part of the attic - Santiago
        r10.addExit("north", r8)
        r10.addExit("south", None)
        # items
        r10.addItem("window", "It is an open window. If you go up to it and look down, you can see a ladder leaning up against the side of the house. It's a way out!")
        r10.addItem("hockey_stick", "It's a hockey stick, long and curved at the end. Considering you're in the South, and it's about\n80 degrees Fahrenheit outside, you wonder why this is even here.")

        #Initial image for room 11
        r11.addImage("skull.gif")
        
        #Initial image for room 12 -Aguillard
        r12.addImage("tunnel.gif")
        #tunnel - Santiago
        r12.addExit("south", r6)
        r12.addExit("north", r13)

        #Initial image for room 13 -Aguillard
        r13.addImage("tunnel.gif")
        #tunnel
        r13.addExit("south", r12)
        r13.addExit("north", r14)

        #Initial image for room 14 -Aguillard
        r14.addImage("tunnel.gif")
        #adds exit to room 14 -Aguillard
        r14.addExit("south", r13)

        #Initial image for room 15
        r15.addImage("ge.gif")
        
        Game.currentRoom = r1 # changed this and inventory - Santiago
        Game.inventory = [] # inventory is now here - Santiago
        
    def setupGUI(self): # - Santiago
        #organize the GUI
        # this function works fine, as long as you have the images as actual GIFs
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
        Game.image = Label(self, width=WIDTH / 2, height=HEIGHT, image = img)
        Game.image.image = img
        Game.image.pack(side=LEFT, fill=Y)
        Game.image.pack_propagate(False)
        
        # setup text to right of GUI
        # first, place frame where the text will be displayed
        text_frame = Frame(self, width=WIDTH / 2, height=HEIGHT)
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
            Game.img = PhotoImage(file=Game.currentRoom.images[0])
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
            Game.text.insert(END, "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nYou've met with a terrible fate, haven't you?\n\nType yes to try again, or close out of the\nwindow to quit.\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        # bad ending, good ending - Santiago
        if (Game.currentRoom == r11):
            Game.text.insert(END, "\n\n\n\n\n\n\n\n\n\n\nYou may have the beer, but you didn't think to\nlook down the ladder before descending.\n\nYou're now being driven off in a cop car on a\nnumber of charges.\n\nNeedless to say, this sucks.\n\nIt could've gone better, don't you think?\n\n(type yes to start over, or close out the window to quit)\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        if (Game.currentRoom == r15):
            Game.text.insert(END, "\n\n\n\n\n\n\n\n\n\n\nYou've made it out of Dr. Gourd's house with the 6-pack of the experimental brew.\n\nThe party shall go\non.\n\nCongratulations.\n\nHope you didn't miss anything cool on the way out.\n\n(type yes to start over, or close out the window to quit)\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
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
        response = "I don't understand. Try the format <verb> <noun>. Valid verbs are go, look, take, kick, use, and read.\nType help me for more assistance. To quit, close out of the window." ### I added a help response -Aguillard
                      
        # exit the game if player wants to leave
        # supports quit, exit, and bye, felicia
        # got rid of these. If I can exit with the x button, what's the point? - Santiago

        # if player is dead if they went south from room 4 or west from room 1 # or if they try to go 'weast'
        if (Game.currentRoom == None or Game.currentRoom == r11 or Game.currentRoom == r15):
            Game.player_input.delete(0, END) # I figured out the try again screen! :D
            if (action == "yes"):
                self.createRooms()
            elif (action == "no"):
                exit(0)
            
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
                    winsound.PlaySound("door.wav", winsound.SND_ASYNC)
                    Game.currentRoom =\
                        Game.currentRoom.exits[noun]
                    # response of success
                    response = "You have entered another room."
                    if (Game.currentRoom == None):
                        response = " "             
                    if (Game.currentRoom == r11 or Game.currentRoom == r15):
                        response = "You've made it out of Gourd's house."
            # note to self - add more verb. - Santiago
            # verb is: look
            elif (verb == "look"):
                # set default response
                response = "There's nothing like that here."
                # check for valid items
                if (noun in Game.currentRoom.items):
                    # if one found, set response to item's description
                    response = Game.currentRoom.items[noun]
                    if ("6-pack" in Game.inventory):
                        winsound.PlaySound("footstep.wav", winsound.SND_ASYNC | winsound.SND_LOOP)
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
                        # code to change stuff, affect status of the room
                        if (Game.currentRoom == r1):
                            Game.currentRoom.delItem("table", "It appears to be made of mahogany. A brass key\nlays on it, close to the left edge as though\ntossed there carelessly.")
                            Game.currentRoom.addItem("table", "Nothing lays upon the mahogany surface.")                         
                            r7.addUsable("key")
                        if (Game.currentRoom == r3):
                            Game.currentRoom.delItem("desk", "A faded red journal rests upon the surface.")
                            Game.currentRoom.addItem("desk", "The desk is bare.")
                            if ("6-pack" in Game.inventory):
                                del r3._images[0]
                                r3.addImage("r3lap.gif")## this changes the image to show the laptop if you've already taken the journal
                            else:
                                del r3._images[0]
                                r3.addImage("r3take.gif")## this just shows the journal if you haven't taken the 6-pack 
                            r1.addReadable("journal")
                            r2.addReadable("journal")
                            r3.addReadable("journal")
                            r4.addReadable("journal")
                            r8.addReadable("journal")
                            r10.addReadable("journal")
                            r6.addUsable("journal")
                        if (Game.currentRoom == r4):
                            winsound.PlaySound("footstep.wav", winsound.SND_NOSTOP)
                            winsound.PlaySound("door.wav", winsound.SND_ASYNC)
                            r3.delItem("bookshelves", "One shelf has its books organized by series.\nAnother shelf is filled with knick-knacks. The others are empty.")
                            r3.addItem("bookshelves", "One shelf has its books organized by series.\nAnother shelf is filled with knick-knacks. One of the empty shelves has a laptop on it.")
                            r3.addItem("laptop", "A powered-off laptop sits on the shelf. The battery's been ripped out.")
                            r2.delItem("fireplace", "It's a stone fireplace, with nothing but ashes in it. There is currently no fire lit.")
                            r2.addItem("fireplace", "It's still a stone fireplace, but where there\nwere only ashes, there is now a roaring fire.")
                            if ("rug" in r2.kickables):
                                del r2._images[0]
                                r2.addImage("r2fire.gif")## this changes the image to show the fire in the fireplace after you've taken the 6-pack
                            else:
                                del r2._images[0]
                                r2.addImage("r2rugfire.gif")## this just shows the rug pushed back and the fire lit if you've already kicked the rug     
                            # laptop is gonna be an item now. The USB drive allows it to be used, if only once - Santiago
                            Game.currentRoom.delItem("brew_rig", "You have no idea how to brew anything, but now\nyou know whose house you've broken into. A 6-pack of some experimental batch is resting beside it. This is what you came for.")
                            Game.currentRoom.addItem("brew_rig", "You still don't know how to brew beer, but you've already taken the fruits of its labors.")
                            r10.delExit("south", None)
                            r10.addExit("south", r11)
                            r14.addExit("north", r15)
                            if ("journal" in Game.inventory):
                                del r3._images[0]
                                r3.addImage("r3lap.gif")#If I've taken the journal already, then room 3 only has the laptop
                            else :
                                del r3._images[0]
                                r3.addImage("r3lapj.gif")#if I haven't taken the journal yet, then the laptop and journal are still in room 3
                            response = "You hear a thud from the west of you, followed by footsteps. Finally, you hear another door slam\nshut. Somebody else is here as well."
                        if (Game.currentRoom == r7):
                            Game.currentRoom.addItem("picture", "It's a picture of Dr. Box. You feel like others would understand it more than you do.")
                            Game.currentRoom.addGrabbable("picture")
                        if (Game.currentRoom == r8):
                            Game.currentRoom.delItem("rock", "It's a small, round stone laying on the wooden\nfloor. If you flip it over, you can see that someone\npainted a face on it. Either way, it's excellent for throwing at things, especially things that tear.")
                            r6.addUsable("rock")
                        break
            elif (verb == "kick"): # added kicking back! - Santiago
                # default response
                response = "Violence isn't always the answer, so quit trying to kick everything."
                # check for valid kickables
                for kickable in Game.currentRoom.kickables:
                    if (noun == kickable):
                        # response here
                        response = "You've kicked the rug away, or rather,\nyou've shuffled it out of the way.\nYou've discovered a trapdoor!"
                        Game.currentRoom.addItem("trapdoor", "It is a wooden door with a circular handle.\nIt's opened, revealing a way down.")
                        Game.currentRoom.delKickable(kickable)
                        Game.currentRoom.delItem("rug", "It looks like one of those Persian rugs your grandmother has. One of the edges has rolled up. You think you see something underneath.") # be able to delete the rug from items list
                        Game.currentRoom.addItem("rug", "The ornate rug is in a crumpled heap, off to the side. There's not much to do to it anymore.")
                        Game.currentRoom.addExit("down", r5)
                        if ("6-pack" in Game.inventory):
                            del r2._images[0]
                            r2.addImage("r2rugfire.gif")#If I've taken the journal already, then room 3 only has the laptop
                        else :
                            del r2._images[0]
                            r2.addImage("r2rugNF.gif")                         
            elif (verb == "use"):
                response = "You can't use this here."
                for usable in Game.currentRoom.usables:
                    if (noun == usable):
                        response = "You've used the {}".format(usable)
                        Game.currentRoom.delUsable(usable)
                        Game.inventory.remove(usable)
                        if (Game.currentRoom == r7):
                            response = "You have unlocked the wooden box. Inside of it is a tiny picture of Dr. Box, and some of his\nphotography."
                            Game.currentRoom.delItem("box", "It's a small, wooden box atop a pedestal.\nYou're pretty sure it used to hold cigars.\nIt is locked.")
                            Game.currentRoom.addItem("box", "It's an unlocked cigar box.")
                            del r7._images[0]
                            r7.addImage("room7open.gif") # This should change the box to open
                            
                            Game.currentRoom.addItem("picture", "It's a picture of Dr. Box. You feel like others would understand it more than you do.")
                            Game.currentRoom.addGrabbable("picture")
                        if (Game.currentRoom == r6):
                            Game.currentRoom.delItem("old_poster",  "It's an old poster of Dominique Wilkins. It's stuck to the wall with glue. You think you can hear the wind blowing behind it. You could use something to tear it.")
                            Game.currentRoom.addItem("torn_poster", "It's an old poster, torn by the {} you threw. A draft is blowing the tatters. You can see a dark tunnel behind it.".format(usable))  
                            del r6._images[0]
                            r6.addImage("r6tear.gif")
                            Game.currentRoom.addExit("north", r12)
                            if (usable == "journal"):
                                r1.delReadable("journal")
                                r2.delReadable("journal")
                                r3.delReadable("journal")
                                r4.delReadable("journal")
                                r8.delReadable("journal")
                                r10.delReadable("journal")
                            response = "You threw the {} at the poster. It went through. You hear it land somewhere beyond the wallspae with a thud.".format(usable)
            elif (verb == "read"):
                pass #eh, I'll do this later - Santiago
                response = "You can't read anything here."
                for readable in Game.currentRoom.readables:
                            response = "Entry 1: To whoever is reading this, you owe it\nto yourself to watch this video: 9 1-13 23-15-18-\n18-9-5-4 1-2-15-21-20 13-25 7-18-1-4-5.\n{}\n"\
                                        "Entry 13: Don't cry over spilled milk. It could\nhave been beer.\n{}\n"\
                                        "Entry 24:...I just got lost in thought. It was\nunfamiliar territory.\n{}\n"\
                                        "Entry 25: I have approximate answers and possible beliefs and different degrees of certainty about different things, "\
                                        "but I'm not absolutely sure\nabout anything. -- Richard Feynman\n{}\n"\
                                        "The Volunteer Fire Department could do nothing\nabout the very flagrant deaths of the Baudelaire\ncouple."
                        # did it. - Santiago

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
            
