import pyautogui, time, sys

"""
Only tryed on Rebirth, Windows
[!]Doesn't see upper treasure room(probably because of the floor' name)
[!]Works only on Isaac, every other character either too slow or too fast, but they able to take item on lower treasure room
ToDo list:
    Add every character as object of class with different parameters
"""

delay = 3
character = "Azazel"
item_list = ["Mom's Knife", "Magic Mushroom", "Cricket's Head", "Proptosis", "20/20"]
if character == "Isaac":
    item_list.append("Polyphemus")
    item_list.append("Death's Touch")
elif character == "Azazel":
    item_list.append("The Ludovico Technique")
    item_list.append("Tiny Planet")

def restart_run():
    pyautogui.keyDown('r')
    time.sleep(1)
    pyautogui.keyUp('r')

def is_treasure_room():
    """
    Returns direction if there is treasure room
    """
    for direction in ["up", "down", "left", "right"]:
        try:
            pyautogui.locateOnScreen("treasure_room_%s.png" % direction, confidence=.8)
            return direction
        except:
            pass
    return False

def go(character, direction):
    # params = {"up": ["w", 1], "down": ["s", .5], "side": ["w", .35], "left": ["a", 1], "right": ["d", 1]}
    correction = 0
    if character == "Azazel":
        correction = -0.2

    if direction == "down":
        pyautogui.keyDown("s")
        time.sleep(1.5)
        pyautogui.keyUp("s")
    elif direction == "up":
        pyautogui.keyDown("w")
        time.sleep(2.3)
        pyautogui.keyUp("w")
    else:
        pyautogui.keyDown("w")
        time.sleep(.35)
        pyautogui.keyUp("w")
        if direction == "left":
            pyautogui.keyDown("a")
            time.sleep(1.4)
            pyautogui.keyUp("a")
            pyautogui.keyDown("s")
            time.sleep(.2)
            pyautogui.keyUp("s")
            pyautogui.keyDown("a")
            time.sleep(.8+correction)
            # time.sleep(.6)
            pyautogui.keyUp("a")
            pyautogui.keyDown("w")
            time.sleep(.4)
            pyautogui.keyUp("w")
        elif direction == "right":
            pyautogui.keyDown("d")
            time.sleep(1.4)
            pyautogui.keyUp("d")
            pyautogui.keyDown("s")
            time.sleep(.2)
            pyautogui.keyUp("s")
            pyautogui.keyDown("d")
            time.sleep(.8+correction)
            # time.sleep(.6)
            pyautogui.keyUp("d")
            pyautogui.keyDown("w")
            time.sleep(.4)
            pyautogui.keyUp("w")

"""
Down - good 3/3
Up - good 2/2
"""
# time.sleep(delay)
# go("Azazel", "right")

def is_items():
    """
    Returns list of items for current run
    """
    log_file = open(u"C:\\Users\\Slope\\Documents\\My Games\\Binding of Isaac Rebirth/log.txt", "r")
    lines = list()
    for line in log_file.readlines():
        if "RNG Start Seed" in line:
            lines = list()
        if line not in lines and "Adding collectible" in line:
            lines.append(line.split("(")[1].split(")")[0])
            # print(line)
    log_file.close()
    return set(lines)

def main():
    time.sleep(delay)
    finding_treasure_room = True
    finding_good_run = True
    while finding_good_run:
        while finding_treasure_room:
            restart_run()
            # time.sleep(3.5)  # Waiting for floor's name to dissapear
            time.sleep(1)  # Waiting for animation
            print("finding room")
            direction = is_treasure_room()
            if direction:
                print(direction)
                # time.sleep(.5)
                go(character, direction)
                finding_treasure_room = False
        time.sleep(1.3)
        current_items = is_items()
        print(current_items)
        if current_items.intersection(set(item_list)):
            finding_good_run = False
        else:
            finding_treasure_room = True
    pyautogui.keyDown('esc')

main()

# def main():
#     time.sleep(delay)
#     while True:
#         direction = is_treasure_room()
#         if direction:  # If there is a treasure room
#             go(direction)  # Go to the treasure room
#             if is_item():  # Checking for items
#                 pyautogui.keyDown('esc')
#                 exit()
#         else:
#             restart_run()
        # while not is_treasure_room():
        #     restart_run()
        # direction = is_treasure_room()
        # go(direction)
        # time.sleep(1)
        # if is_item():r
        #     pyautogui.keyDown('esc')
        #     exit()
        # else:
        #     restart_run()


# go("left")
# go("right")
# if is_item():
#     print("good")
#     pyautogui.keyDown('esc')
# time.sleep(delay)
# item = pyautogui.locateOnScreen("Mom's Knife.png", confidence=.8)
# x, y = pyautogui.center(item)
# pyautogui.moveTo(x, y)
# go("down")
# print(is_treasure_room())
# time.sleep(delay)
# go("left")
# main()

# if __name__ == "__main__":
#     main()
