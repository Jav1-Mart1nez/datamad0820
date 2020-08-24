
import random

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
    """def attack(self):
        return self.strength"""
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
    """def __init__ (self, health, strength):
        self.health = health
        self.strength = strength
    def attack (self):
        return self.strength"""
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
    def addViking(self, viking):
        self.viking = viking
        self.vikingArmy.append(self.viking)
    def addSaxon(self, saxon):
        self.saxon = saxon
        self.saxonArmy.append(self.saxon)
    def vikingAttack(self):
        viking_rand = random.choice(self.vikingArmy)
        saxon_rand = random.choice(self.saxonArmy)
        viking_attack = saxon_rand.receiveDamage(viking_rand.strength)
        if saxon_rand.health <= 0:
            self.saxonArmy.remove(saxon_rand)
        return viking_attack
    def saxonAttack(self):
        viking_rand = random.choice(self.vikingArmy)
        saxon_rand = random.choice(self.saxonArmy)
        saxon_attack = viking_rand.receiveDamage(saxon_rand.strength)
        if viking_rand.health <= 0:
            self.vikingArmy.remove(viking_rand)
        return saxon_attack
    def showStatus(self):
        if len(self.saxonArmy)==0:
            return ("Vikings have won the war of the century!")
        if len(self.vikingArmy)==0:
            return ("Saxons have fought for their lives and survive another day...")
        if len(self.saxonArmy)>=1 and len(self.vikingArmy)>=1:
            return ("Vikings and Saxons are still in the thick of battle.")
    
    pass
