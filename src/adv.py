from rooms import room
from player import Player
from commands import command_parser

player_name = input("What is your name? ")
print()

player = Player(player_name.title(), room['spawn'])

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
    if (player.current_room.chest):
        print(f"{player.current_room.chest.description}\n")
    command = input("What will you do? ")
    print()
    command_parser(command, player)
