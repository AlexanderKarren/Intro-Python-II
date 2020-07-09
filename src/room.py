class Room:
    def __init__(self, name, description, npc=None, chest=None):
        self.name = name
        self.description = description
        self.npc = npc
        self.chest = chest

    def __str__(self):
        return self.description
