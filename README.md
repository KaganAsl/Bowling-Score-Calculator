# Bowling-Score-Calculator
Python Bowling Score Calculator

It's not just only calculate, it has also a interface that shows you pins and scores.

Normal one just for the score calculate. 2 player one has a winner at the end.

I couldn't check all possibilities but I guess it works correct.

# Rules Of Bowling

A strike frame: The player knocks down all ten pins with one ball (on the first roll). The score
for a strike is 10 + the next two rolls.

A spare frame: The player knocks down all ten pins with two balls. The score for a spare is
10 + the next roll.

An open frame: The player fails to knock down all ten pins with two balls in a frame. The
score is the number of pins knocked down in that frame.

In the 10th frame, the player may get one or two more bonus ball(s) if a spare or strike
occurs.

# How It Works
-Frames:
Frames and pins stored in player_pins list. For every frames there is two empty string (Except last frame). These are for pins. It use pins function to write pins into the list. It checks invalid values like bigger numbers than 10, negative numbers and for every frame if someone enters more than 10 pins (for example 6 and 7). It also checks knocking ten pins in one shot. When someone knocks all ten pins in one shot it leaves second shot as empty string.

-Last Frame:
Last frame has special situatian. Player could get one or two more shots. To check that it have extra function called lastPins. It checks valid values like pins. But it also checks spare frames and strike frames. It doesn't use any extra functions to check that, it just uses if statements.

-Calculation - 1:
Calculation part is the hardest part. It hard because in every turn program shoul write total scores. So program needs to calculate while program workig. It can't just calculate at the end. Problem in here is while program working when player makes strike or spare it should get scores in next frame. But due to we don't have these pins yet it can't calculate. To solve these I created a empty list called memory. In memory program store these pins when someone makes spare or strike. Also it stores open frame pins (It makes the calculation easier. To store program have three function called: isStrike isSpare isOpen. When any those situations happens they appends their values to memory list.

-Calculation - 2:
Until now we just stored pins in memory. After that we have memoryAdder function to calculate scores. Calculation logic is depends on the length of the memory list. When we called memoryAdder function it firstly checks what kind of frame is currently working on. I uses isStrike, isSpare and isOpen functions to that. While we learn what kind of frame we use also these functions appends to memory list our values and returns. After returned for every frame type we could get specific lengths.
For example in first frame when we hit all ten frames it goes to the isStrike, appends 10 to the memory and returns true. But due we can't afford the length it doesn't makes calculation and continues. In second frame we assume we hit 4 and 3. So it's an open frame. It goes to isOpen, appends 4 and 3 to the memory and checks the length. And it goes to the length == 3 situaation. When enters situations it starts making calculations.
In calculation part it uses pins to calculate and delete these pins. But if program need these datas in the next steps it doesn't delete. For exampla if we have [10],[4, 6] it can calculate first frame but it can't calculate second frame yet. So it just deletes the number 10. [10],[1, 5] in these situation it could calculate both frames. So it does and clears all datas in memory. So basically calculation depends on frame type and lenght.
So how we write these scores? To make that program has to list. First one has empty ten strings (named player_scores) and second one has ten zero's in it (named player_scoresCalc). So whenever a score gets calculated it first goes to player_scoresCalc. After that all datas get sum and get writed to it's specific place in player_score. Note: I used second list (player_scoreCalc) for not to sum all list at one a time instead of one by one. Pragram can't do it in first one because it uses strings.

-Interface:
Easiest part. It has to part one for pins one for total scores. For total scores it needs "|" at the end for every score and after last score it don't need it. So we have a loop it writes scores and then uses "|" and just checks last turn. In last turn it doesn't puts "|". For pins we just write side by side but we should checks strike situation. Because when ever a strike situation happens it makes a space and it looks bad. (For example when it should look like these "5 3 2 8 10 5 4" it shows "5 3 2 8 10  5 4".
