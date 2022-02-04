player_pins = [["", ""], ["", ""], ["", ""], ["", ""], ["", ""], ["", ""], ["", ""], ["", ""], ["", ""], ["", "", ""]]
player_score = ["", "", "", "", "", "", "", "", "", ""]
player_scoreCalc = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
memory = []

def lastPins():
    i = 9
    print("Player rolls...", (i + 1))
    player_pins[9][0] = int(input("Pins: "))
    while player_pins[9][0] < 0 or player_pins[9][0] > 10:
        print("Please enter a valid value: ")
        player_pins[9][0] = int(input("Pins: "))
    if player_pins[9][0] == 10:
        player_pins[9][1] = int(input("Pins: "))
        while player_pins[9][1] < 0 or player_pins[9][1] > 10:
            print("Please enter a valid value: ")
            player_pins[9][1] = int(input("Pins: "))
        if player_pins[9][1] == 10:
            player_pins[9][2] = int(input("Pins: "))
            while player_pins[9][2] < 0 or player_pins[9][2] > 10:
                print("Please enter a valid value: ")
                player_pins[9][2] = int(input("Pins: "))
        else:
            player_pins[9][2] = int(input("Pins: "))
            while player_pins[9][2] < 0 or player_pins[9][2] > 10 or player_pins[9][1] + player_pins[9][2] > 10:
                print("Please enter a valid value: ")
                player_pins[9][2] = int(input("Pins: "))
    else:
        player_pins[9][1] = int(input("Pins: "))
        while player_pins[9][1] < 0 or player_pins[9][1] > 10 or player_pins[9][0] + player_pins[9][1] > 10:
            print("Please enter a valid value: ")
            player_pins[9][1] = int(input("Pins: "))
        if player_pins[9][0] + player_pins[9][1] == 10:
            player_pins[9][2] = int(input("Pins: "))
            while player_pins[9][2] < 0 or player_pins[9][2] > 10:
                print("Please enter a valid value: ")
                player_pins[9][2] = int(input("Pins: "))

def pins(i):
    while i < 9:
        print("Player rolls...", (i + 1))
        player_pins[i][0] = int(input("Pins: "))
        while player_pins[i][0] < 0 or player_pins[i][0] > 10:
            print("Please enter a valid value: ")
            player_pins[i][0] = int(input("Pins: "))
        if player_pins[i][0] == 10:
            return
        player_pins[i][1] = int(input("Pins: "))
        while player_pins[i][1] < 0 or player_pins[i][1] > 10 or player_pins[i][0] + player_pins[i][1] > 10:
            print("Please enter a valid value: ")
            player_pins[i][1] = int(input("Pins: "))
        if player_pins[i][0] + player_pins[i][1] >= 0:
            return
    lastPins()

def isStrike(i):
    if player_pins[i][0] == 10 and i < 9:
        memory.append(player_pins[i][0])
        return True
    elif player_pins[i][0] == 10 and i == 9:
        memory.append(player_pins[i][0])
        memory.append(player_pins[i][1])
        memory.append(player_pins[i][2])
        return True

def isSpare(i):
    if type(player_pins[i][0]) == type(player_pins[i][1]) and player_pins[i][0] + player_pins[i][1] == 10 and i < 9:
        memory.append(player_pins[i][0])
        memory.append(player_pins[i][1])
        return True
    elif type(player_pins[i][0]) == type(player_pins[i][1]) and player_pins[i][0] + player_pins[i][1] == 10 and i == 9:
        memory.append(player_pins[i][0])
        memory.append(player_pins[i][1])
        memory.append(player_pins[i][2])
        return True

def isOpen(i):
    if type(player_pins[i][0]) == type(player_pins[i][1]) and player_pins[i][0] + player_pins[i][1] > 0 and player_pins[i][0] + player_pins[i][1] != 10:
        memory.append(player_pins[i][0])
        memory.append(player_pins[i][1])
        return True

def memoryAdder(i):
    if isStrike(i):
        if len(memory) == 3 and memory[0] != 10:
            temp = sum(memory)
            player_scoreCalc[i - 1] = temp
            player_score[i - 1] = sum(player_scoreCalc)
            del memory[0]
            del memory[0]
        elif len(memory) == 3 and i != 9:
            temp = sum(memory)
            player_scoreCalc[i - 2] = temp
            player_score[i - 2] = sum(player_scoreCalc)
            del memory[0]
        elif len(memory) == 4:
            temp = sum(memory)
            player_scoreCalc[i - 1] = temp - memory[3]
            player_score[i - 1] = sum(player_scoreCalc)
            del memory[0]
            temp = sum(memory)
            player_scoreCalc[i] = temp
            player_score[i] = sum(player_scoreCalc)
        elif len(memory) == 5 and memory[0] == 10:
            temp = sum(memory)
            player_scoreCalc[i - 2] = temp - memory[3] - memory[4]
            player_score[i - 2] = sum(player_scoreCalc)
            del memory[0]
            temp = sum(memory)
            player_scoreCalc[i - 1] = temp - memory[3]
            player_score[i - 1] = sum(player_scoreCalc)
            del memory[0]
            temp = sum(memory)
            player_scoreCalc[i] = temp
            player_score[i] = sum(player_scoreCalc)
        elif len(memory) == 5 and memory[0] != 10:
            temp = sum(memory)
            player_scoreCalc[i - 1] = temp - memory[3] - memory[4]
            player_score[i - 1] = sum(player_scoreCalc)
            del memory[0]
            del memory[0]
            temp = sum(memory)
            player_scoreCalc[i] = temp
            player_score[i] = sum(player_scoreCalc)
    if isSpare(i):
        if len(memory) == 3 and memory[0] == 10:
            temp = sum(memory)
            player_scoreCalc[i - 1] = temp
            player_score[i - 1] = sum(player_scoreCalc)
            del memory[0]
        elif len(memory) == 3 and i == 9:
            temp = sum(memory)
            memory.clear()
            player_scoreCalc[i] = temp
            player_score[i] = sum(player_scoreCalc)
        elif len(memory) == 4 and memory[0] == 10:
            temp = sum(memory)
            player_scoreCalc[i - 2] = temp - memory[3]
            player_score[i - 2] = sum(player_scoreCalc)
            del memory[0]
            temp = sum(memory)
            player_scoreCalc[i - 1] = temp
            player_score[i - 1] = sum(player_scoreCalc)
            del memory[0]
        elif len(memory) == 4:
            temp = sum(memory)
            player_scoreCalc[i - 1] = temp - memory[3]
            player_score[i - 1] = sum(player_scoreCalc)
            del memory[0]
            del memory[0]
        elif len(memory) == 5:
            temp = sum(memory)
            player_scoreCalc[i - 1] = temp - memory[3] - memory[4]
            player_score[i - 1] = sum(player_scoreCalc)
            del memory[0]
            del memory[0]
            temp = sum(memory)
            memory.clear()
            player_scoreCalc[i] = temp
            player_score[i] = sum(player_scoreCalc)
    if isOpen(i):
        if len(memory) == 2:
            temp = sum(memory)
            memory.clear()
            player_scoreCalc[i] = temp
            player_score[i] = sum(player_scoreCalc)
        elif len(memory) == 3:
            temp = sum(memory)
            player_scoreCalc[i - 1] = temp
            player_score[i - 1] = sum(player_scoreCalc)
            del memory[0]
            temp = sum(memory)
            memory.clear()
            player_scoreCalc[i] = temp
            player_score[i] = sum(player_scoreCalc)
        elif len(memory) == 4:
            if memory[0] == 10:
                temp = sum(memory)
                player_scoreCalc[i - 2] = temp - memory[3]
                player_score[i - 2] = sum(player_scoreCalc)
                del memory[0]
                temp = sum(memory)
                player_scoreCalc[i - 1] = temp
                player_score[i - 1] = sum(player_scoreCalc)
                del memory[0]
                temp = sum(memory)
                memory.clear()
                player_scoreCalc[i] = temp
                player_score[i] = sum(player_scoreCalc)
            else:
                temp = sum(memory)
                player_scoreCalc[i - 1] = temp - memory[3]
                player_score[i - 1] = sum(player_scoreCalc)
                del memory[0]
                del memory[0]
                temp = sum(memory)
                memory.clear()
                player_scoreCalc[i] = temp
                player_score[i] = sum(player_scoreCalc)

def interface():
    print("Player Ball Scores: ", end="") 
    for i in range(10):
        if i < 9:
            if player_pins[i][0] == 10:
                print(player_pins[i][0], end=" ")
            else:
                print(player_pins[i][0], player_pins[i][1], end=" ")
        elif i == 9:
            print(player_pins[i][0], player_pins[i][1], player_pins[i][2], end=" ")
    print()
    print("Player Total Scores: ", end="")
    for i in range(10):
        if i < 9:
            print(player_score[i], end=" | ")
        if i == 9:
            print(player_score[i], end="")
    print()

def main():
    for i in range(10):
        pins(i)
        memoryAdder(i)
        interface()

main()