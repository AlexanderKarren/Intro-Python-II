from chest import Chest
from items import item

chest_items = {
    'hr_garbage_can_items': [
        item["cigarettes"]
    ]
}

chest = {
    'hr_garbage_can': Chest('Garbage Can', """There is a garbage can next to
the secretary's desk.""", chest_items['hr_garbage_can_items'])
}
