class Player:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        def take_damage(self, amount):
            self.health -= amount
            if self.health < 0:
                self.health = 0
                def attack(self, target, damage):
                    target.take_damage(damage)
                    print(f"{self.name} attacked {target.name} for {damage} damage!")

                c1 = Player("Player1", 100)
                c2 = Player("Player2", 100)
                c1.attack(c2, 20)
                print(f"{c2.name}'s health: {c2.health}")