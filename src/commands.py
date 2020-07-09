wall_message = "You can't go that way!\n"


def display_inventory(player):
    index = 1
    print(f"{player.name}'s Bag:")
    for item in player.inventory:
        print(f"{index}: {item.name}")
        index += 1
    print(f"\nWallet: {player.balance} bumplecoins\n")
    command = input("# to select item, 'q' to back out: ")
    print()


def display_chest_items(chest, inventory):
    looting = True
    index = 1
    print(f"{chest.name}:")
    for item in chest.items:
        print(f"{index}: {item.name}")
        index += 1
    print()
    while (looting):
        command = input("# to take item, 'a' to take all, 'q' to back out: ")
        print()
        if (command == "a"):
            inventory.extend(chest.items)
            chest.items.clear()
            print(f"You took everything inside the {chest.name.lower()}.\n")
        elif (command == "q"):
            looting = False
        elif (command.isnumeric()):
            if (int(command) >= 1 and int(command) < index):
                print(f"You take the {chest.items[int(command) - 1].name}.\n")
                inventory.append(chest.items.pop(int(command) - 1))
                looting = False
            else:
                print(f"That number does not appear in the list.\n")


def command_parser(command, player):
    if (command == "bag" or command == "inventory"):
        if (len(player.inventory) <= 0):
            print("Your bag is empty!\n")
        else:
            display_inventory(player)
    elif (command == "go north" or command == "n" or command == "walk north"):
        if hasattr(player.current_room, "n_to"):
            player.go_to(player.current_room.n_to)
        else:
            print(wall_message)
    elif (command == "go east" or command == "e" or command == "walk east"):
        if hasattr(player.current_room, "e_to"):
            player.go_to(player.current_room.e_to)
        else:
            print(wall_message)
    elif (command == "go south" or command == "s" or command == "walk south"):
        if hasattr(player.current_room, "s_to"):
            player.go_to(player.current_room.s_to)
        else:
            print(wall_message)
    elif (command == "go west" or command == "w" or command == "walk west"):
        if hasattr(player.current_room, "w_to"):
            player.go_to(player.current_room.w_to)
        else:
            print(wall_message)
    elif (command == "loot"):
        if player.current_room.chest:
            chest = player.current_room.chest
            if (len(chest.items) <= 0):
                print(f"You check the {chest.name.lower()}, but it's empty!\n")
            else:
                display_chest_items(chest, player.inventory)
        else:
            print("There is nothing here to loot!\n")
    elif (command == "talk"):
        if player.current_room.npc:
            print("DEV: Engage in dialogue tree")
        else:
            print("There is nobody here to talk to!\n")
    elif (command == "exit" or command == "quit" or command == "q"):
        print("Thanks for playing!")
        exit()
    else:
        print(f"I don't know how to '{command}'\n")
