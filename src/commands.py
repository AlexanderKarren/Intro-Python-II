wall_message = "! There is nothing that way !\n"


def command_parser(command, player):
    if (command == "go north" or command == "n" or command == "walk north"):
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
    elif (command == "huh"):
        print("huh")
    elif (command == "exit" or command == "quit" or command == "q"):
        print("Thanks for playing!")
        exit()
    else:
        print(f"I don't know how to '{command}'\n")
