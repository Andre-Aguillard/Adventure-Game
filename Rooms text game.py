###########################################################################################
# Names: Andre Aguillard, Stelli Li, Samantha Santiago
# Date: 2/10/2017
# Description: Room adventure text game! Yay!
###########################################################################################

###########################################################################################
# the blueprint for a room
class Room(object):
    # constructor
    def __init__(self, name):
        # rooms have a name, exits (e.g. south), exit locations (e.g. to the south is room n),
        # items (e.g. table), item descriptions (for each item), and grabbables (things that can
        # be taken into inventory)
        self.name = name
        self.exits = []
        self.exitLocations = []
        self.items = []
        self.itemDescriptions = []
        self.grabbables = []
        self.kickables = [] #items that can be kicked - Santiago
        self.openables = [] # items that can be opened - Santiago
        self.usables = [] # items that can be used - Santiago
        self.readables = [] # items that can read - Santiago
        # these are all lists

    # getters and setters for the instance variables
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    # salidas
    @property
    def exits(self):
        return self._exits
    
    # exits
    @exits.setter
    def exits(self, value):
        self._exits = value

    # need  a way out?
    @property
    def exitLocations(self):
        return self._exitLocations

    @exitLocations.setter
    def exitLocations(self, value):
        self._exitLocations = value
        
    # items!
    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        self._items = value

    # describing things
    @property
    def itemDescriptions(self):
        return self._itemDescriptions

    @itemDescriptions.setter
    def itemDescriptions(self, value):
        self._itemDescriptions = value

    # grab and go products
    @property
    def grabbables(self):
        return self._grabbables

    @grabbables.setter
    def grabbables(self, value):
        self._grabbables = value

    @property # kickable rug - Santiago
    def kickables(self):
        return self._kickables
    
    @kickables.setter
    def kickables(self, value):
        self._kickables = value

    @property # makes the box able to be opened - Santiago
    def openables(self):
        return self._openables

    @openables.setter
    def openables(self, value):
        self._openables = value

    @property # things that can be used - Santiago
    def usables(self):
        return self._usables

    @usables.setter
    def usables(self, value):
        self._usables = value

    @property # in order to read the journal - Santiago
    def readables(self):
        return self._readables

    @readables.setter
    def readables(self, value):
        self._readables = value

    # glad that that's over. now to add things to build up the game
    
    # adds an exit to the room
    # this exit is a string
    # the room is an instance of the room
    def addExit(self, exit, room):
        # appends the exit and room to the appropriate lists
        self._exits.append(exit)
        self._exitLocations.append(room)
    def delExit(self, exit, room): # deletes certain exits - Santiago
        self._exits.remove(exit)
        self._exitLocations.remove(room)
        
    # adds an item to the room
    # item is a string
    # description is a string to describe the item
    def addItem(self, item, desc):
        # append the item and description to the appropriate lists
        self._items.append(item)
        self._itemDescriptions.append(desc)
    def delItem(self, item, desc): # be able to delete items and replace them - Santiago
        self._items.remove(item)
        self._itemDescriptions.remove(desc)

    # adds a grabbable item from the room
    # this is also a string
    def addGrabbable(self, item):
        # append to the list
        self._grabbables.append(item)
    # removes grabbable from the room
    def delGrabbable(self, item):
        # delete from the list
        self._grabbables.remove(item)

    # the one kickable item in the game
    def addKickable(self, item):
        #append to list
        self._kickables.append(item)
        # remove once kicked
    def delKickable(self, item):
        self._kickables.remove(item)

    # stuff that can be opened
    def addOpenable(self, item):
        # add the thing
        self._openables.append(item)
        # remove once opened
    def delOpenable(self, item):
        self._openables.remove(item)

    #stuff that can be used
    def addUsable(self, item):
        self._usables.append(item)
    def delUsable(self, item):
        self._usables.remove(item)

    #things that can be read
    def addReadable(self, item):
        self._readables.append(item)
    def delReadable(self, item):
        self._readables.remove(item)

    def __str__(self):
        # room name
        s = "You are in {}.\n".format(self.name)
        
        #items in the room
        s += "You see: "
        for item in self.items:
            s += item + "... "
        s += "\n"

        # exits from the room
        s += "Exits: "
        for exit in self.exits:
            s += exit + "... "

        return s


###########################################################################################
# creates the rooms
def createRooms():
    # r1-r4 are the four rooms in the alleged mansion
    # I may add more rooms as time goes on
    # currentRoom is the room we're currently in. It can be any of the four
    # this needs to be global since it's changed in the main part of the program
    global currentRoom
    global r1 # needed for the key
    global r2 # this is needed for the rug and trapdoor - Santiago
    global r3 # actually, they're all needed to be able to read the book and use certain things in other rooms. - Santiago
    global r4
    global r5
    global r6
    global r7
    global r8
    global r9
    global r10
    global r11
    global r12
    global r13
    global r14
    global r15
    r1 = Room("Room 1")
    r2 = Room("Room 2")
    r3 = Room("Room 3")
    r4 = Room("Room 4")
    r5 = Room("the basement") # r5-r7 are the basement
    r6 = Room("the basement")
    r7 = Room("the basement")
    r8 = Room("the attic") # r8 is the attic
    r9 = Room("the attic")
    r10 = Room("the attic")
    r11 = Room(" ")
    r12 = Room("tunnel")
    r13 = Room("tunnel")
    r14 = Room("tunnel")
    r15 = Room(" ")

    
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
    r2.addKickable("rug")
    # moved openable to fix bug - Santiago
    #add items
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
    # set room 1 as the room you start in at the beginning of the game

    # add exits to r5
    r5.addExit("up", r2)
    r5.addExit("east", r6)
    # add items
    r5.addItem("light", "It's a bare bulb on a string. It doesn't provide a lot to see by.")
    r5.addItem("cobweb", "It's a dusty web. You're hoping that there isn't a massive spider in it. Maybe it's just dust.")

    # add exits to r6
    r6.addExit("west", r5)
    r6.addExit("east", r7)
    # add items to r6
    r6.addItem("old_poster", "It's a faded poster of a beautiful woman; it seems familiar for some reason. It's stuck to the wall with glue. You think you can hear the wind blowing behind it. You could use something to tear it.")

    #add exits to r7
    r7.addExit("west", r6)
    # add the box
    r7.addItem("box", "It's a small, wooden box atop a pedestal. You're pretty sure it used to hold cigars. It is locked.")
    r7.addItem("overhead_lamp", "A large lamp hangs over the pedestal.")
    # it's also an openable
    r7.addOpenable("box")
    #add usable
    r7.addUsable("key")
    #add grabbable
    r7.addGrabbable("usb_drive")

    #add exits to r8
    r8.addExit("down", r4)
    r8.addExit("west", r9)
    r8.addExit("south", r10)
    #add item
    r8.addItem("flag", "It's a flag with a maple leaf. You wonder where the hockey sticks and poutine are at.")

    #add exits to r9
    r9.addExit("east", r8)
    # add other things
    r9.addItem("rock", "It's a small, round stone laying on the wooden floor. If you flip it over, you can see that someone painted a face on it. Either way, it's excellent for throwing at things, especially things that tear.")
    # add grabbable
    r9.addGrabbable("rock")

    #add exits to r10
    r10.addExit("north", r8)
    r10.addExit("south", None)
    #add other things
    r10.addItem("window", "It is an open window. If you go up to it and look down, you can see a ladder leaning up against the side of the house. It's a way out!")
    r10.addItem("hockey_stick", "It's a hockey stick, long and curved at the end. Considering you're in the South, and it's about 80 degrees Fahrenheit outside, you wonder why this is even here.")

    #r11 can win

    # r12 and beyond
    r12.addExit("south", r6)
    r12.addExit("north", r13)
    
    r13.addExit("south", r12)
    r13.addExit("north", r14)

    r14.addExit("south", r13)
    r14.addExit("north", r15)
    
    currentRoom = r1
    
def win():  ##Andre did this part, :) -Aguillard
    print "Yay! you won! Wow, what a great adventure..."
    print "...."
    print "Who knew Dr. Gourd owned a mansion, I wonder if I missed anything..."
def badwin(): # I couldn't help it. There had to be a bad ending, if only to encourage the player to use the Shawshank tunnel. - Santiago
    print "You may have the beer, but you didn't think to look down the ladder before descending. You're now being driven off in a cop car on a number of charges."
    print "...."
    print "Well, this sucks. Was there another way this could've gone?"
 
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
                        r1.addReadable("journal")
                        r2.addReadable("journal")
                        r3.addReadable("journal")
                        r4.addReadable("journal")
                        r5.addReadable("journal")
                        r6.addReadable("journal")
                        r7.addReadable("journal")
                        r8.addReadable("journal")
                        r9.addReadable("journal")
                        r10.addReadable("journal")
                        r12.addReadable("journal")
                        r13.addReadable("journal")
                        r14.addReadable("journal")
                        
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
                        r3.addReadable("laptop")
                        r3.addUsable("usb_drive")
                        response = "You hear a thud from the west of you, followed by footsteps. Finally, you hear another door slam shut. Somebody else is here as well."
                        r10.delExit("south", None)
                        r10.addExit("south", r11)
                        r14.addExit("north", r15)
                        r6.addExit("north", r12)
                    if (currentRoom == r9):
                        # add usable to the basement
                        r6.addUsable("rock")
                        r9.addReadable("rock")
                        currentRoom.delItem("rock", "It's a small, round stone laying on the wooden floor. If you flip it over, you can see that someone painted a face on it. Either way, it's excellent for throwing at things, especially things that tear.")
                    break
        # kick should be interesting # there's a bug where trapdoor remains an openable. needs to be fixed - Santiago
        elif (verb == "kick"):
            response = "Nothing happened. Violence isn't always the answer."
            for kickable in currentRoom.kickables:
                if (noun == kickable):
                    response = "You kick the rug away, or rather, you shuffle it out of the way with your feet. You've revealed a trapdoor!"
                    currentRoom.addItem("trapdoor", "It is a wooden door with a circular handle. The handle folds into the floor.") # able to add trapdoor to items list
                    print response
                    action = raw_input("Would you like to open the trapdoor? ")
                    if (action == "yes"):
                        response = "You have opened the trapdoor."
                        currentRoom.delItem("trapdoor", "It is a wooden door with a circular handle. The handle folds into the floor.")
                        currentRoom.addItem("trapdoor", "It is a wooden door with a circular handle. The door has been swung to the side, revealing a dark descent.")
                        currentRoom.addExit("down", r5)
                        print response
                    # i've allowed for one to come back and open the trapdoor, should they choose - Santiago
                    elif (action == "no"):
                        response = "You leave the trapdoor closed."
                        currentRoom.addOpenable("trapdoor")
                    else:
                        response = "I didn't get that."
                        print response
                        currentRoom.addOpenable("trapdoor")
                        action = raw_input("Would you like to open the trapdoor? ")
                        if (action == "yes"):
                            currentRoom.delOpenable("trapdoor")
                            response = "You have opened the trapdoor."
                            print response
                        elif (action == "no"):
                            response = "You leave the trapdoor closed."
                            print response # changed this to allow you to come back to the closed trapdoor at any time - Santiago
                            
                        # make something to come back and open the trapdoor, if desired
                # modifies rug appearance
                currentRoom.delKickable(kickable)
                currentRoom.delItem("rug", "It looks like one of those Persian rugs your grandmother has. One of the edges has rolled up. You think you see something underneath.") # be able to delete the rug from items list
                currentRoom.addItem("rug", "The ornate rug is in a crumpled heap, off to the side. There's not much to do to it anymore.") # adds back a new description for the future
                
        elif (verb == "open"): # allows for things to be opened. Apparently, for every new verb, you need lists and everything. Rock fact! - Santiago
            response = "There's nothing that can be opened."
            for openable in currentRoom.openables:
                if (noun == openable):
                    action = raw_input("Would you like to open this? (yes or no) ") # depending on what room you're in, different things happen. - Santiago
                    if (action == "yes" and currentRoom == r2):    
                        currentRoom.delItem("trapdoor", "It is a wooden door with a circular handle. The handle folds into the floor.")
                        currentRoom.addItem("trapdoor", "It is a wooden door with a circular handle. The door has been swung to the side, revealing a dark descent.")
                        response = "You have opened the trapdoor."
                        currentRoom.delOpenable("trapdoor")
                        currentRoom.addExit("down", r5)
                    elif (action == "yes" and currentRoom == r7):
                        response = "You can't open the box without unlocking it first."
                    elif (action == "no" and currentRoom == r7):
                        response = "The box is left in the same spot as before."
                    elif (action == "no" and currentRoom == r2):
                        response = "You leave the trapdoor closed."
                    else:
                        response = "I didn't get that."
                        print response
        elif (verb == "read"): # allows journal, rock, and laptop to be viewed - Santiago
            response = "There's nothing here to read, stupid."
            for readable in currentRoom.readables:
                if (readable == "journal" and currentRoom != r9 and currentRoom !=r3): # changed condition here so journal can be read everywhere AND not be mixed up with the laptop - Santiago
                    action = raw_input("Would you like to read this? ")
                    if (action == "yes"):
                        print "Entry 1: To whoever is reading this, you owe it to yourself to watch this video: 9 1-13 23-15-18-18-9-5-4 1-2-15-21-20 13-25 7-18-1-4-5."
                        print "\n{}"
                        action = raw_input("Would you like to keep reading? ")
                        if (action == "yes"):
                            print "Entry 13: Don't cry over spilled milk. It could have been beer."
                            print "\n{}"
                            action = raw_input("Would you like to keep reading? ")
                            if (action == "yes"):
                                print "Entry 24:...I just got lost in thought. It was unfamiliar territory."
                                print "\n{}"
                                action = raw_input("Keep reading? ")
                                if (action == "yes"):
                                    print "Entry 25: I have approximate answers and possible beliefs and different degrees of certainty about different things, but I'm not absolutely sure about anything. -- Richard Feynman"
                                    print "\n{}"
                                    action = raw_input("Maybe one more entry? ")
                                    if (action == "yes"):
                                        print "Entry 37: Wow. You're a real anarchist."
                                        print "\n{}"
                                        action = raw_input("Still gonna read private thoughts? ")
                                        if (action == "yes"):
                                            print "The Volunteer Fire Department could do nothing about the very flagrant deaths of the Baudelaire couple."
                                        
                    elif (action == "no"):
                        break
                    else: # acoounts for missspellings
                        print response
                        break
                elif (readable == "laptop" and currentRoom == r3): # laptop can only be read in room 3 - Santiago
                    print "The laptop has several windows open."
                    action = raw_input("Would you like to read a window? ")
                    if (action == "yes"):
                        print "Good Programming Practices...yeah, maybe later."
                        print "\n{}"
                        action = raw_input("Pull up another window? ")
                        if (action == "yes"):
                            print "Hobbies:...brewing beer, baking bread, building and flying my model rockets... the list goes on and on."
                            print "\n{}"
                            action = raw_input("Perhaps open one more window? ")
                            if (action == "yes"):
                                print "ourgourdandsavior.tumblr.com, a site dedicated to our real priorities."
                                print "\n{}"
                                action = raw_input("Keep going, then? ")
                                if (action == "yes"):
                                    print "It's a YouTube playlist of 80s music. You click out of it."
                                    print "\n{}"
                                    action = raw_input("Still gonna go through a guy's browser history? ")
                                    if (action == "yes"):  
                                        print "It's just task manager."
                                        print "\n{}"              
                    elif (action == "no"):
                        break
                    else: # acoounts for missspellings
                        print response
                        break
                elif (readable == "rock" and currentRoom == r9): # changed this so that you can only read the rock in that one room. Otherwise, you're crazy. - Santiago
                    print "Rock fact!"
                    action = raw_input("Want to hear a rock fact? ")
                    if (action == "yes"):
                        print "If you soak a raisin in grape juice, it turns into a grape."
                        print "\n{}"
                        action = raw_input("Want to hear another rock fact? ")
                        if (action == "yes"):
                            print "Dinosaurs had big ears, but everyone forgot about this because dinosaur ears don't have bones."
                            print "\n{}"
                            action = raw_input("Another? ")
                            if (action == "yes"):
                                print "Greg stole this rock from old lady Daniel's yard."
                                print "\n{}"
                    elif (action == "no"):
                        break
                        response = " "
        # allows certain items to be used to progress - Santiago
        # changed some aspects to allow used items to be deleted - Santiago
        elif (verb == "use"):
            response = "What am I supposed to use this on?"
            for usable in currentRoom.usables:
                if (noun == usable):
                    action = raw_input("Use this item? ")
                    if (action == "yes" and currentRoom == r7):
                        currentRoom.delItem("box", "It's a small, wooden box atop a pedestal. You're pretty sure it used to hold cigars. It is locked.")
                        currentRoom.addItem("box", "It's an unlocked cigar box.")
                        print "You have unlocked the little wooden box. Inside of it is a USB drive and a tiny picture of Dr. Box. Some of his photography is also included."
                        inventory.remove("key")
                        currentRoom.delOpenable("box")
                        response = " "
                    elif (action == "no" and currentRoom == r7):
                        print "You put it away. Perhaps you'll use it later."
                        response = " "
                    if (action == "yes" and currentRoom == r6):
                        currentRoom.delItem("old_poster", "It's a faded poster of a beautiful woman; it seems familiar for some reason. It's stuck to the wall with glue. You think you can hear the wind blowing behind it. You could use something to tear it.")
                        currentRoom.addItem("torn_poster", "It's an old poster, torn by the rock you threw. A draft is blowing the tatters. You can see a dark tunnel behind it.")
                        print "You threw the rock at the poster. It went through it, and took a bit to land."
                        inventory.remove("rock")
                        currentRoom.delUsable("rock")
                        r9.delReadable("rock")
                    elif (action == "no" and currentRoom == r6):
                        print "You put it away. Perhaps you'll use it later."
                        response = " "
                    if (action == "yes" and currentRoom == r3):
                        currentRoom.delUsable("usb_drive")
                        inventory.remove("usb_drive")
                        print "You put the USB drive in the laptop, and go to Files. There's only one thing on the drive."
                        action = raw_input("Would you like to open the file? ")
                        if (action == "yes"):
                            print "...this is why I recommend that you keep a brewing log from the very beginning of your homebrew 'hobby'...it appears to have been updated very recently..."
                        elif (action == "no"):
                            print "You put it away. Perhaps you'll use it later."
                            response = " "
        elif (verb == "help"): # tutorial/remidner system if a player gets lost in how to play this - Santiago
            if (noun == "me"):
                print "The object of the game is to fulfill an unconventional beer run--rather than go to Walgreen's, you've instead gained access to one of your professor's houses to get an excellent small-batch brew."
                print " "
                print "Type <verb><noun> to do things."
                print " "
                print "Valid verbs: go, look, take, kick, open, use, and read."
                print " "
                print "Valid nouns include things such as directions, objects in the room, and even certain items within descriptions."
                print " "
                print "If one action doesn't work on something, feel free to try others."
                print " "
                print "Some things are limited to certain rooms. Keep that in mind."
                print " "
                print "Remember to revisit places you've been. An action you've performed in one room can cause changes in others."
                response = " "
        # something to be able to use certain items
    print "\n{}".format(response)

    # this street has really dangerous litter
            
        

