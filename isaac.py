import pyautogui, time, os
from win32gui import GetWindowText, GetForegroundWindow

"""
Only tryed on Rebirth, Windows
[!]Doesn't see upper treasure room(probably because of the floor' name)
[!]Works only on Isaac, every other character either too slow or too fast, but they able to take item on lower treasure room

ToDo list:
    Add every character as object of class with different parameters
"""

delay = 5
character = "Azazel"
item_list = ["Mom's Knife", "Magic Mushroom", "Cricket's Head", "Proptosis", "20/20", "Tech X", "Epic Fetus"]
# item_list = ["Tech X"]  # OP for Afterbirth

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

def go(direction):
    correction = 0
    # if character == "Azazel":
    #     correction = -0.2
    params = {  "up": {"key": "w", "to": 1.2, "in": .8}, \
                "down": {"key": "s", "to": .2, "in": .8}, \
                "center": {"key": "w", "to": .3}, \
                "left": {"key": "a", "to": 1.4, "in": .8}, \
                "right": {"key": "d", "to": 1.4, "in": .8}, \
                "evade": {"key": "s", "in": .2}, \
                "take_item": {"key": "w", "in": .2}}

    # Going to the room
    if direction in ["left", "right"]:
        pyautogui.keyDown(params["center"]["key"])
        time.sleep(params["center"]["to"])
        pyautogui.keyUp(params["center"]["key"])
    pyautogui.keyDown(params[direction]["key"])
    time.sleep(params[direction]["to"])
    pyautogui.keyUp(params[direction]["key"])

    # Going in the room
    time.sleep(.3)
    room_type = get_from_log()["room_type"]
    if room_type == "4.12":
        return None
    print("Room Type: %s" % room_type)
    if direction in ["up", "down"]:
        pyautogui.keyDown(params[direction]["key"])
        time.sleep(params[direction]["in"])
        pyautogui.keyUp(params[direction]["key"])
        if direction == "down":
            if room_type in ["4.11", "4.27"]:
                pyautogui.keyDown("d")
                time.sleep(.1)
                pyautogui.keyUp("d")

                pyautogui.keyDown("w")
                time.sleep(.4)
                pyautogui.keyUp("w")

                # Maybe go to the left (for 4.11(two items close to each other)), but need to correct upper command
            elif room_type == "4.16":
                return None
    else:
        if room_type != "4.26":
            pyautogui.keyDown(params["evade"]["key"])
            time.sleep(params["evade"]["in"])
            pyautogui.keyUp(params["evade"]["key"])

        pyautogui.keyDown(params[direction]["key"])
        time.sleep(params[direction]["in"])
        pyautogui.keyUp(params[direction]["key"])

        pyautogui.keyDown(params["take_item"]["key"])
        time.sleep(params["take_item"]["in"])
        pyautogui.keyUp(params["take_item"]["key"])

        # For 4.27
        pyautogui.keyDown("d")
        time.sleep(.1)
        pyautogui.keyUp("d")

def get_from_log():
    """
    Returns list of items for current run
    """
    log_file = open(u"C:\\Users\\Slope\\Documents\\My Games\\Binding of Isaac Afterbirth/log.txt", "r")
    items = list()
    room_type = str()
    for line in log_file.readlines():
        if "RNG Start Seed" in line:
            items = list()
        elif "Room" in line:
            room_type = line.split()[1].split("(")[0]
        elif line not in items and "Adding collectible" in line:
            items.append(line.split("(")[1].split(")")[0])
            # print(line)
    log_file.close()
    return {"items": set(items), "room_type": room_type}

def main():
    os.system('mode con: lines=25')

    time.sleep(delay)
    app_name = "Binding of Isaac: Afterbirth"
    if GetWindowText(GetForegroundWindow()) != app_name:
        print("Switch to Isaac")
    finding_treasure_room = True
    finding_good_run = True
    number_of_runs = 1
    while finding_good_run:
        while finding_treasure_room:
            restart_run()
            # time.sleep(3.5)  # Waiting for floor's name to dissapear
            time.sleep(1)  # Waiting for animation
            print("[Run #%s] Finding room" % number_of_runs)
            direction = is_treasure_room()
            if direction:
                print("Found. Going %s" % direction)
                # time.sleep(.5)
                go(direction)
                finding_treasure_room = False
            else:
                print("Nope\n")
                number_of_runs += 1
        time.sleep(1.3)
        current_items = get_from_log()["items"]
        print("%s\n" % current_items)
        if current_items.intersection(set(item_list)):
            finding_good_run = False
        else:
            finding_treasure_room = True
        number_of_runs += 1

    pyautogui.keyDown('esc')

main()
# time.sleep(2)
# go("left")

# if __name__ == "__main__":
#     main()
