print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
choice_01 = input('You are at a cross road.Where do you want to go? left or right?\n')
if choice_01.lower() == "left":
    choice_02 = input("You came to a lake.There is an island in the lake.Do you choose to swim or wait?\n")
    if choice_02.lower() == "wait":
        choice_03 = input("You have arrived at the island safe.There is a house with 3 doors.which door you want to go? Red, Blue or Yellow\n")
        if choice_03.lower() == "yellow":
            print("You Win!")
        elif choice_03.lower() == "Blue":
            print("Eaten by Beasts and Game Over!")
        elif choice_03.lower() == "Red":
            print("Burned by fire and Game Over!")
        else:
            print("Game Over!")
    else:
        print("Attacked by a trout and Game Over!")
else:
    print("Fall into a hole and Game Over!")
