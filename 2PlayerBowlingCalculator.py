playerA_pins = [["", ""], ["", ""], ["", ""], ["", ""], ["", ""], ["", ""], ["", ""], ["", ""], ["", ""], ["", "", ""]]
playerA_score = ["", "", "", "", "", "", "", "", "", ""]
playerA_scoreCalc = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
memoryA = []
playerB_pins = [["", ""], ["", ""], ["", ""], ["", ""], ["", ""], ["", ""], ["", ""], ["", ""], ["", ""], ["", "", ""]]
playerB_score = ["", "", "", "", "", "", "", "", "", ""]
playerB_scoreCalc = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
memoryB = []

def lastPinsA():
    i = 9
    print("Player A rolls...", (i + 1))
    playerA_pins[9][0] = int(input("Pins: "))
    while playerA_pins[9][0] < 0 or playerA_pins[9][0] > 10:
        print("Please enter a valid value: ")
        playerA_pins[9][0] = int(input("Pins: "))
    if playerA_pins[9][0] == 10:
        playerA_pins[9][1] = int(input("Pins: "))
        while playerA_pins[9][1] < 0 or playerA_pins[9][1] > 10:
            print("Please enter a valid value: ")
            playerA_pins[9][1] = int(input("Pins: "))
        if playerA_pins[9][1] == 10:
            playerA_pins[9][2] = int(input("Pins: "))
            while playerA_pins[9][2] < 0 or playerA_pins[9][2] > 10:
                print("Please enter a valid value: ")
                playerA_pins[9][2] = int(input("Pins: "))
        else:
            playerA_pins[9][2] = int(input("Pins: "))
            while playerA_pins[9][2] < 0 or playerA_pins[9][2] > 10 or playerA_pins[9][1] + playerA_pins[9][2] > 10:
                print("Please enter a valid value: ")
                playerA_pins[9][2] = int(input("Pins: "))
    else:
        playerA_pins[9][1] = int(input("Pins: "))
        while playerA_pins[9][1] < 0 or playerA_pins[9][1] > 10 or playerA_pins[9][0] + playerA_pins[9][1] > 10:
            print("Please enter a valid value: ")
            playerA_pins[9][1] = int(input("Pins: "))
        if playerA_pins[9][0] + playerA_pins[9][1] == 10:
            playerA_pins[9][2] = int(input("Pins: "))
            while playerA_pins[9][2] < 0 or playerA_pins[9][2] > 10:
                print("Please enter a valid value: ")
                playerA_pins[9][2] = int(input("Pins: "))
def lastPinsB():
    i = 9
    print("Player B rolls...", (i + 1))
    playerB_pins[9][0] = int(input("Pins: "))
    while playerB_pins[9][0] < 0 or playerB_pins[9][0] > 10:
        print("Please enter a valid value: ")
        playerB_pins[9][0] = int(input("Pins: "))
    if playerB_pins[9][0] == 10:
        playerB_pins[9][1] = int(input("Pins: "))
        while playerB_pins[9][1] < 0 or playerB_pins[9][1] > 10:
            print("Please enter a valid value: ")
            playerB_pins[9][1] = int(input("Pins: "))
        if playerB_pins[9][1] == 10:
            playerB_pins[9][2] = int(input("Pins: "))
            while playerB_pins[9][2] < 0 or playerB_pins[9][2] > 10:
                print("Please enter a valid value: ")
                playerB_pins[9][2] = int(input("Pins: "))
        else:
            playerB_pins[9][2] = int(input("Pins: "))
            while playerB_pins[9][2] < 0 or playerB_pins[9][2] > 10 or playerB_pins[9][1] + playerB_pins[9][2] > 10:
                print("Please enter a valid value: ")
                playerB_pins[9][2] = int(input("Pins: "))
    else:
        playerB_pins[9][1] = int(input("Pins: "))
        while playerB_pins[9][1] < 0 or playerB_pins[9][1] > 10 or playerB_pins[9][0] + playerB_pins[9][1] > 10:
            print("Please enter a valid value: ")
            playerB_pins[9][1] = int(input("Pins: "))
        if playerB_pins[9][0] + playerB_pins[9][1] == 10:
            playerB_pins[9][2] = int(input("Pins: "))
            while playerB_pins[9][2] < 0 or playerB_pins[9][2] > 10:
                print("Please enter a valid value: ")
                playerB_pins[9][2] = int(input("Pins: "))

def pinsA(i):
    while i < 9:
        print("Player A rolls...", (i + 1))
        playerA_pins[i][0] = int(input("Pins: "))
        while playerA_pins[i][0] < 0 or playerA_pins[i][0] > 10:
            print("Please enter a valid value: ")
            playerA_pins[i][0] = int(input("Pins: "))
        if playerA_pins[i][0] == 10:
            return
        playerA_pins[i][1] = int(input("Pins: "))
        while playerA_pins[i][1] < 0 or playerA_pins[i][1] > 10 or playerA_pins[i][0] + playerA_pins[i][1] > 10:
            print("Please enter a valid value: ")
            playerA_pins[i][1] = int(input("Pins: "))
        if playerA_pins[i][0] + playerA_pins[i][1] >= 0:
            return
    lastPinsA()
def pinsB(i):
    while i < 9:
        print("Player B rolls...", (i + 1))
        playerB_pins[i][0] = int(input("Pins: "))
        while playerB_pins[i][0] < 0 or playerB_pins[i][0] > 10:
            print("Please enter a valid value: ")
            playerB_pins[i][0] = int(input("Pins: "))
        if playerB_pins[i][0] == 10:
            return
        playerB_pins[i][1] = int(input("Pins: "))
        while playerB_pins[i][1] < 0 or playerB_pins[i][1] > 10 or playerB_pins[i][0] + playerB_pins[i][1] > 10:
            print("Please enter a valid value: ")
            playerB_pins[i][1] = int(input("Pins: "))
        if playerB_pins[i][0] + playerB_pins[i][1] >= 0:
            return
    lastPinsB()

def isStrikeA(i):
    if playerA_pins[i][0] == 10 and i < 9:
        memoryA.append(playerA_pins[i][0])
        return True
    elif playerA_pins[i][0] == 10 and i == 9:
        memoryA.append(playerA_pins[i][0])
        memoryA.append(playerA_pins[i][1])
        memoryA.append(playerA_pins[i][2])
        return True
def isStrikeB(i):
    if playerB_pins[i][0] == 10 and i < 9:
        memoryB.append(playerB_pins[i][0])
        return True
    elif playerB_pins[i][0] == 10 and i == 9:
        memoryB.append(playerB_pins[i][0])
        memoryB.append(playerB_pins[i][1])
        memoryB.append(playerB_pins[i][2])
        return True

def isSpareA(i):
    if type(playerA_pins[i][0]) == type(playerA_pins[i][1]) and playerA_pins[i][0] + playerA_pins[i][1] == 10 and i < 9:
        memoryA.append(playerA_pins[i][0])
        memoryA.append(playerA_pins[i][1])
        return True
    elif type(playerA_pins[i][0]) == type(playerA_pins[i][1]) and playerA_pins[i][0] + playerA_pins[i][1] == 10 and i == 9:
        memoryA.append(playerA_pins[i][0])
        memoryA.append(playerA_pins[i][1])
        memoryA.append(playerA_pins[i][2])
        return True
def isSpareB(i):
    if type(playerB_pins[i][0]) == type(playerB_pins[i][1]) and playerB_pins[i][0] + playerB_pins[i][1] == 10 and i < 9:
        memoryB.append(playerB_pins[i][0])
        memoryB.append(playerB_pins[i][1])
        return True
    elif type(playerB_pins[i][0]) == type(playerB_pins[i][1]) and playerB_pins[i][0] + playerB_pins[i][1] == 10 and i == 9:
        memoryB.append(playerB_pins[i][0])
        memoryB.append(playerB_pins[i][1])
        memoryB.append(playerB_pins[i][2])
        return True

def isOpenA(i):
    if type(playerA_pins[i][0]) == type(playerA_pins[i][1]) and playerA_pins[i][0] + playerA_pins[i][1] > 0 and playerA_pins[i][0] + playerA_pins[i][1] != 10:
        memoryA.append(playerA_pins[i][0])
        memoryA.append(playerA_pins[i][1])
        return True
def isOpenB(i):
    if type(playerB_pins[i][0]) == type(playerB_pins[i][1]) and playerB_pins[i][0] + playerB_pins[i][1] > 0 and playerB_pins[i][0] + playerB_pins[i][1] != 10:
        memoryB.append(playerB_pins[i][0])
        memoryB.append(playerB_pins[i][1])
        return True

def memoryAdderA(i):
    if isStrikeA(i):
        if len(memoryA) == 3 and memoryA[0] != 10:
            temp = sum(memoryA)
            playerA_scoreCalc[i - 1] = temp
            playerA_score[i - 1] = sum(playerA_scoreCalc)
            del memoryA[0]
            del memoryA[0]
        elif len(memoryA) == 3 and i != 9:
            temp = sum(memoryA)
            playerA_scoreCalc[i - 2] = temp
            playerA_score[i - 2] = sum(playerA_scoreCalc)
            del memoryA[0]
        elif len(memoryA) == 4:
            temp = sum(memoryA)
            playerA_scoreCalc[i - 1] = temp - memoryA[3]
            playerA_score[i - 1] = sum(playerA_scoreCalc)
            del memoryA[0]
            temp = sum(memoryA)
            playerA_scoreCalc[i] = temp
            playerA_score[i] = sum(playerA_scoreCalc)
        elif len(memoryA) == 5 and memoryA[0] == 10:
            temp = sum(memoryA)
            playerA_scoreCalc[i - 2] = temp - memoryA[3] - memoryA[4]
            playerA_score[i - 2] = sum(playerA_scoreCalc)
            del memoryA[0]
            temp = sum(memoryA)
            playerA_scoreCalc[i - 1] = temp - memoryA[3]
            playerA_score[i - 1] = sum(playerA_scoreCalc)
            del memoryA[0]
            temp = sum(memoryA)
            playerA_scoreCalc[i] = temp
            playerA_score[i] = sum(playerA_scoreCalc)
        elif len(memoryA) == 5 and memoryA[0] != 10:
            temp = sum(memoryA)
            playerA_scoreCalc[i - 1] = temp - memoryA[3] - memoryA[4]
            playerA_score[i - 1] = sum(playerA_scoreCalc)
            del memoryA[0]
            del memoryA[0]
            temp = sum(memoryA)
            playerA_scoreCalc[i] = temp
            playerA_score[i] = sum(playerA_scoreCalc)
    if isSpareA(i):
        if len(memoryA) == 3 and memoryA[0] == 10:
            temp = sum(memoryA)
            playerA_scoreCalc[i - 1] = temp
            playerA_score[i - 1] = sum(playerA_scoreCalc)
            del memoryA[0]
        elif len(memoryA) == 3 and i == 9:
            temp = sum(memoryA)
            memoryA.clear()
            playerA_scoreCalc[i] = temp
            playerA_score[i] = sum(playerA_scoreCalc)
        elif len(memoryA) == 4 and memoryA[0] == 10:
            temp = sum(memoryA)
            playerA_scoreCalc[i - 2] = temp - memoryA[3]
            playerA_score[i - 2] = sum(playerA_scoreCalc)
            del memoryA[0]
            temp = sum(memoryA)
            playerA_scoreCalc[i - 1] = temp
            playerA_score[i - 1] = sum(playerA_scoreCalc)
            del memoryA[0]
        elif len(memoryA) == 4:
            temp = sum(memoryA)
            playerA_scoreCalc[i - 1] = temp - memoryA[3]
            playerA_score[i - 1] = sum(playerA_scoreCalc)
            del memoryA[0]
            del memoryA[0]
        elif len(memoryA) == 5:
            temp = sum(memoryA)
            playerA_scoreCalc[i - 1] = temp - memoryA[3] - memoryA[4]
            playerA_score[i - 1] = sum(playerA_scoreCalc)
            del memoryA[0]
            del memoryA[0]
            temp = sum(memoryA)
            memoryA.clear()
            playerA_scoreCalc[i] = temp
            playerA_score[i] = sum(playerA_scoreCalc)
    if isOpenA(i):
        if len(memoryA) == 2:
            temp = sum(memoryA)
            memoryA.clear()
            playerA_scoreCalc[i] = temp
            playerA_score[i] = sum(playerA_scoreCalc)
        elif len(memoryA) == 3:
            temp = sum(memoryA)
            playerA_scoreCalc[i - 1] = temp
            playerA_score[i - 1] = sum(playerA_scoreCalc)
            del memoryA[0]
            temp = sum(memoryA)
            memoryA.clear()
            playerA_scoreCalc[i] = temp
            playerA_score[i] = sum(playerA_scoreCalc)
        elif len(memoryA) == 4:
            if memoryA[0] == 10:
                temp = sum(memoryA)
                playerA_scoreCalc[i - 2] = temp - memoryA[3]
                playerA_score[i - 2] = sum(playerA_scoreCalc)
                del memoryA[0]
                temp = sum(memoryA)
                playerA_scoreCalc[i - 1] = temp
                playerA_score[i - 1] = sum(playerA_scoreCalc)
                del memoryA[0]
                temp = sum(memoryA)
                memoryA.clear()
                playerA_scoreCalc[i] = temp
                playerA_score[i] = sum(playerA_scoreCalc)
            else:
                temp = sum(memoryA)
                playerA_scoreCalc[i - 1] = temp - memoryA[3]
                playerA_score[i - 1] = sum(playerA_scoreCalc)
                del memoryA[0]
                del memoryA[0]
                temp = sum(memoryA)
                memoryA.clear()
                playerA_scoreCalc[i] = temp
                playerA_score[i] = sum(playerA_scoreCalc)
def memoryAdderB(i):
    if isStrikeB(i):
        if len(memoryB) == 3 and memoryB[0] != 10:
            temp = sum(memoryB)
            playerB_scoreCalc[i - 1] = temp
            playerB_score[i - 1] = sum(playerB_scoreCalc)
            del memoryB[0]
            del memoryB[0]
        elif len(memoryB) == 3 and i != 9:
            temp = sum(memoryB)
            playerB_scoreCalc[i - 2] = temp
            playerB_score[i - 2] = sum(playerB_scoreCalc)
            del memoryB[0]
        elif len(memoryB) == 4:
            temp = sum(memoryB)
            playerB_scoreCalc[i - 1] = temp - memoryB[3]
            playerB_score[i - 1] = sum(playerB_scoreCalc)
            del memoryB[0]
            temp = sum(memoryB)
            playerB_scoreCalc[i] = temp
            playerB_score[i] = sum(playerB_scoreCalc)
        elif len(memoryB) == 5 and memoryB[0] == 10:
            temp = sum(memoryB)
            playerB_scoreCalc[i - 2] = temp - memoryB[3] - memoryB[4]
            playerB_score[i - 2] = sum(playerB_scoreCalc)
            del memoryB[0]
            temp = sum(memoryB)
            playerB_scoreCalc[i - 1] = temp - memoryB[3]
            playerB_score[i - 1] = sum(playerB_scoreCalc)
            del memoryB[0]
            temp = sum(memoryB)
            playerB_scoreCalc[i] = temp
            playerB_score[i] = sum(playerB_scoreCalc)
        elif len(memoryB) == 5 and memoryB[0] != 10:
            temp = sum(memoryB)
            playerB_scoreCalc[i - 1] = temp - memoryB[3] - memoryB[4]
            playerB_score[i - 1] = sum(playerB_scoreCalc)
            del memoryB[0]
            del memoryB[0]
            temp = sum(memoryB)
            playerB_scoreCalc[i] = temp
            playerB_score[i] = sum(playerB_scoreCalc)
    if isSpareB(i):
        if len(memoryB) == 3 and memoryB[0] == 10:
            temp = sum(memoryB)
            playerB_scoreCalc[i - 1] = temp
            playerB_score[i - 1] = sum(playerB_scoreCalc)
            del memoryB[0]
        elif len(memoryB) == 3 and i == 9:
            temp = sum(memoryB)
            memoryB.clear()
            playerB_scoreCalc[i] = temp
            playerB_score[i] = sum(playerB_scoreCalc)
        elif len(memoryB) == 4 and memoryB[0] == 10:
            temp = sum(memoryB)
            playerB_scoreCalc[i - 2] = temp - memoryB[3]
            playerB_score[i - 2] = sum(playerB_scoreCalc)
            del memoryB[0]
            temp = sum(memoryB)
            playerB_scoreCalc[i - 1] = temp
            playerB_score[i - 1] = sum(playerB_scoreCalc)
            del memoryB[0]
        elif len(memoryB) == 4:
            temp = sum(memoryB)
            playerB_scoreCalc[i - 1] = temp - memoryB[3]
            playerB_score[i - 1] = sum(playerB_scoreCalc)
            del memoryB[0]
            del memoryB[0]
        elif len(memoryB) == 5:
            temp = sum(memoryB)
            playerB_scoreCalc[i - 1] = temp - memoryB[3] - memoryB[4]
            playerB_score[i - 1] = sum(playerB_scoreCalc)
            del memoryB[0]
            del memoryB[0]
            temp = sum(memoryB)
            memoryB.clear()
            playerB_scoreCalc[i] = temp
            playerB_score[i] = sum(playerB_scoreCalc)
    if isOpenB(i):
        if len(memoryB) == 2:
            temp = sum(memoryB)
            memoryB.clear()
            playerB_scoreCalc[i] = temp
            playerB_score[i] = sum(playerB_scoreCalc)
        elif len(memoryB) == 3:
            temp = sum(memoryB)
            playerB_scoreCalc[i - 1] = temp
            playerB_score[i - 1] = sum(playerB_scoreCalc)
            del memoryB[0]
            temp = sum(memoryB)
            memoryB.clear()
            playerB_scoreCalc[i] = temp
            playerB_score[i] = sum(playerB_scoreCalc)
        elif len(memoryB) == 4:
            if memoryB[0] == 10:
                temp = sum(memoryB)
                playerB_scoreCalc[i - 2] = temp - memoryB[3]
                playerB_score[i - 2] = sum(playerB_scoreCalc)
                del memoryB[0]
                temp = sum(memoryB)
                playerB_scoreCalc[i - 1] = temp
                playerB_score[i - 1] = sum(playerB_scoreCalc)
                del memoryB[0]
                temp = sum(memoryB)
                memoryB.clear()
                playerB_scoreCalc[i] = temp
                playerB_score[i] = sum(playerB_scoreCalc)
            else:
                temp = sum(memoryB)
                playerB_scoreCalc[i - 1] = temp - memoryB[3]
                playerB_score[i - 1] = sum(playerB_scoreCalc)
                del memoryB[0]
                del memoryB[0]
                temp = sum(memoryB)
                memoryB.clear()
                playerB_scoreCalc[i] = temp
                playerB_score[i] = sum(playerB_scoreCalc)

def interfaceA():
    print("Player A Ball Scores: ", end="") 
    for i in range(10):
        if i < 9:
            if playerA_pins[i][0] == 10:
                print(playerA_pins[i][0], end=" ")
            else:
                print(playerA_pins[i][0], playerA_pins[i][1], end=" ")
        elif i == 9:
            print(playerA_pins[i][0], playerA_pins[i][1], playerA_pins[i][2], end=" ")
    print()
    print("Player A Total Scores: ", end="")
    for i in range(10):
        if i < 9:
            print(playerA_score[i], end=" | ")
        if i == 9:
            print(playerA_score[i], end="")
    print()
def interfaceB():
    print("Player B Ball Scores: ", end="")
    for i in range(10):
        if i < 9:
            if playerB_pins[i][0] == 10:
                print(playerB_pins[i][0], end=" ")
            else:
                print(playerB_pins[i][0], playerB_pins[i][1], end=" ")
        elif i == 9:
            print(playerB_pins[i][0], playerB_pins[i][1], playerB_pins[i][2], end=" ")
    print()
    print("Player B Total Scores: ", end="")
    for i in range(10):
        if i < 9:
            print(playerB_score[i], end=" | ")
        if i == 9:
            print(playerB_score[i], end="")
    print()

def winner():
    if playerA_score[9] > playerB_score[9]:
        print("Winner is player A.")
    elif playerA_score[9] < playerB_score[9]:
        print("Winner is player B.")

def main():
    for i in range(10):
        pinsA(i)
        memoryAdderA(i)
        interfaceA()
        pinsB(i)
        memoryAdderB(i)
        interfaceB()
    winner()

main()