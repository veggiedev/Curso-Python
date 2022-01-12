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
rabbit = Card('Rabbit', '🐰', 'Earth🟫', 35, 70, 95, 95)
cow = Card('Cow', '🐄', 'Earth🟫', 78, 80, 10, 60 )
mouse = Card('Mouse', '🐭', 'Earth🟫', 5, 90, 99, 90)
dog = Card('Dog', '🐕', 'Earth🟫', 60, 60, 70, 60)
snake = Card('Snake', '🐍', 'Earth🟫', 99, 30, 85, 90)
lion = Card('Lion', '🦁', 'Earth🟫', 85, 90, 75, 75)
whale = Card('Whale', '🐋', 'Water🟦', 100, 90, 0, 1)
turttle = Card('Turttle', '🐢', 'Water🟦', 5, 95, 5, 0)
hawk = Card('Hawk', '🦅', 'Air🏳️', 5, 90, 99, 90)
phoenix = Card('Phoenix', '🔥🐦', 'Fire🟧', 5, 90, 99, 90)
crocodile = Card('Crocodile', '🐊', 'Water🟦', 5, 90, 99, 90)
wolf = Card('Wolf', '🐺', 'Earth🟫', 5, 90, 99, 90)
pig = Card('Pig', '🐖', 'Earth🟫', 5, 90, 99, 90)
cat = Card('Cat', '😺', 'Earth🟫', 5, 90, 99, 90)
catfish = Card('Catfish', '😺🐠', 'Water🟦')



deck.append(dragon)
deck.append(rabbit)
deck.append(cow)
deck.append(mouse)