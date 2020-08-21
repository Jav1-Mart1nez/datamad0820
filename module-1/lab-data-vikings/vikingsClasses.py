
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
    import random

    def __init__ (self):
        self.vikingArmy = []
        self.saxonArmy = []
    def addViking(self, viking):
        self.viking = viking
        self.vikingArmy.append(self.viking)
    def addSaxon(self, saxon):
        self.saxon = saxon
        self.saxonArmy.append(self.saxon)
    def vikingAttack(self):
        pass
    def receiveDamage (self):
        return (f"receiveDamage() of a Saxon with the {self.strength} of a Viking")
    def saxonAttack(self):
        self.viking
    def receiveDamage(self):
        return (f"receiveDamage() of a viking with the {self.strength} of a Saxon")
    def showStatus(self):
        while True:
            if len(self.saxonArmy)==0:
                return "Saxons have fought for their lives and survive another day..."
            if len(self.vikingArmy)==0:
                return "Vikings have won the war of the century!"
            if len(self.saxonArmy)==1 and len(self.vikingArmy)==0:
                return "Vikings and Saxons are still in the thick of battle."
            break
    
    pass
