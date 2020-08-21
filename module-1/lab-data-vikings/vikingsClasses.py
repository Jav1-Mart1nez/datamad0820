
# Soldier


class Soldier:
    def __init__ (self, health, strength):
        self.health = health
        self.strength = strength
    def attack(self):
        return self.strength
    def receiveDamage(self, damage):
        self.damage = damage
        self.health = self.health - self.damage
    pass

# Viking


class Viking (Soldier):
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength
    def attack(self):
        return self.strength
    def receiveDamage(self, damage):
        self.damage = damage
        self.health = self.health - self.damage
        if self.health <= 0:
            return (f"{self.name} has died in act of combat")
        else:
            return (f"{self.name} has received {self.damage} points of damage")
    def battleCry(self):
        return "Odin Owns You All!"
    pass

# Saxon


class Saxon (Soldier):
    def __init__ (self, health, strength):
        self.health = health
        self.strength = strength
    def attack (self):
        return self.strength
    def receiveDamage (self,damage):
        self.damage = damage
        self.health = self.health - self.damage
        if self.health <= 0:
            return ("A Saxon has died in combat")
        else:
            return (f"A Saxon has received {self.damage} points of damage")
    pass

# War


class War:
    def __init__ (self):
        self.vikingArmy = []
        self.saxonArmy = []
    def addViking(self, Viking):
        self.vikingArmy.append(Viking)
        
    pass
