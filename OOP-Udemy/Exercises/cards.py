class Card:
    def __init__(self, name, emoji, element, attack, defense, evasion, speed):
        self.name = name
        self.emoji = emoji
        self.element = element
        self.attack = attack
        self.defense = defense
        self.evasion = evasion
        self.speed = speed


deck = []
dragon = Card('Dragon', '🐉', 'Fire🟧', 95, 75, 10, 40)
rabbit = Card('Rabbit', '🐰', 'Earth🟫', 35, 70, 95, 99)
cow = Card('Cow', '🐄', 'earth🟫', 78, 80, 10, 60 )
mouse = Card('Mouse', '🐭', 'earth🟫', 5, 90, 99, 90)



deck.append(dragon)
deck.append(rabbit)
deck.append(cow)
deck.append(mouse)