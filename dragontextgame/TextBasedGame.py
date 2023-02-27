#  instructions for the game that will print at start
def instructions():
    print('Welcome to the Necromancer Village Text Adventure Game!')
    print('There are 6 items that you must get before you can defeat the Necromancer!')
    print('Type North, South, East, or West to move.')
    print('Type Exit to end the game at any time.')
    print('You are in the Town Entrance.')
    print('--------------')


def main():  # Define the rooms the game will take place in and the items in the room
    rooms = {
        'Town Entrance': {'South': 'Jeweler', 'East': 'Leatherworker', 'loot': 'None'},
        'Leatherworker': {'West': 'Town Entrance', 'East': 'Cooks House', 'loot': 'Bag of Holding'},
        'Cooks House': {'West': 'Leatherworker', 'South': 'Wizards House', 'loot': 'Steak Dinner'},
        'Jeweler': {'North': 'Town Entrance', 'East': 'Blacksmith', 'loot': 'Anti-fire Ring'},
        'Blacksmith': {'West': 'Jeweler', 'East': 'Tailor', 'loot': 'Sword'},
        'Tailor': {'West': 'Blacksmith', 'North': 'Wizards House', 'loot': 'Magic Robes'},
        'Wizards House': {'South': 'Tailor', 'North': 'Cooks House', 'West': 'Necromancers Lair', 'loot': 'Staff'},
        'Necromancers Lair': {'East': 'Wizards House', 'loot': 'None'}

    }

    # defining the movement function to move between rooms
    def move(direction, room='Town Entrance'):
        if direction in rooms[room]:  # if the direction entered is linked to the current room, print
            print('You move', direction, 'to the', (rooms[room][direction]))
            print('--------------')
            return rooms[room][direction]
        else:
            print('Invalid input')  # if direction entered is not linked to any rooms, does not move
            return playerLoc

    # inventory list that will be added to later as the player moves about the village
    inventory = []

    # function for item retrieval from the various rooms
    def getItem(room):
        item = rooms[room]['loot']  # identifying the variable that stores which item is in which room
        if item == 'None':  # if the dictionary entry for the item in that room is none, print
            print('There is no item here.')
        else:  # otherwise print what item is in the room, and allow the player a choice to pick it up or not
            print('There is a(n) {} in this room.'.format(item))
            userItem = input('Would you like to pick the item up? Type y/n. ')
            print('--------------')
            if userItem == 'y' or userItem == 'Y':
                print('You picked up {}'.format(item))
                inventory.append(item)
                print(inventory)  # prints the updated inventory list so the player knows how many items they have
                print('--------------')
                rooms[room]['loot'] = 'None'  # updates the dictionary entry for the room to have no item
            elif userItem == 'n' or userItem == 'N':  # if the player decides not to pick the item up
                print('You do not pick up the item.')
            else:
                print('Invalid input')
                getItem(playerLoc)
                return item

    stop = 'go'  # control
    instructions()  # prints the instructions one time at start of game
    playerLoc = 'Town Entrance'  # player starting location
    while stop != 'Exit':  # allows the player to exit any time they want
        userMove = input('Which direction would you like to go? ')
        if userMove == 'Exit':
            print('You moved to the Exit.')
            print('Thank you for playing!')
            break  # bulk of the code that calls the move function for player movement
        elif userMove == 'South':  # if userMove is South then the player location is updated to the new room
            playerLoc = move('South', playerLoc)
            getItem(playerLoc)
        elif userMove == 'East':  # if userMove is East then the player location is updated to the new room
            playerLoc = move('East', playerLoc)
            getItem(playerLoc)
        elif userMove == 'West':  # if userMove is West then the player location is updated to the new room
            playerLoc = move('West', playerLoc)
            getItem(playerLoc)
            if len(inventory) != 6 and playerLoc == 'Necromancers Lair':
                print('You were killed by the Necromancer!')
                userCont = input('Thank you for playing! Restart? y/n? ')
                if userCont == 'n':
                    break
                else:
                    print('Restarting...')
                    main()
            if len(inventory) == 6 and playerLoc == 'Necromancers Lair':
                print('You Win!')
                userCont = input('Thank you for playing! Restart? y/n? ')
                if userCont == 'n':
                    break
                else:
                    print('Restarting...')
                    main()
        elif userMove == 'North':  # if userMove is North then the player location is updated to the new room
            playerLoc = move('North', playerLoc)
            getItem(playerLoc)


main()
