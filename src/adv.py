from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance", "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

item = {
    'axe': Item('axe', '''A rusted axe. Someone must have forgotten it.''', 'an old axe'),
    'note': Item('note', '''It says "thank you" on it''', 'a crumpled note'),
    'hat': Item('hat', '''A gross hat. There's fungus growing in it.''', 'a discarded hat')
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

room['narrow'].add_item(item['axe'])
room['treasure'].add_item(item['note'])
room['outside'].add_item(item['hat'])

#
# Main
#

playing = True

# Make a new player object that is currently in the 'outside' room.

player = Player(room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
print('\nLocation: ' + player.current_room.name)
print(player.current_room.description)
while(playing is True):
    command = input('\nEnter a command: ')
    command = command.split(' ')
    if len(command) == 1:
        if command[0] == 'quit':
            print('Thanks for playing!')
            playing is False
            break
        elif command[0] == 'west':
            if player.current_room.w_to is not None:
                player.change_room(player.current_room.w_to)
            else:
                print('There is no path that way.')
        elif command[0] == 'south':
            if player.current_room.s_to is not None:
                player.change_room(player.current_room.s_to)
            else:
                print('There is no path that way.')
        elif command[0] == 'north':
            if player.current_room.n_to is not None:
                player.change_room(player.current_room.n_to)
            else:
                print('There is no path that way.')
        elif command[0] == 'east':
            if player.current_room.e_to is not None:
                player.change_room(player.current_room.e_to)
            else:
                print('There is no path that way.')
        elif command[0] == 'help':
            print('Here are some commands you can try: \nnorth, south, east, west \nsearch room \ninspect (item) \ntake (item) \ndrop (item) \nview inventory \n')
    if len(command) == 2:
        if command == ['search', 'room']:
            player.current_room.view_items()
        elif command[0] == 'inspect' and player.current_room.item_check(command[1]):
            player.current_room.item_check(command[1]).inspect()
        elif command[0] == 'inspect' and not player.current_room.item_check(command[1]):
            print("That's not here. You inspect yourself instead.")
        elif command[0] == 'take' and player.current_room.item_check(command[1]):
            player.take_item(player.current_room.item_check(command[1]))
            print('You took the ' + command[1])
        elif command[0] == 'take' and not player.current_room.item_check(command[1]):
            print('You took what?')
        elif command[0] == 'drop' and player.item_check(command[1]):
            player.drop_item(player.item_check(command[1]))
            print('You dropped the ' + command[1])
        elif command[0] == 'drop' and not player.item_check(command[1]):
            print("You don't have that to drop.")
        elif command[0] == 'view' and command[1] == 'inventory':
            if len(player.items) != 0:
                player.view_inventory()
            else:
                print('Your inventory is empty.')

    