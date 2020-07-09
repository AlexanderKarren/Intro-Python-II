class Chest:
    def __init__(self, name, description, items):
        self.name = name
        self.description = description.replace("\n", " ")
        self.items = items
