import sys
import time
import os
import random
import math

def slowprint(s):
    for c in s + '\n\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./10)

def clear():
    os.system("cls")

def sleep(s):
    time.sleep(s)
    clear()

def speak(name, speech):
    print(name.title(), end = ": ")
    slowprint(speech)
    time.sleep(2)

class Cybermon:
    def __init__(self, name, type, moves, level, poison, burn, paralysis, confused, frozen, faint, EV):
        self.name = name
        self.type = type
        self.moves = moves
        self.level = level
        self.hp = level * 10
        self.poison = poison
        self.burn = burn
        self.paralysis = paralysis
        self.confused = confused
        self.frozen = frozen
        self.faint = faint

    def attackDamage(self):
        modifier = random.randint(1, 6) + 1
        atkDamage = math.ceil(((2 * self.level) + modifier)/5)
        return atkDamage

    def debuff(self):
        if self.poison == True:
            print(f"Your Cybermon has been Poisoned and Lost {self.hp/4} HP!")
            self.hp = self.hp - self.hp/4

        if self.burn == True:
            print(f"Your Cybermon has been Burnt and Lost {self.hp/10}")
            self.hp = self.hp - self.hp/10

        if self.paralysis == True:
            print("Your Cybermon has been Paralysed and Cannot Perform his next Move")
            self.paralysis = False

        if self.confused == True:
            print("Your Cybermon has been Confused and Cannot Perform his next Move")
            self.confused = False
        
        if self.frozen == True:
            print(f"Your Cybermon has been Froze and Lost {self.hp/10}")
            self.hp = self.hp - self.hp/10

        if self.faint == True:
            print("Your Cybermon has Fainted")

Dracon = Cybermon("Dracon", "Dragon Type/Fire Type", ["pyromaniac", "dragon rage", "draco meteor", "dragon ritual", "nuclear flame"], random.randint(35, 70), False, False, False, False, False, False, False)
Dinoton = Cybermon("Dinoton", "Dragon Type", ["flamethrower", "windstorm", "avian", "headbutt", "rock smash"], random.randint(15, 34), False, False, False, False, False, False, Dracon)
Salareon = Cybermon("Salareon", "Dragon Type", ["ember", "earthquake", "fire punch", "headbutt", "dragon claw"], random.randint(1, 14), False, False, False, False, False, False, Dinoton)

Crocodoth = Cybermon("Crocodoth", "Water Type", ["hydro beam", "water gun", "bite", "headbutt", "croc stance"], random.randint(35, 70), False, False, False, False, False, False, False)
Allichomp = Cybermon("Allichomp", "Water Type", ["chomp", "water gun", "haze", "bubble"], random.randint(1, 34), False, False, False, False, False, False, Crocodoth)

Gogoat = Cybermon("Gogoat", "Grass Type", ["forest's curse", "grass knot", "grassy terrain", "giga drain", "bullet seed"], random.randint(50, 70), False, False, False, False, False, False, False)
Ramraffe = Cybermon("Ramraffe", "Grass Type", ["photosynthesis", "grass knot", "razor leaf", "seed bomb", "bullet seed"], random.randint(1, 49), False, False, False, False, False, False, Gogoat)

Kynerine = Cybermon("Kynerine", "Dark Type/Ghost Type", ["bite", "armageddon", "death's howl", "invasion", "devil's glare"], random.randint(90, 95), False, False, False, False, False, False, False)
Coyolow = Cybermon("Coyolow", "Dark Type", ["bite", "dark shadow", "doom desire", "metal claw", "light of ruin"], random.randint(40, 45), False, False, False, False, False, False, Kynerine)
Kyena = Cybermon("Kyena", "Dark Type", ["crunch", "dark shadow", "doom desire", "bomb rush", "dream eater"], random.randint(1, 39), False, False, False, False, False, False, Coyolow)

Barracross = Cybermon("Barracross", "Water Type/Electric Type", ["water gun", "surf", "thunder fang", "electric terrain", "discharge"], random.randint(61, 80), False, False, False, False, False, False, False)
Voltacuda = Cybermon("Voltacuda", "Water Type/Electric Type", ["water gun", "hydro beam", "electro shock", "electric terrain", "voltage"], random.randint(30, 60), False, False, False, False, False, False, Barracross)
Wattope = Cybermon("Wattope", "Water Type/Electric Type", ["water gun", "bubble", "thunder bolt", "charge beam"], random.randint(1, 12), False, False, False, False, False, False, Voltacuda)

Komodozer = Cybermon("Komodozer", "Dark Type/Poison Type", ["shadow fang", "shadow claw", "toxic waste", "dark pulse", "torment"], random.randint(31, 60), False, False, False, False, False, False, False)
Komodoom = Cybermon("Komodoom", "Dark Type/Poison Type", ["shadow fang", "shadow claw", "toxic sludge", "sludge bomb", "toxic wate"], random.randint(1, 30), False, False, False, False, False, False, Komodozer)

Wolvash = Cybermon("Wolvash", "Dark Type/Electric Type", ["thunder bolt", "electro fang", "howl of the wild", "dark pulse", "fire punch"], random.randint(50, 80), False, False, False, False, False, False, False)
Wolvetric = Cybermon("Wolvetric", "Electric Type", ["thunder bolt", "electro fang", "howl of the wild", "bite"], random.randint(15, 45), False, False, False, False, False, False, Wolvash)

Empoguin = Cybermon("Empoguin", "Ice Type/Steel Type", ["technoblade", "sheer cold", "hydro beam", "arctic tundra", "moonblast"], random.randint(60, 80), False, False, False, False, False, False, False)
Hypeguin = Cybermon("Hypeguin", "Ice Type", ["ice punch", "sheer cold", "hydro beam", "wing attack", "arctic tundra"], random.randint(25, 50), False, False, False, False, False, False, False)
Boneguin = Cybermon("Boneguin", "Ice Type", ["ice punch", "tsunami", "water gun", "sheer cold", "frozen"], random.randint(1, 19), False, False, False, False, False, False, False)

Flamyte = Cybermon("Flamyte", "Fire Type/Ground Type", ["flamethrower", "fire punch", "scald", "pyromaniac", "earthquake"], random.randint(75, 90), False, False, False, False, False, False, False)
Charmetic = Cybermon("Charmetic", "Fire Type", ["tackle", "mud bomb", "flamethrower", "fire punch", "sclad"], random.randint(30, 60), False, False, False, False, False, False, Flamyte)
Chardvark = Cybermon("Chardvark", "Fire Type", ["scratch", "tackle", "mud bomb", "ember"], random.randint(1, 10), False, False, False, False, False, False, Charmetic)

Hippobite = Cybermon("Hippobite", "Water Type", ["water gun", "hydro beam", "scald", "bite", "ice punch"], random.randint(80, 90), False, False, False, False, False, False, False)
Hippodoom = Cybermon("Hippodoom", "Water Type", ["tackle", "water gun", "bubble", "scald", "hydro beam"], random.randint(30, 50), False, False, False, False, False, False, Hippobite)
Hipposaur = Cybermon("Hipposaur", "Water Type", ["scratch", "tackle", "water gun", "bubble"], random.randint(1, 10), False, False, False, False, False, False, Hippodoom)

Patank = Cybermon("Patank", "Grass Type/Rock Type", ["razor leaf", "bullet seed", "stun spore", "toxic mushroom", "photosynthesis"], random.randint(80, 90), False, False, False, False, False, False, False)
Ragent = Cybermon("Ragent", "Grass Type", ["tackle", "razor leaf", "bullet seed", "stun spore", "toxic mushroom"], random.randint(30, 50), False, False, False, False, False, False, Patank)
Parsnipe = Cybermon("Parsnipe", "Grass Type", ["tackle", "scratch", "razor leaf", "bullet seed"], random.randint(1, 10), False, False, False, False, False, False, Ragent)

Zebrawl = Cybermon("Zebrawl", "Normal Type", ["tackle", "headbutt", "crunch", "run over"], random.randint(1, 40), False, False, False, False, False, False, False)

Cybermons = {
    "Dracon": Dracon,
    "Dinoton": Dinoton,
    "Salareon": Salareon,

    "Crocodoth": Crocodoth,
    "Allichomp": Allichomp,

    "Gogoat": Gogoat,
    "Ramraffe": Ramraffe,

    "Kynerine": Kynerine,
    "Coyolow": Coyolow,
    "Kyena": Kyena,

    "Barracross": Barracross,
    "Volatcuda": Voltacuda,
    "Wattope": Wattope,

    "Komodozer": Komodozer,
    "Komodoom": Komodoom,

    "Wolvash": Wolvash,
    "Wolvetric": Wolvetric,

    "Empoguin": Empoguin,
    "Hypeguin": Hypeguin,
    "Boneguin": Boneguin,

    "Flamyte": Flamyte,
    "Charmetic": Charmetic,
    "Chardvark": Chardvark,

    "Hippobite": Hippobite,
    "Hippodoom": Hippodoom,
    "Hipposaur": Hipposaur,

    "Patank": Patank,
    "Ragent": Ragent,
    "Parsnipe": Parsnipe,

    "Zebrawl": Zebrawl,
}