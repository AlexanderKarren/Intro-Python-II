from room import Room
from chests import chest

room = {
    # E5
    'spawn':  Room("Outside Restaurant", """You are outside Rupert's Rumpets,
your employer. There is a highway parallel to the restaurant running north
to south.
The building directly south of you is Rupert's Rumpets HR Department."""),
    # E6
    'hr':  Room("HR Department", """You are inside Rupert's Rumpets HR Dpt.\n
There is a purple yarrowsneezie in a pantsuit working the front desk.
She's a familiar face.""", None, chest["hr_garbage_can"]),
}


# Link rooms together

room['spawn'].s_to = room['hr']
room['hr'].n_to = room['spawn']
