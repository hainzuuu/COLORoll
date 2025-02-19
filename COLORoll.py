import random
import time
import sys


class Deque:

    def __init__(self):
        self.deque = []

    def addFront(self, color):
        self.deque.insert(0, color)

    def addRear(self, result):
        self.deque.append(result)

    def delFront(self):
        return self.deque.pop(0)

    def delRear(self):
        return self.deque.pop()

    def peekFront(self):
        return self.deque[0]

    def peekRear(self):
        return self.deque[-1]

    def showDeque(self):
        print(self.deque)


class Game:

    def __init__(self):
        self.colorList = ["green", "red", "blue", "pink", "white", "yellow"]
        self.multiplier = []
        self.prize = 0
        self.result = []
        self.quota = 0
        self.maxBet = 0
        self.moneyLose = 0

    def roll(self):
        self.result = random.choices(self.colorList, k=3)

    def showResult(self):
        for x in range(len(game.result)):
            time.sleep(0.75)
            if not Coloredbet:
                print((game.result[x]), end=" ")
            else:
                if game.result[x] == "green":
                    print(Color.GREEN + game.result[x] + Color.END, end=" ")
                elif game.result[x] == "red":
                    print(Color.RED + game.result[x] + Color.END, end=" ")
                elif game.result[x] == "blue":
                    print(Color.BLUE + game.result[x] + Color.END, end=" ")
                elif game.result[x] == "pink":
                    print(Color.PURPLE + game.result[x] + Color.END, end=" ")
                elif game.result[x] == "white":
                    print(game.result[x], end=" ")
                elif game.result[x] == "yellow":
                    print(Color.YELLOW + game.result[x] + Color.END, end=" ")

        time.sleep(0.75)
        print()


class Player:

    def __init__(self):
        self.money = 0
        self.colorBet = []
        self.moneyBet = []
        self.lose = []

    def showAll(self):
        for x in range(len(self.moneyBet)):
            print(self.moneyBet[x], end=" ")
        print()


class Color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'





def separator():
    print("+++*+++*+++*+++*+++*+++*  COLORoll  +++*+++*+++*+++*+++*+++*")


def load_animation():
    load_str = "                    coloroll is loading..."

    ls_len = len(load_str)
    animation = "|/-\\"
    anicount = 0

    counttime = 0

    i = 0

    while (counttime != 80):  # loading time 80 is the original
        time.sleep(0.075)
        load_str_list = list(load_str)
        x = ord(load_str_list[i])
        y = 0
        if x != 32 and x != 46:
            if x > 90:
                y = x - 32
            else:
                y = x + 32
            load_str_list[i] = chr(y)
        res = ''
        for j in range(ls_len):
            res = res + load_str_list[j]
        sys.stdout.write("\r" + res + animation[anicount])
        sys.stdout.flush()
        load_str = res
        anicount = (anicount + 1) % 4
        i = (i + 1) % ls_len
        counttime = counttime + 1
    print()
    if not Coloredbet:
        input('{:^59s}'.format("press enter to continue: "))
    else:
        input('{:^59s}'.format(Color.GREEN + "press enter to continue: " + Color.END))

def backAnimation():
    load_str = "                    going back to main menu..."
    ls_len = len(load_str)
    animation = "|/-\\"
    anicount = 0

    counttime = 0

    i = 0

    while (counttime != 80):  # loading time
        time.sleep(0.075)
        load_str_list = list(load_str)
        x = ord(load_str_list[i])
        y = 0
        if x != 32 and x != 46:
            if x > 90:
                y = x - 32
            else:
                y = x + 32
            load_str_list[i] = chr(y)
        res = ''
        for j in range(ls_len):
            res = res + load_str_list[j]
        sys.stdout.write("\r" + res + animation[anicount])
        sys.stdout.flush()
        load_str = res
        anicount = (anicount + 1) % 4
        i = (i + 1) % ls_len
        counttime = counttime + 1
    print()


def showMenu():
    separator()
    # print(f"money: {player.money}\t\t\tmax_bet: {game.maxBet}\t\t\tquota: {game.quota}")
    print(f"money: {player.money}")
    if not Coloredbet:
        for x in ("""          _____ ____  _      ____  _____       _ _ 
         / ____/ __ \| |    / __ \|  __ \     | | |
        | |   | |  | | |   | |  | | |__) |___ | | |
        | |   | |  | | |   | |  | |  _  // _ \| | |
        | |___| |__| | |___| |__| | | \ \ (_) | | |
         \_____\____/|______\____/|_|  \_\___/|_|_|
    
                                                """):
            time.sleep(0.005)
            print(x, end="")
    else:
        for x in (Color.YELLOW + """          _____ ____  _      ____  _____       _ _ 
         / ____/ __ \| |    / __ \|  __ \     | | |
        | |   | |  | | |   | |  | | |__) |___ | | |
        | |   | |  | | |   | |  | |  _  // _ \| | |
        | |___| |__| | |___| |__| | | \ \ (_) | | |
         \_____\____/|______\____/|_|  \_\___/|_|_|

                                                """ + Color.END):
            time.sleep(0.005)
            print(x, end="")
    print()

    # print("\t\t\tStart\tStore\tExit")
    print('{:^55s}'.format("[Start]\t[Store]\t[Exit]"))
    print()
    print()
    separator()


def showRules():
    separator()
    print(f"money: {player.money}\t\t\tmax_bet: {game.maxBet}\t\t\tquota: {game.quota}")
    print()
    for letters in ("""                           Rules:
          -Choose a color from the list
          -Decide how much to bet for your chosen color
          -You can only bet the max bet stated above
          -If the quota is met, the game is over
          -If you ran out of money, the game is also over
          -Collect money to purchase items
          -Have fun!!!"""):
        time.sleep(0.03) #0.03 original
        print(letters, end="")
    print()
    print()
    print()
    separator()




def pickDifficulty():
    separator()

    for x in ("""          _____ ____  _      ____  _____       _ _ 
         / ____/ __ \| |    / __ \|  __ \     | | |
        | |   | |  | | |   | |  | | |__) |___ | | |
        | |   | |  | | |   | |  | |  _  // _ \| | |
        | |___| |__| | |___| |__| | | \ \ (_) | | |
         \_____\____/|______\____/|_|  \_\___/|_|_|

                                            """):
        time.sleep(0.005)
        print(x, end="")
    print()
    # print("\t\t\tStart\tStore\tExit")
    print('{:^55s}'.format("[easy] [medium] [hard] [impossible]"))
    print()
    print()
    separator()


def processDifficulty(difficulty):
    if difficulty == "easy":
        player.money = 150
        game.quota = 300
        game.maxBet = 100
    elif difficulty == "medium":
        player.money = 100
        game.quota = 500
        game.maxBet = 75
    elif difficulty == "hard":
        player.money = 50
        game.quota = 500
        game.maxBet = 50
    elif difficulty == "impossible":
        player.money = 10
        game.quota = 1000
        game.maxBet = 10


def typeWriter(msg):
    for x in msg:
        time.sleep(0.03)
        print(x, end="")


def bigTypeWriter(msg):
    for x in msg:
        time.sleep(0.005)
        print(x, end="")


def goStore():
    print(f"money: {player.money}")
    bigTypeWriter("""           _____ _______ ____  _____  ______ 
          / ____|__   __/ __ \|  __ \|  ____|
         | (___    | | | |  | | |__) | |__   
          \___ \   | | | |  | |  _  /|  __|  
          ____) |  | | | |__| | | \ \| |____ 
         |_____/   |_|  \____/|_|  \_\______|

                                     """)
    print()
    print('{:^55s}'.format("""[Upbet]- $199 [Manybet] - $299 [Coloredbet] - $499"""))
    print('{:^55s}'.format("[back]"))


def goStart():
    if not alredyShowedRules:
        showRules()
    load_animation()
    goGame()


def goGame():
    origMaxBet = game.maxBet

    while True:
        separator()
        if player.money < game.maxBet:
            game.maxBet = player.money
        else:
            game.maxBet = origMaxBet

        if not Coloredbet:
            print(f"money: {player.money}\t\t\tmax_bet: {game.maxBet}\t\t\tquota: {game.quota}")
        else:
            print(Color.CYAN + f"money: {player.money}\t\t\tmax_bet: {game.maxBet}\t\t\tquota: {game.quota}" + Color.END)

        print()
        if not Coloredbet:
            print('{:^55s}'.format("[green] [red] [blue] [pink] [white] [yellow]"))
        else:
            print('{:^55s}'.format(Color.GREEN + "\t\t[green] " + Color.END + Color.RED + "[red] " + Color.END + Color.BLUE + "[blue] " + Color.END + Color.PURPLE + "[pink] " + Color.END + "[white] " + Color.YELLOW + "[yellow]" + Color.END))

        if not Manybet:
            while True:
                print('{:^55s}'.format("Enter one color from the list: "))

                player.colorBet = input("\t\t\t  ").split()

                if player.colorBet == []:
                    if not Coloredbet:
                        print('{:^55s}'.format("Error: Enter colors that are on the list"))
                    else:
                        print('{:^55s}'.format(Color.RED + "\t\tError: Enter colors that are on the list" + Color.END))
                    continue

                if len(player.colorBet) > 1:
                    if not Coloredbet:
                        print('{:^55s}'.format("Error: Enter one color only"))
                    else:
                        print('{:^55s}'.format(Color.RED + "\t\tError: Enter one color only" + Color.END))
                    continue

                if player.colorBet[0] not in game.colorList:
                    if not Coloredbet:
                        print('{:^55s}'.format("Error: Enter colors that are on the list"))
                    else:
                        print('{:^55s}'.format(Color.RED + "\t\tError: Enter colors that are on the list" + Color.END))
                    continue


                else:
                    break

        elif Manybet:
            while True:
                wrongInput = False
                print('{:^55s}'.format("Enter one or more colors separated by space: "))
                player.colorBet = input("\t\t\t  ").split()

                for x in range(len(player.colorBet)):
                    if player.colorBet[x] not in game.colorList:
                        separator()
                        if not Coloredbet:
                            print('{:^55s}'.format("Error: Enter colors that are on the list"))
                        else:
                            print('{:^55s}'.format(Color.RED + "\t\tError: Enter colors that are on the list" + Color.END))
                        separator()
                        wrongInput = True
                        break
                if wrongInput:
                    continue
                else:
                    break


        # entering the money bet
        while True:
            separator()
            numbers = list("1234567890")
            isNumbers = False
            if not Manybet:
                print('{:^55s}'.format("Enter bet amount: "))
            if Manybet:
                print('{:^55s}'.format("Enter bet for each color. If multiple, separated by space: "))
            player.moneyBet = input("\t\t\t  ").split()
            for values in player.moneyBet:
                for digit in values:
                    if digit not in numbers:
                        if not Coloredbet:
                            print('{:^55s}'.format("Error: Enter positive, numbers only"))  # error message
                        else:
                            print('{:^55s}'.format(Color.RED + "\t\tError: Enter positive, numbers only" + Color.END))
                        isNumbers = False
                        break



                    else:
                        isNumbers = True

                    continue
                break

            if len(player.moneyBet) != len(player.colorBet):
                separator()
                if not Coloredbet:
                    print('{:^55s}'.format("Error: Give a bet for each of the color separated by space."))  # error message
                else:
                    ('{:^55s}'.format(Color.RED + "Error: Give a bet for each of the color separated by space." + Color.END))
                continue

            if not isNumbers:
                continue


            else:
                maxbetError = False
                valueSum = 0
                for values in player.moneyBet:
                    if int(values) > game.maxBet:
                        if not Coloredbet:
                            print('{:^55s}'.format(f"Error: You can only bet maximum of {game.maxBet}"))
                        else:
                            print('{:^55s}'.format(Color.RED + f"\t\tError: You can only bet maximum of {game.maxBet}" + Color.END))
                        maxbetError = True
                        break
                    valueSum += int(values)

                if valueSum > player.money:
                    if not Coloredbet:
                        print('{:^55s}'.format(f"Error: Insufficient money for that amount of bet"))
                    else:
                        print('{:^55s}'.format(Color.RED + f"\t\tError: Insufficient money for that amount of bet" + Color.END))
                    maxbetError = True

                if maxbetError:
                    continue
                else:
                    break


        game.roll()

        addColorBet()
        addResult()

        goingDown(Coloredbet)
        goingDown(Coloredbet)

        print("\t\t\t\t\t", end="")
        game.showResult()
        print()

        compare()

        addMoneyBet()
        addMultiplier()
        isLucky()

        if not Coloredbet:
            print("prize =", computePrize(), "lose:", game.moneyLose)

        else:
            print(Color.GREEN + "prize =" + Color.END, computePrize(), Color.RED + "lose:" + Color.END, game.moneyLose)

        addPrize()

        clearAll()

        if player.money >= game.quota:
            congrats()
            break
        elif player.money <= 0:
            gameOver()
            break


# algo
def gameOver():
    if not Coloredbet:
        print("money: ", player.money)
    else:
        print(Color.CYAN + "money: " + Color.END, player.money)
    separator()
    if not Coloredbet:
        print("""   _____          __  __ ______    ______      ________ _____  
 / ____|   /\   |  \/  |  ____|  / __ \ \    / /  ____|  __ \ 
| |  __   /  \  | \  / | |__    | |  | \ \  / /| |__  | |__) |
| | |_ | / /\ \ | |\/| |  __|   | |  | |\ \/ / |  __| |  _  / 
| |__| |/ ____ \| |  | | |____  | |__| | \  /  | |____| | \ \ 
 \_____/_/    \_\_|  |_|______|  \____/   \/   |______|_|  \_\ 
                                                               
                                                               """)
    else:
        print(Color.RED + """      _____          __  __ ______    ______      ________ _____  
     / ____|   /\   |  \/  |  ____|  / __ \ \    / /  ____|  __ \ 
    | |  __   /  \  | \  / | |__    | |  | \ \  / /| |__  | |__) |
    | | |_ | / /\ \ | |\/| |  __|   | |  | |\ \/ / |  __| |  _  / 
    | |__| |/ ____ \| |  | | |____  | |__| | \  /  | |____| | \ \ 
     \_____/_/    \_\_|  |_|______|  \____/   \/   |______|_|  \_\ 
                                                               
                                                               """ + Color.END)
    separator()

def congrats():
    separator()

    if not Coloredbet:
        print("""   _____ ____  _   _  _____ _____         _______ _____ 
  / ____/ __ \| \ | |/ ____|  __ \     /\|__   __/ ____|
 | |   | |  | |  \| | |  __| |__) |   /  \  | | | (___  
 | |   | |  | | . ` | | |_ |  _  /   / /\ \ | |  \___ \ 
 | |___| |__| | |\  | |__| | | \ \  / ____ \| |  ____) |
  \_____\____/|_| \_|\_____|_|  \_\/_/    \_\_| |_____/          
                                                        """)
    else:
        print(Color.GREEN + """   _____ ____  _   _  _____ _____         _______ _____ 
  / ____/ __ \| \ | |/ ____|  __ \     /\|__   __/ ____|
 | |   | |  | |  \| | |  __| |__) |   /  \  | | | (___  
 | |   | |  | | . ` | | |_ |  _  /   / /\ \ | |  \___ \ 
 | |___| |__| | |\  | |__| | | \ \  / ____ \| |  ____) |
  \_____\____/|_| \_|\_____|_|  \_\/_/    \_\_| |_____/          
                                                        """ + Color.END)
    print('{:^55s}'.format("QUOTA REACHED"))
    separator()
    print("money: ", player.money)
    backAnimation()
    game.quota = player.money + 300

    if difficulty == "impossible":
        print(""" Good job player, You have defeated the impossible, 
         contact developer Longares for a gcash reward.
         Send this code: GM50GC
                                                            """)
    time.sleep(3)

def goodBye():
    print("""   _____  ____   ____  _____  ______     ________ 
  / ____|/ __ \ / __ \|  __ \|  _ \ \   / /  ____|
 | |  __| |  | | |  | | |  | | |_) \ \_/ /| |__   
 | | |_ | |  | | |  | | |  | |  _ < \   / |  __|  
 | |__| | |__| | |__| | |__| | |_) | | |  | |____ 
  \_____|\____/ \____/|_____/|____/  |_|  |______|
                                                  """)

def isLucky():
    isThreeColors = 0
    for x in range(-1, -4 -1):
        isThreeColors += moneyDeque[x]

    if isThreeColors == 3:
        print("LUCKY!!!")


def addColorBet():
    for x in range(len(player.colorBet)):
        colorDeque.addFront(player.colorBet[x])


def addMoneyBet():
    for x in range(len(player.moneyBet)):
        moneyDeque.addFront(int(player.moneyBet[x]))


def addResult():
    for x in range(len(game.result)):
        colorDeque.addRear(game.result[x])


def addMultiplier():
    game.multiplier.reverse()
    for x in range(len(player.moneyBet)):
        moneyDeque.addRear(game.multiplier[x])


def compare():
    multi = 0
    for x in range(len(player.colorBet)):

        for y in range(-1, -4, -1):

            if colorDeque.peekFront() == colorDeque.deque[y]:
                multi += 1

        colorDeque.delFront()
        game.multiplier.append(multi)
        multi = 0



def computePrize():
    for x in range(len(player.moneyBet)):
        game.prize += moneyDeque.peekFront() * moneyDeque.peekRear()
        if moneyDeque.peekRear() == 0:
            game.moneyLose += (moneyDeque.peekFront())
        moneyDeque.delFront()
        moneyDeque.delRear()
    return game.prize




def addPrize():
    player.money += game.prize
    player.money -= game.moneyLose


def clearAll():
    colorDeque.deque.clear()
    moneyDeque.deque.clear()
    player.lose.clear()
    game.prize = 0
    game.moneyLose = 0


def goingDown(Coloredbet):
    for x in range(1, 5):
        time.sleep(0.1)
        if not Coloredbet:
            print(("\t\t\t\t\t" + " " * x), " \    \    \ ")
        else:
            print(Color.YELLOW + ("\t\t\t\t\t" + " " * x), " \    \    \ " + Color.END)

    for x in range(5, 1, -1):
        time.sleep(0.1)
        if not Coloredbet:
            print(("\t\t\t\t\t" + " " * x), "/    /    / ")
        else:
            print(Color.YELLOW + ("\t\t\t\t\t" + " " * x), "/    /    / " + Color.END)


player = Player()
game = Game()
colorDeque = Deque()
moneyDeque = Deque()

difficultyDone = False
Upbet = False
Manybet = False
Coloredbet = False
alredyShowedRules = False


while True:
    gameLose = False
    showMenu()
    titleAnimationDone = True


    typeWriter("Enter action: ")
    menuInput = input().lower()
    if menuInput not in ["start", "store", "exit"]:
        if not Coloredbet:
            print("Enter valid input")
        else:
            print(Color.RED + "Enter valid input" + Color.END)
        continue
    elif menuInput == "exit":
        goodBye()
        break

    elif menuInput == "store":
        goStore()
        while True:
            storeInput = input("Enter action: ").lower()
            if storeInput not in ["upbet", "manybet", "coloredbet", "back"]:
                print("Error: Select proper action")
                continue
            else:


                if storeInput == "back":
                    break

                elif storeInput == "upbet":
                    if not Upbet:
                        if player.money > 199:
                            Upbet = True
                            game.maxBet += 100
                            player.money -= 199
                            print("Purchase confirmed: Max bet is increased")
                            print(f'money left: {player.money}')
                            continue
                        elif player.money == 199:
                            print("You can't buy this because you should have money left")
                            continue

                        else:
                            print("Error: Insufficient money.")
                            continue
                    else:
                        print("You already bought this item")

                elif storeInput == "manybet":
                    if not Manybet:
                        if player.money > 299:
                            Manybet = True
                            player.money -= 300
                            print("Purchase confirmed: You can now bet on multiple colors")
                            print(f'money left: {player.money}')
                            continue

                        elif player.money == 299:
                            print("You can't buy this because you should have money left")
                            continue

                        else:
                            print("Error: Insufficient money.")
                            continue
                    else:
                        print("You already bought this item")

                elif storeInput == "coloredbet":
                    if not Coloredbet:
                        if player.money > 499:
                            Coloredbet = True
                            player.money -= 499
                            print(Color.GREEN + "Purchase confirmed: Enjoy the Colorful Game" + Color.END)
                            print(f'money left: {player.money}')
                            continue

                        elif player.money == 499:
                            print("You can't buy this because you should have money left")
                            continue

                        else:
                            print("Error: Insufficient money.")
                            continue
                    else:
                        print("You already bought this item")

                continue

        continue

    elif menuInput == "start":
        if not difficultyDone:
            pickDifficulty()
            while True:
                difficulty = input("Enter difficulty: ").lower()
                if difficulty not in ["easy", "medium", "hard", "impossible"]:
                    print("Select correct difficulty")
                    separator()
                    continue
                processDifficulty(difficulty)
                difficultyDone = True
                break
        goStart()
        alredyShowedRules = True

    if player.money <= 0:
        break

