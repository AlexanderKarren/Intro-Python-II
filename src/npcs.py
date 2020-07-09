from npc import NPC
from items import item

dialogue = {
    "hr_jammy": {
        "greeting": "Oh, it's you. Hello, {player}.",
        "gift_phrase": "Oh? What's this?",
        "bad_gift": "If you think this gains you my favor, think again.",
        "good_gift": """Oh, goodness! How unexpected!
How did you know that I loved these?
It's not much, but here's 50 bumplecoins for your troubles.""",
        "dialogues": [
            "Mayor Jagweed has turned this part of town into a nightmare.",
            """Oh, mercy. One would think that the umpteenth time you took
out another mortgage on your house you would've memorized how to
get to the bank. And who asks for directions, anymore?
Ever heard of Bumple Maps?\n
To get to The Bank of Happystate, you'll need to head north from
Rupert's Rumpets until you hit a T-intersection in the road.
The road going west there is closed, but I've known people to
take a shortcut through The Sketchy Apartment Complex anyway,
if you think you can handle it.""",
            """Crazy Seymour is some unemployed parasite living behind
Rupert's Rumpets and Human Resources. I'd avoid going around
back if you don't want some hippie to talk your ear off for
an hour. One can't help but blame that awful mayor for the state
of this neighborhood! I do suppose he's harmless, though.
Still."""
        ],
        "player_options": [
            "* Ask about politics",
            "* Ask for directions to the bank",
            "* Ask about Crazy Seymour"
        ]
    }
}

npc = {
    "hr_jammy":
    NPC("Jammy", dialogue["hr_jammy"], item['laptop'], item['cigarettes'])
}

example_dialogue_friendly = {
    "greeting": "Hello, I am a friendly NPC.",
    "gift_phrase": "Oh? A present?",
    "bad_gift": "Oh. Hrm, thanks, I guess...",
    "good_gift": "A {item name}! I love these things!",
    "purchase_phrase": "What are ya' buyin'?",
    "sell_phrase": "What are ya' sellin'?",
    "dialogues": [
        "Go north to find the key.",
        "I can't tell you anything about that.",
        "Don't have a deal. Just a man who loves doughnuts."
    ],
    "player_options": [
        "Where can I find the key?",
        "How do I beat the game?",
        "What's your deal?"
    ],
    "item_dialogue": "I'll give you a key for that doughnut."
}
