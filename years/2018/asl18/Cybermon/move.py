from cyberdex import *
from cybermon import *
from colorama import Fore, Back, Style
import sys

party = []

class Player:
    def __init__(self, money, cyberballs, location, badges):
        self.money = money
        self.cyberballs = cyberballs
        self.location = location
        self.badges = badges

    def updateMoney(self, newMoney):
        self.money = self.money + int(newMoney)

    def updateCyberballs(self, newCyberballs):
        self.cyberballs = self.cyberballs + int(newCyberballs)

    def updateLocation(self, newLocation):
        self.location = newLocation

    def updateBadges(self, newBadge):
        self.badges.append(newBadge)

Player1 = Player(0, 0, "Pallet Town", 0)

class Battle(Cybermon):
    def __init__(self, enemyJob, enemyName, enemyCybermon1, enemyCybermon2, enemyCybermon3, enemyCybermon4, enemyCybermon5, enemyCybermon6):
        self.enemyJob = enemyJob
        self.enemyName = enemyName
        self.i = 0
        self.enemyCybermon1 = enemyCybermon1
        self.enemyCybermon2 = enemyCybermon2
        self.enemyCybermon3 = enemyCybermon3
        self.enemyCybermon4 = enemyCybermon4
        self.enemyCybermon5 = enemyCybermon5
        self.enemyCybermon6 = enemyCybermon6

    def battle(self):

        enemyParty = {
            "enemyCybermon1": self.enemyCybermon1,
            "enemyCybermon2": self.enemyCybermon2,
            "enemyCybermon3": self.enemyCybermon3,
            "enemyCybermon4": self.enemyCybermon4,
            "enemyCybermon5": self.enemyCybermon5,
            "enemyCybermon6": self.enemyCybermon6
        }

        print(f"{self.enemyJob} {self.enemyName} has Challenged You to a Battle!")
        speak(f"{self.enemyJob} {self.enemyName}", "You're Going Down!")
        sleep(2)

        x = "enemyCybermon"
        y = 1

        while Cybermons[party[self.i]].hp > 0 and Cybermons[enemyParty[x + str(y)]].hp > 0:
            sleep(2)
            print(f"{self.enemyJob} {self.enemyName}'s {enemyParty[x + str(y)]} has {Cybermons[enemyParty[x + str(y)]].hp} HP left\n\n")
            print(f"Your {party[self.i]} has {Cybermons[party[self.i]].hp} HP left")
            print(f"Here are Your {party[self.i]}'s Moves: ", end="")
            print(', '.join(Cybermons[party[self.i]].moves).title())
            moveUsed = input("\nWhich Move do you want to do: ")
            if moveUsed not in Cybermons[party[self.i]].moves:
                print("\nInvalid Move")
            else:
                print(f"\nYour {party[self.i]} has done {Cybermons[party[self.i]].attackDamage()} Damage!")
                print(f"\n{self.enemyJob} {self.enemyName}'s {enemyParty[x + str(y)]} has done {Cybermons[enemyParty[x + str(y)]].attackDamage()} HP Damage\n")
                Cybermons[party[self.i]].hp = Cybermons[party[self.i]].hp - Cybermons[enemyParty[x + str(y)]].attackDamage()
                Cybermons[enemyParty[x + str(y)]].hp = Cybermons[enemyParty[x + str(y)]].hp - Cybermons[party[self.i]].attackDamage()

            if Cybermons[enemyParty[x + str(y)]].hp <= 0:
                print(f"\nYou have Beaten {self.enemyJob} {self.enemyName}'s {enemyParty[x + str(y)]}!")
                if enemyParty[x + str(y + 1)] != None:
                    y = y + 1

                else:
                    print(f"\nYou have defeated {self.enemyJob} {self.enemyName}!")
                    speak(f"{self.enemyJob} {self.enemyName}", "No Fair! You Must have Cheated!")
                    money = random.randint(100, 500)
                    print(f"You have gotten ${money}!")
                    Player1.updateMoney(money)

            if Cybermons[party[self.i]].hp <= 0:
                print(f"\nYour {party[self.i]} has been defeated by {self.enemyJob} {self.enemyName}'s {enemyParty[x + str(y)]}!")
                if len(party) > self.i + 1:
                    self.i = self.i + 1
                else:
                    print(f"\nYou have been defeated by {self.enemyJob} {self.enemyName}!")
                    speak(f"{self.enemyJob} {self.enemyName}", "HAHAHAHAHA I told you I was superior!")

def showPokedex(s):
    for c in s + '\n\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./500)

print("""\n                                             ██████╗██╗   ██╗██████╗ ███████╗██████╗ ███╗   ███╗ ██████╗ ███╗   ██╗
                                            ██╔════╝╚██╗ ██╔╝██╔══██╗██╔════╝██╔══██╗████╗ ████║██╔═══██╗████╗  ██║
                                            ██║      ╚████╔╝ ██████╔╝█████╗  ██████╔╝██╔████╔██║██║   ██║██╔██╗ ██║
                                            ██║       ╚██╔╝  ██╔══██╗██╔══╝  ██╔══██╗██║╚██╔╝██║██║   ██║██║╚██╗██║
                                            ╚██████╗   ██║   ██████╔╝███████╗██║  ██║██║ ╚═╝ ██║╚██████╔╝██║ ╚████║
                                             ╚═════╝   ╚═╝   ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝\n""")

print("""                        ██████╗ ██╗   ██╗     ██████╗ ███████╗██╗   ██╗████████╗██╗   ██╗██████╗ ██╗███████╗████████╗██╗ ██████╗███████╗
                        ██╔══██╗╚██╗ ██╔╝    ██╔═══██╗██╔════╝██║   ██║╚══██╔══╝██║   ██║██╔══██╗██║██╔════╝╚══██╔══╝██║██╔════╝██╔════╝
                        ██████╔╝ ╚████╔╝     ██║██╗██║█████╗  ██║   ██║   ██║   ██║   ██║██████╔╝██║███████╗   ██║   ██║██║     ███████╗
                        ██╔══██╗  ╚██╔╝      ██║██║██║██╔══╝  ██║   ██║   ██║   ██║   ██║██╔══██╗██║╚════██║   ██║   ██║██║     ╚════██║
                        ██████╔╝   ██║       ╚█║████╔╝██║     ╚██████╔╝   ██║   ╚██████╔╝██║  ██║██║███████║   ██║   ██║╚██████╗███████║
                        ╚═════╝    ╚═╝        ╚╝╚═══╝ ╚═╝      ╚═════╝    ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝╚══════╝   ╚═╝   ╚═╝ ╚═════╝╚══════╝""")
                                                                                                               
sleep(10)

name = input("Input Your Name: ").title()

clear()

speak("professor birch", f"Hurry Up {name}! Come On! We've got other aspiring trainers in line! Pick your starter Cybermon already!")
speak("professor birch", f"Oh Oops, sorry {name}. I forgot that I didn't tell you what your Cybermon are! Oops! Here let me tell you.")
speak("professor birch", f"Here are these Cybermon's Cyberdex Entries.")

clear()

showPokedex(chardvark)

waste = input()
clear()

showPokedex(hipposaur)

waste = input("")
clear()

showPokedex(parsnipe)

waste = input("")
clear()

starterCybermon = input(f"So Which Starter Cybermon Do You Choose {name}: ").capitalize()

party.append(starterCybermon)
    
print(f"\nYou Have Now Obtained {starterCybermon}!")

sleep(5)

speak("barry", "Hey! You think You're So Good!? Let's Battle!")
speak("professor birch", "You know what, I'll give the Winner a special prize as well!")

Battle("Trainer", "Barry", "Chardvark", None, None, None, None, None).battle()
waste = input("")

if Player1.money != 0:
    speak("professor birch", f"Congratulations {name}! You won your first Pokemon Battle, here's your prize!")
    print("You Have Obtained x5 Cyberballs")
    Player1.updateCyberballs(5)

else:
    print("Oh Well, looks like you don't get the special prize")

def question(text,options):    
	place = 0
	cho = ""
	print("\n",Fore.WHITE,text,"(a & d keys to nav. w to confirm)\n")
	while place != 100:
		print(Fore.RED,"\r|",end="")
		for i in range(len(options)):
			if i == place:
				print(Back.WHITE,Fore.RED,options[i],Style.RESET_ALL,Fore.RED,end="|")
				sys.stdout.flush()
				cho = options[i]
			else:
				print(Style.RESET_ALL,Fore.RED,options[i],end = "  |")
				sys.stdout.flush()

question("",["Start","Load","How to Play"])