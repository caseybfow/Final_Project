from gametools import write, write_md, get_input, get_choice, clear, pause, spin
import random
import time

game_state = []
balance = 1000
def slot_machine():
    global balance
    if balance <= 0:
        write("You have no money left!!!")
        pause("You have no idea what to do now, Press any key to continue...")
        return broke_balance
    winners = ["🍒","🎲","💰","✨","👑"]
    clear()
    write(
        """
[bold red]WELCOME TO THE SLOT MACHINE[/]
        """
    )
    pause("Press any key to spin the slots...")
    temp = []
    write("SPINNING")
    time.sleep(0.75)
    for i in range(3):
        emoji = random.choice(winners)
        temp.append(emoji)
        write(" | ".join(temp + ["❔"] * (2 - i)))
        time.sleep(0.75)
    clear()
    result = " | ".join(temp)
    write(f"{result}")
    if temp[0] == temp[1] == temp[2]:
        if temp[0] == "🍒":
            tmp = 250*3
            balance = balance *3
        if temp[0] == "🎲":
            tmp = 250*5
            balance = balance *5
        if temp[0] == "💰":
            tmp = 250*10
            balance = balance *10
        if temp[0] == "✨":
            tmp = 250*25
            balance = balance *25
        if temp [0] == "👑":
            tmp = 250*100
            balance = balance *100
        write(f"[bold green]CONGRATULATIONS YOU WON ${tmp}[/]")
        write(f"Your new balance is [green]{balance}[/]")
    else:
        write()
        balance = balance - 250
        write(f"[bold red]Aww you lost $250! Better luck next time[/]")
        write(f"BALANCE: {balance}")
    pause()
    return slots
def show_wallet():
    write(
        f"""
BALANCE: {balance}
        """
    )
def intro():
    write_md(
        """
# YIN WIN CASINO

You have finally arrived to the land of fortune... the CASINO! Its time to go big or 
go home! You have _$1000_ to your name and are looking to either 10x your money or 
go home a millionaire! The opporutunities are endless and you just know you are the 1%
*destined* to win it big!
        """
    )
    write()
    pause("Press any key to begin your gambling [italic]addic-[/] ha I mean [bold italic]ADVENTURE![/]")
    return main_hall

def main_hall():
    write(
        """
You have made your way inside and are in awe with the sheer amount of machines and gambling that is going on 
inside... You head over to the front desk and approach the sketchy looking clerk who couldn't seem to care less
that you just walked in
        """
    )
    write()
    write(
        """
As you walk up to him he notices you and his eyes appear to light up and he greets you with a smile. He then
points you in the direction of 4 different games: [yellow]Poker[/], [red]Roulette[/], [blue]Slots[/], and [purple]Blackjack[/]. Each of these games seem
enticing but remember you only have [bold green]$1000[/] to your name so you vow to only spend [bold green]$250[/]
on every bet
        """
    )
    write()
    pause("Now which game to choose...")
    choices = [
        "Poker",
        "Slots",
        "Blackjack",
        "Roulette",
        "View Wallet"
    ]
    user_choice = get_choice(choices)
    if user_choice == 0:
        return poker
    elif user_choice == 1:
        return slots
    elif user_choice == 2:
        return black_jack
    elif user_choice == 3:
        return roulette
    else:
        write()
        show_wallet()
        write()
        pause()
        return main_hall
def poker():
    write_md(
        """
        """
    )

def slots():
    write_md(
        """
# SLOTS

The way this game works is you simply just pull the lever and pray you get the right combination

- 🍒🍒🍒 = **3x**
- 🎲🎲🎲 = **5x**
- 💰💰💰 = **10x**
- ✨✨✨ = **25x**
- 👑👑👑 = **100x**

You are betting $250 everytime you pull the lever so be careful...
        """
    )
    pause()
    choices = [
        "Go Back",
        "Pull the Lever",
        "Check Wallet"
    ]
    user_choice = get_choice(choices)
    if user_choice == 0:
        return main_hall
    elif user_choice == 1:
        return slot_machine

def black_jack():
    write_md(
        """
        """
    )

def roulette():
    write_md(
        """
        """
    )
def broke_balance():
    write_md(
        """
You officially have lost all of your money... NOW WHAT! You were promised riches not rags!
Angry you begin throwing a tantrum until you notice that there is a large pile of cash just
about 30 yards in front of you...

You really need the money but there appears to be around 10 guards surrounding it... you 
could cause a distraction to get them away from the money or you could just try and brute
force it and grab it then run for your life. What to do...
        """
    )
    pause()
    choices = [
        "Cause a distraction",
        "Force your Way",
        "Cut your losses and go home",
        "Check Wallet",
    ]
    user_choice = get_choice(choices)
    if user_choice == 0:
        return ending_1
    elif user_choice == 1:
        return ending_2
    elif user_choice == 2:
        return ending_3
    else:
        write()
        show_wallet()
        write()
        pause()
        return broke_balance
def ending_1():
    write_md(
        """
        """
    )
def ending_2():
    write_md(
        """
        """
    )
def ending_3():
    write_md(
        """
        """
    )
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
