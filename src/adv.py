from room import Room
from player import Player
from commands import command_parser

# Declare all the rooms

room = {
    'outside':  Room("Outside Restaurant", """You are outside Rupert's Rumpets,
your employer. There is a highway parallel to the restaurant running north
to south."""),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you,
falling into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from
west to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

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

# bumplesnop

player_name = input("What is your name? ")
print()

player = Player(player_name.title(), room['outside'])

print(f"""You are {player.name}, an orange bumplesnop.\n
You are a middle-class food service employee living in Detroit, Happystate.\n
Tonight was a cash night at work! You made the bulk of your tips in physical
bumplecoins.\n
Unfortunately for you, ever since the election of the corrupt Mayor Jagweed,
Detroit has become an unstable and crime-ridden place, and, having no
means to a vehicle, you must rely on your own two feet to get to the bank and
deposit your tips.\n
Your goal is to get to the bank in one piece and deposit at least 500 coins.
For commands, type 'help'.\n""")

while (True):
    print(f"{player.current_room}\n")
    command = input("What will you do? ")
    print()
    command_parser(command, player)
