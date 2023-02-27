# Define the rooms the game will take place in and the items in the rooms
rooms = {
    'Town Entrance': {'South': 'Jeweler', 'East': 'Leatherworker', 'item': 'None'},
    'Leatherworker': {'West': 'Town Entrance', 'East': 'Cooks House', 'item': 'Bag of Holding'},
    'Cooks House': {'West': 'Town Entrance', 'South': 'Wizards House', 'item': 'Steak Dinner'},
    'Jeweler': {'North': 'Town Entrance', 'East': 'Blacksmith', 'item': 'Anti-fire Ring'},
    'Blacksmith': {'West': 'Jeweler', 'East': 'Tailor', 'item': 'Sword'},
    'Tailor': {'West': 'Blacksmith', 'North': 'Wizards House', 'item': 'Magic Robes'},
    'Wizards House': {'South': 'Tailor', 'North': 'Cooks House', 'West': 'Necromancer', 'item': 'Staff'},
    'Necromancer': {'East': 'Wizards House', 'item': 'None'}

}


# add a list or dictionary for inventory and maybe define a function for getting items.
# if item in room: notify player
# delete an item from the dictionary of items once gotten from room
# if player has all items, trigger win condition on entrance of Necromancer room

# instructions for the game that will print at start
def instructions():
    print('Welcome to the Necromancer Village Text Adventure Game!')
    print('There are 6 items that you must get before you can defeat the Necromancer!')
    print('Type North, South, East, or West to move.')
    print('To add an item to your inventory type "get itemnamehere".')
    print('Type Exit to end the game at any time.')

# defining the movement function to move between rooms
def move(direction, room='Town Entrance'):
    if direction in rooms[room]:  # if the direction entered is linked to the current room, print
        print(rooms[room][direction])
        return rooms[room][direction]
    else:
        print('Invalid input')
        return playerLoc


def getItem(item, room='Town Entrance'):
    if rooms[room][item] != 'None':
        print(rooms[room][item])
        print('There is an item in the room.')
        item = input('Find the item? y/n? ')
        return item


inventory = []

stop = 'go'  # control
playerLoc = 'Town Entrance'  # player starting location
instructions()  # prints the instructions one time at start of game
while stop != 'Exit':  # allows the player to exit any time they want
    userMove = input('Which direction would you like to go? ')
    invItem = 'None'
    room = playerLoc
    if userMove == 'Exit':
        playerLoc = 'Exit'
        print('You moved to the {}.'.format(playerLoc))
        print('Thank you for playing!')
        break
    elif userMove == 'South':  # bulk of the code that calls the move function for player movement
        playerLoc = move('South', playerLoc)  # player location = the move function with parameter south and current loc
    elif userMove == 'East':  # if userMove is East then the player location is updated to the new room
        playerLoc = move('East', playerLoc)
    elif userMove == 'West':  # if userMove is West then the player location is updated to the new room
        playerLoc = move('West', playerLoc)
    elif userMove == 'North':  # if userMove is North then the player location is updated to the new room
        playerLoc = move('North', playerLoc)
    else:
        print('Invalid input')
    # if item in room and not in inventory:
invItem = 'None'
while 'item' != 'None':
    if playerLoc == 'Leatherworker':
        invItem = getItem('item', 'Leatherworker')