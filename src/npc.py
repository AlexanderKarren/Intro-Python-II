class NPC:
    def __init__(self, name, description, dialogue, item):
        self.name = name
        self.description = description
        self.dialogue = dialogue


example_dialogue_friendly = {
    "greeting": "Hello, I am a friendly NPC.",
    "gift_phrase": "Oh? A present?",
    "bad_gift": "Oh. Hrm, thanks, I guess...",
    "good_gift": "A {item name}! I love these things!"
    "purchase_phrase": "What are ya' buyin'?",
    "sell_phrase": "What are ya' sellin'?",
    "dialogues": [
        "Go north to find the key.",
        "I can't tell you anything about that.",
        "Don't have a deal. Just a man who loves doughnuts."
    ]
    "player_options": [
        "Where can I find the key?",
        "How do I beat the game?",
        "What's your deal?"
    ]
    "item_dialogue": "I'll give you a key for that doughnut."
}
