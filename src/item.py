class Item:
    def __init__(self, name, description, value, desired=False):
        self.name = name
        self.description = description
        self.value = value
        self.desired = desired

    def __str__(self):
        return self.name
