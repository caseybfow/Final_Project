from gametools import write, write_md, get_input, get_choice, clear, pause, spin

game_state = []
inventory = []


################################################################################
# SHOW_INVENTORY
#   TODO: fix this function

def show_inventory():
    # Modify this to print inventory as a bulleted list using hyphens for
    # bullets. You should first print a "title" line ("PLAYER INVENTORY")
    # followed by lines displaying each item in the inventory. Each line should
    # be prefixed with " - " (space dash space). If no items are in the
    # inventory then display "*** EMPTY ***". For example:
    # 
    # PLAYER INVENTORY
    # 
    #  - Spear
    #  - Magic Helmet
    # 
    # PLAYER INVENTORY
    # 
    # *** EMPTY ***
    # 
    # Although gametools.write() has a way to help with this, please just use
    # print() for this assignment instead.
    # 
    print(inventory)


################################################################################
# INTRO
#   Nothing do do here

def intro():
    clear()
    write_md(
"""
# DUNGEON OF BOB

Dear player, I fear that you have found yourself in quite a predicament. You
have been captured by the evil Dragon _Bob_. _Bob_ intends to **_eat_** you in
just a few days. So, now is the time to pull yourself together and find a way to
escape.
"""
    )
    write()     # just a blank line to make things look better  
    pause("Press any key to get off of your (soon to be tasty) rump and get out of here")
    return cell


################################################################################
# CELL
#   Nothing to do here, but a lot to understand, so read through the code and
#   comments carefully.

def cell():
    clear()

    # This part of the scene is the same whenever we enter. However, the rest of
    # the scene changes depending on game_state and inventory.
    write_md(
"""
# YOUR DANK CELL

You are currently in your prison cell in this dank horrid dungeon that smells
oddly like burnt peanut butter.
"""
    )
    write()
    
    # Here we "examine" the game state list to see if the player has done
    # something yet. This will determine how the scene is displayed.

    if not "torch_lit" in game_state:
        write_md(
"""
This place is dark as heck. There's no way to do anything until you are able to
see.

Fortunately (and inexplicably), it appears that _Bob_ supplied you with a torch
and a fancy propane cigar lighter. How does a cigar lighter end up in a dungeon
cell in a fantasy world that is modeled after the early middle ages? Suspension
of disbelief, folks. Turn off your rational brain...right now.
"""
        )
        write()
        write("What would you like to do?")
        choices = [
            "Light the torch the with cigar lighter",
            "Cry out in hopeless agony",
            "Examine your inventory"
        ]
        user_choice = get_choice(choices)
        if user_choice == 0:
            # Here we add a specific value to the game_state list. We can then
            # check to see if this value exists in the list...which we are
            # already doing above. In other words, we modify state here so that
            # the NEXT time the function is called, things will be different.

            game_state.append("torch_lit")

            write()
            write("You wisely choose to light your torch.")
            write()
            pause()   # pause here so the player can read what was written before returning.
            return cell

        elif user_choice == 1:
            write()
            write("I hope that made you feel better. Unfortunately it did no good whatsoever.")
            write()
            pause()   # pause here so the player can read what was written before returning.
            return cell

        else:
            write()
            show_inventory()
            write()
            pause()
            return cell

    else:       # "torch_lit" *IS* in game_state

        # This is the alternative way of showing the scene once the torch is
        # lit.
        write_md(
"""
The room is well lit thanks to your torch. It appears that _Bob_ has forgotten
to close your cell door. Whaaaat??!? Is it really going to be this easy?

The cell door is to the South.
"""
        )
        write()
        write("What will you do?")
        choices = [
            "Go South through the cell door",
            "Examine your inventory"
        ]
        user_choice = get_choice(choices)
        if user_choice == 0:
            return hall
        else:
            write()
            show_inventory()
            write()
            pause()
            return cell


################################################################################
# HALL
#   Same as above. Nothing to do but a lot of "understanding" to be gained.

def hall():
    clear()

    # Here we check game_state and inventory and set local variables to allow us
    # to easily control the way the room is displayed.

    if "door_open" in game_state:
        door_open = True
        door_state = "open"
    else:
        door_open = False
        door_state = "closed"

    if "Cell Block Key" in inventory:
        has_key = True
    else:
        has_key = False

    # NOTE: I'm using an f-string here...it allows me to _slightly_ modify the
    # narrative without introducing more branching logic.

    write_md(
f"""
# CELL BLOCK HALLWAY

You are in a hallway that connects a lot of other dungeon cells. The doors to
each of the other cells are locked. You're sure it would be interesting to
explore them, but you just can't be bothered right now given your impending
visit to _Bob's_ belly.

You can go North to return to your cell. To the East you see a door that appears
to be {door_state}.
"""
    )
    write()
    if not has_key:
        write_md(
"""
Dangling from the neck of a lightly grilled and heavily dead dungeon guard, you
see a key.
"""
        )

    choices = [
        "Go North",
        "Go East",
        "Take Key",
        "View Inventory"
    ]

    # Once you have the key, then the third option should no longer be
    # displayed. You can pass a list of indexes to get_choice() that will hide
    # specific choices from the player.

    hidden_choices = []
    if has_key:
        hidden_choices.append(2)    # 2 is the index of the "Take Key" choices

    # Now call get_choice with the optional second argument.

    user_choice = get_choice(choices, hidden_choices)
    if user_choice == 0:            # North
        return cell

    elif user_choice == 1:          # East
        if door_open:
            # If the door has already been opened, you just step through it
            return bobs_lair
        else:
            # If the door hasn't been opened yet, then if we have the key we can
            # open it. Note that adding the door_open state here _ONLY_ affects
            # the scene if we return to this room after visiting Bob. But little
            # details like this can really make or break players' experiences.
            if has_key:
                game_state.append("door_open")
                write()
                write("You use the key to unlock the door and open it.")
                write()
                pause("Press any key to step through the open door")
                return bobs_lair

            # But if we don't have the key, we can't leave
            else:
                write()
                write("The door appears to be locked. Hmm. Maybe that key on that roasted guard may help.")
                write()
                pause()
                return hall

    elif user_choice == 2:          # Take Key
        inventory.append("Cell Block Key")
        write()
        write(
"""
You gently remove the key from the guard's neck. Apparently not gently enough as
his head tumbles to the floor and rolls across the hall making disgusting
"shplurp, shplurp, thunk" sounds.
"""
        )
        write()
        pause()
        return hall

    else:                           # View Inventory
        write()
        show_inventory()
        write()
        pause()
        return hall


################################################################################
# BOBS_LAIR
# 
#   TODO:
#     * Complete the if/elif/else logic to properly handle the user_choice.

def bobs_lair():
    clear()
    write_md(
"""
# _BOB'S_ LAIR

You are standing in the main chamber of _Bob's_ lair. _Bob_ is laying atop a
large mound of gold coins and cigar lighters, snoring loudly. Around his neck is
what appears to be a garage door opener. Huh? Whatever, clearly you need to kill
_Bob_ in order to retrieve that garage door opener and escape.

You're confident you can sneak up on _Bob_ and attack him while he sleeps. But
are you ready to do this?

You can also go back West to the cell block hallway. There's another open door
to the East that appears perhaps to be the guards' armory. And to the South is
an enormous, industrial-sized garage door that is closed.

What would you like to do?
"""
    )
    choices = [
        "Go West",
        "Go East",
        "Go South",
        "Attack Bob",
        "View Inventory"
    ]
    user_choice = get_choice(choices)

    # TODO: write the logic below to navigate to the right scene based on the
    # user_choice index value. Add elif blocks as needed.
    # 
    # 0: West takes you back to the hall.
    # 
    # 1: East takes you to the armory.
    # 
    # 2; Going South is simply not possible. You will stay in bobs_lair, though
    # do display a message to the user letting them know that the way is blocked
    # and don't forget to pause so they can read it.
    # 
    # 3: Attacking Bob, well that's the attack_bob scene.
    # 
    if user_choice == 0:
        ...
    else:
        write()
        show_inventory()
        write()
        pause()
        return bobs_lair


################################################################################
# ARMORY
# 
#   TODO: (use the code in `hall()` for inspiration)
# 
#     * Hide the description of the rusty spear if the player already has it
#     * Hide the choice to take the spear if the player already has it
#     * Add "Rusty Spear" to the inventory if the player takes it
#     * Display a message indicating that the player has taken the spear

def armory():
    clear()

    if "Rusty Spear" in inventory:
        has_spear = True
    else:
        has_spear = False

    write_md(
"""
# GUARDS' ARMORY

Apparently Bob didn't always just roast his cell guards. He at least at one time
armed them. There are a lot of useless broken weapons and armor scattered all
over and covered in cobwebs.
"""
    )
    
    # TODO: This should only be displayed if the player has not yet picked up the spear
    write()
    write("There appears to be one rusty old spear that might still be usable as a weapon.")
    
    write()
    write("What do you want to do?")

    choices = [
        "Go West back to Bob's Lair",
        "Pick up the Rusty Spear",
        "View Inventory"
    ]
    hidden_choices = []
    # TODO: "hide" the choice to take the spear if the player already has it

    user_choice = get_choice(choices, hidden_choices)
    if user_choice == 0:        # West
        return bobs_lair

    elif user_choice == 1:      # Take Spear
        # TODO:
        #   1. add "Rusty Spear" to inventory
        #   2. display a message indicating that the player picked up the spear
        #      and pause before returning

        return armory

    else:                       # View Inventory
        write()
        show_inventory()
        write()
        pause()
        return armory


################################################################################
# ATTACK_BOB
# 
#   TODO: This one is entirely on you.
# 
#   If you attack Bob and you do not have "Rusty Spear" in your inventory, then
#   you will die. The (hopefully creative) narrative describing this outcome is
#   entirely up to you.
# 
#   If you do have the "Rusty Spear" than you manage to kill Bob, take the
#   garage door opener, and open the door allowing you to escape. Again, this
#   narrative is totally up to you.
# 
#   This is end game. Both paths simply exit(), so nothing to return here. 

def attack_bob():
    exit()


################################################################################
# The main game loop. Look but don't touch!!

def game_loop():
    scene = intro
    while True:
        next_scene = scene()
        if callable(next_scene):
            scene = next_scene
        else:
            print("SILLY CODE ERROR")
            print("It appears you returned something other than a function from one of your scene functions.")
            exit()


if __name__ == "__main__":
    game_loop()
