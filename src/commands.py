wall_message = "You can't go that way!\n"


def display_inventory(player, in_conversation=False):
    inventory_open = True
    print(f"{player.name}'s Bag:")
    while inventory_open:
        index = 1
        for item in player.inventory:
            print(f"{index}: {item.name}")
            index += 1
        if in_conversation:
            print(f"\nWallet: {player.balance} bumplecoins\n")
        else:
            print()
        command = input("# to select item, 'q' to back out: ")
        print()
        if command.isnumeric():
            if (int(command) >= 1 and int(command) < index):
                return int(command) - 1
        else:
            inventory_open = False


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


def converse_friendly(npc, player):
    talking = True
    greeting = npc.dialogue['greeting'].replace("{player}", player.name)
    print(f'{npc.name}: "{greeting}"\n')
    while(talking):
        index = 1
        print(f"Talk to {npc.name}:")
        for option in npc.dialogue['player_options']:
            print(f"{index}: {option}")
            index += 1
        print(f"{index}: * Give {npc.name} an item\n")
        command = input("# to talk, 'q' to back out: ")
        print()
        if (command.isnumeric()):
            if (int(command) >= 1 and int(command) < index):
                print(f"{npc.dialogue['dialogues'][int(command) - 1]}\n")
            elif (int(command) == index):
                if len(player.inventory) <= 0:
                    print(f"You don't have anything to give to {npc.name}!\n")
                else:
                    print(f'"{npc.dialogue["gift_phrase"]}"\n')
                    selected_item = display_inventory(player, True)
                    if npc.receive_gift(player.inventory[selected_item]):
                        print(f"{npc.dialogue['good_gift']}\n")
                        player.inventory.append(npc.item)
                    else:
                        print(f"{npc.dialogue['bad_gift']}\n")
            else:
                print(f"That number does not appear in the list.\n")
        else:
            talking = False


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
            converse_friendly(player.current_room.npc, player)
        else:
            print("There is nobody here to talk to!\n")
    elif (command == "exit" or command == "quit" or command == "q"):
        print("Thanks for playing!")
        exit()
    else:
        print(f"I don't know how to '{command}'\n")
