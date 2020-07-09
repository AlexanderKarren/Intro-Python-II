class NPC:
    friendly = True

    def __init__(self, name, dialogue, item=None, fav_item=None):
        self.name = name
        self.dialogue = dialogue
        self.item = item
        self.fav_item = fav_item

    def receive_gift(self, player_gift):
        if player_gift == self.fav_item:
            return True
        return False
