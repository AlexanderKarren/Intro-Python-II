class Player:
    balance = 500
    inventory = []

    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def go_to(self, new_room):
        self.current_room = new_room
