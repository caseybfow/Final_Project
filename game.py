from gametools import write, write_md, get_input, get_choice, clear, pause, spin
import random
import time

balance = 1000
cont = False
iterationCount = 0
def slot_machine():
    global balance, cont
    if balance >= 10000 and cont == False:
        write_md(
            f"""
*WOW* you sure have won alot of money! In fact you have ${balance} to your name right now!
That's more than what I came here for so do you want to keep playing or enjoy your winnings
while you have them?
            """
        )
        choices = [
            "Continue to Play",
            "Its time to go Home"
        ]
        user_choice = get_choice(choices)
        if user_choice == 0:
            cont = True
            return main_hall
        elif user_choice == 1:
            return happy_ending    
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
    write()
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
            balance = balance + tmp
        if temp[0] == "🎲":
            tmp = 250*5
            balance = balance + tmp
        if temp[0] == "💰":
            tmp = 250*10
            balance = balance + tmp
        if temp[0] == "✨":
            tmp = 250*25
            balance = balance + tmp
        if temp [0] == "👑":
            tmp = 250*100
            balance = balance + tmp
        write(f"[bold green]CONGRATULATIONS YOU WON ${tmp}[/]")
        write(f"Your new balance is [green]{balance}[/]")
    else:
        write()
        balance = balance - 250
        write(f"[bold red]Aww you lost $250! Better luck next time[/]")
        write(f"BALANCE: {balance}")
    write()
    choices = [
        "Play Again",
        "Return to Main Hall"
    ]
    user_choice = get_choice(choices)
    if user_choice == 0:
        return slots
    elif user_choice == 1:
        return main_hall
   
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
    global balance, iterationCount, cont
    iterationCount += 1
    if balance >= 10000 and cont == False:
        write_md(
            f"""
*WOW* you sure have won alot of money! In fact you have ${balance} to your name right now!
That's more than what I came here for so do you want to keep playing or enjoy your winnings
while you have them?
            """
        )
        choices = [
            "Continue to Play",
            "Its time to go Home"
        ]
        user_choice = get_choice(choices)
        if user_choice == 0:
            cont = True
            return main_hall
        elif user_choice == 1:
            return happy_ending    
    if balance <= 0:
        write("You have no money left!!!")
        pause("You have no idea what to do now, Press any key to continue...")
        return broke_balance
    clear()
    if iterationCount <= 1:
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
    write(f"[bold]Balance:[/] [green bold]${balance}[/]")
    pause("Press any key to choose a game...")
    choices = [
        "Poker",
        "Slots",
        "Blackjack",
        "Roulette",
        "View Wallet",
        "Go Home (End Game)"
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
    elif user_choice == 4:
        write()
        show_wallet()
        write()
        pause()
        return main_hall
    else:
        return home
def poker():
    global balance
    if balance <= 0:
        return broke_balance
    clear()
    write_md(
        """
# 🃏 POKER 🃏
You walk over to the poker table and take your seat waiting for the dealer to 
deal you your cards. You give your **$250** to the pot and in turn you get your
hand.

You have really no idea how poker works so this has now become a *game of balls*.
Do you bluff your hand to scare away these posers or do you take your place in 
the hierachy and fold like a baby.
        """
    )
    write()
    pause()
    choices = [
        "Bluff",
        "Fold",
        "GO ALL IN",
    ]
    user_choice = get_choice(choices)
    if user_choice == 0:
        return bluff
    elif user_choice == 1:
        return fold
    elif user_choice == 2:
        return All_In
def bluff():
    global balance
    num1 = random.randint(1,7)
    num2 = random.randint(1,7)
    write_md(
        """
You decide to bluff because you have no real idea what your doing but you know
fake it till you make it right? Anyways you see everyone around you seems to have 
the same idea as you so everyone is in on this now...

You all await the dealer to deal the remainder of the cards eagerly and nobody
raised the pot so it is just a light *$2000* up for grabs
        """
    )
    pause("Press any key to reveal the results...")
    if num1 == num2:
        balance = balance + 2000
        write_md(
            f"""
# YOU 👑 WON 👑

Somehow despite not knowing at all what you are doing you managed to have a better hand 
than the rest of the particpants in the game! Congratulations! You have won *$2000* and 
your new balance is now **${balance}** 
            """
        )
        pause()
        choices = [
            "Play again",
            "Go Back to Hall",
            "Check Wallet"
        ]
        user_choice = get_choice(choices)
        if user_choice == 0:
            return poker
        elif user_choice == 1:
            return main_hall
        elif user_choice == 2:
            return show_wallet
    elif not(num1 == num2):
        balance = balance -250
        write_md(
            f"""
# YOU ❌ LOST ❌

Aww man it turns out this poker stuff is harder than it looks and you just managed to blow $250
just like that, well your new balance is **{balance}**. Better luck next time!
            """
        )
        write()
        pause()
        choices = [
            "Play again",
            "Go Back to Hall",
            "Check Wallet"
        ]
        user_choice = get_choice(choices)
        if user_choice == 0:
            return poker
        elif user_choice == 1:
            return main_hall
        elif user_choice == 2:
            return show_wallet

def fold():
    global balance
    balance = balance -250
    write_md(
        f"""
Well you can't really get any lamer than that man, you lost **$250** and
your pride alongside that. Now your remaining balance is {balance}

You walk back to the main hall in shame of your loss but at least you still
have some money to your name...
        """
    )
    write()
    pause("Press any key to go back to the Main Hall...")
    return main_hall
def All_In():
    global balance
    num1 = random.randint(1,2)
    num2 = random.randint(1,2)
    write_md(
        """
You decide to go ALL IN no going back now, you eagerly wait for the dealer to 
set down the remaining cards but before he can do that 2 of the other players 
fold but 1 decides to call your All In play. 

Its just you two waiting for the dealer to decide the fate of the game,
        """
    )
    write()
    pause("Press any key to find out if your risk was worth it...")
    if num1 == num2:
        balance = balance + 10000
        write()
        write_md(
            f"""
# ITS A 🃏👑 ROYAL FLUSH 👑🃏

You have now won all the money on the table which adds up to about *$10,000*!
Now that you have the money you came for you can either test your luck playing
more games or just simply take your winnings and go HOME!

Your new BALANCE: {balance}
            """
        )
        write()
        pause("Press any key to decide what to do next...")
        choices = [
            "Go Home",
            "Continue to Gamble",
        ]
        user_choice = get_choice(choices)
        if user_choice == 0:
            return happy_ending
        elif user_choice == 1:
            return main_hall
    elif not(num1 == num2):
        balance = 0
        clear()
        write_md(
            """
# ❌❌❌ YOU LOST ❌❌❌

Your risk did not pay off and your hand was a bust, now you lost all your money
and have nothing to show for it, you walk away in shame.
            """
        )
        write()
        pause()
        return broke_balance
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
    write()
    pause()
    choices = [
        "Go Back",
        "Pull the Lever",
    ]
    user_choice = get_choice(choices)
    if user_choice == 0:
        return main_hall
    elif user_choice == 1:
        return slot_machine
def blackjack_game():
    global balance
    if balance <= 0:
        return broke_balance
    card = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    values = {
        '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11, '18': 18, '19': 19, '20': 20, '21': 21
    }
    hand = [random.choice(card), random.choice(card)]
    handvalue = sum(values[card] for card in hand)
    choices = [
        "Hit",
        "Stand"
    ]
    cond = True
    while cond == True:
        write(f"Your hand: {hand} -> {handvalue}")
        if handvalue > 21:
            write("You went over 21! [bold red]BUST[/]")
            break
        user_choice = get_choice(choices)
        if user_choice == 0:
            newcard = random.choice(card)
            hand.append(newcard)
            handvalue = handvalue + values[newcard]
        elif user_choice == 1:
            cond = False
    dealer_hand = ["18", "19","20","21"]
    dealer = random.choice(dealer_hand)
    dealer_value = values[dealer]
    write(f"The Dealer's hand had a value of: {dealer_value}")
    if dealer_value > handvalue or handvalue > 21:
        balance = balance -250
        write_md(
            """
# ❌ YOU LOSE ❌

Better luck next time!
            """
        )
        write()
        pause("Press any key to go back to the main hall...")
        return main_hall
    elif dealer_value < handvalue and not(handvalue > 21):
        balance = balance + 250
        write_md(
            """
#  ✨ YOU WON ✨

Nice Job! You have won $250 from this game!
            """
        )
        write()
        pause("Press any key to go back to the main hall...")
        return main_hall
    if dealer_value == handvalue:
        write_md(
            """
# ➖ DRAW ➖

You both had the same value hand so therefore no one wins and you keep your money!
            """
        )
        write()
        pause("Press any key to return to the main hall...")
        return main_hall
def black_jack():
    global balance
    if balance <= 0:
        return broke_balance
    write_md(
        """
# 🃏♦️ BLACKJACK ♦️🃏

This game is simple you will be given two cards from a standard deck which will then add up to a number
and then based on the number you get at the start you can either hit or stand with the goal of trying to 
get as close to **21** as possible.

However, this game is heavily favored in the dealers way so by playing this you are putting yourself
at a hefty disadvantage so be careful how many times you end up betting here. 
        """
    )
    write()
    pause("Press any key to play the game")
    return blackjack_game

def roulette_game():
    global balance
    choices = [
        "Red 🟥",
        "Black ⬛",
        "Go Back",
    ]
    user_choice = get_choice(choices)
    if user_choice == 0:
        color = ['⬛','⬛','⬛','🟥']
        pickcolor = random.choice(color)
        if pickcolor == '🟥':
            write()
            write("You picked 🟥 and the wheel landed on 🟥")
            write()
            pause()
            balance = balance + balance
            write_md(
                f"""
# 💰 YOU WIN 💰

Congratulations! Despite the seemingly rigged game you managed to win and doubled your money!
You now feel a rush of happiness cause you were able to overcome the scammers at this casino.

New Balance: **{balance}**
                """
            )
            write()
            pause("Press any key to return to the main hall...")
            return main_hall
        elif pickcolor == '⬛':
            write()
            write("You picked 🟥 and the wheel landed on ⬛")
            write()
            pause()
            balance = balance -250
            write_md(
                f"""
# ❌ YOU LOSE ❌

Aww man you thought this was a fair game but it kind of looks like its rigged now :/
Welp theres always next time and maybe you will really win it big just remember dont
*ever QUIT!*

New Balance: **{balance}**
                """
            )
            write()
            pause("Press any key to return to the main hall...")
            return main_hall
    elif user_choice == 1:
        color = ['🟥','🟥','🟥','⬛']
        pickcolor = random.choice(color)
        if pickcolor == '⬛':
             write()
             write("You picked ⬛ and the wheel landed on ⬛")
             write()
             pause()
             balance = balance + balance
             write_md(
                f"""
# 💰 YOU WIN 💰

Congratulations! Despite the seemingly rigged game you managed to win and doubled your money!
You now feel a rush of happiness cause you were able to overcome the scammers at this casino.

New Balance: **{balance}**
                """
            )
             write()
             pause("Press any key to return to the main hall...")
             return main_hall
        elif pickcolor == '🟥':
            write()
            write("You picked ⬛ and the wheel landed on 🟥")
            write()
            pause()
            balance = balance -250
            write_md(
                f"""
# ❌ YOU LOSE ❌

Aww man you thought this was a fair game but it kind of looks like its rigged now :/
Welp theres always next time and maybe you will really win it big just remember dont
*ever QUIT!*

New Balance: **{balance}**
                """
            )
            write()
            pause("Press any key to return to the main hall...")
            return main_hall
    elif user_choice == 2:
        return main_hall

def roulette():
    global balance
    if balance <= 0:
        return broke_balance
    write_md(
        """
# 🔴⚫ ROULETTE ⚫🔴

This is the game called **Roulette* and it is very simple just pick a color red or black!
All you have to do is choose one its a 50/50 shot! Right? Well I sure hope so lets just get
this over with
        """
    )
    write()
    pause("Press any key to choose a color...")
    return roulette_game
    
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
    write()
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
        write("Why are you even checking here theres [bold italic]NOTHING LEFT![/]")
        show_wallet()
        write()
        pause()
        return broke_balance
def ending_1():
    write(
        """
You notice an empty liquor bottle just to your left and think to throw it in the direction
of a poker table to get securities attention,
        """
    )
    write()
    write(
        """
You go to grab the bottle and it reads [bold red]'DO NOT CONSUME'[/] huh must be an edgy brand label for 
die hard drinkers, anyways you dont think much of it and get ready to throw it into the crowd
of gamblers to lure the guards away from the [bold green]$Money$[/]
        """
    )
    write()
    pause("Press any key to throw the BOTTLE...")
    write(
        """
You throw the bottle over towards the gamblers and it hits a guy whos about to light a cigar in his hand
the liquid gets everywhere and out of no where flames erupt all around him and the table! [bold #FFA500]ITS A FIRE![/]
        """
    )
    write()
    write(
        """
It begins to spread quickly and you now realize that you ****** up big time! No need to try and get any money
anymore you just need to secure your freedom and bolt out of there as quickly as you can hoping nobody got wind 
that *you* were the one who threw the bottle...
        """
    )
    write()
    write(
        """
You arrive home late at night as you wanted to make sure nobody was able to trail you and after a long day of gambling
and unfortunately no winning you decide to call it a night and consider some new hobbies cause theres no way you are returning
to that casino anytime soon...
        """
    )
    write()
    write(
        """
[bold #FFA500]GAME OVER! YOU CAUSED HAVOC AND WON NOTHING[/]
        """
    )
    exit()
def ending_2():
    balance = random.randint(1000,100000)
    write_md(
        """
You **CHARGE** towards the guards with no regrets in sight! The first two dive for your legs but you
hurdle them making them crash into somebodies slot machine knocking them out! You inch closer and closer
but as you do the guards keep coming

Two more are on your left and three are on your right you decide to zip past them all and try to grab as 
much money as possible while they all knock into each other dazzing one another! As you are grabbing the cash
you realize the guards are back on their feet and it might be time to dip now!
        """
    )
    write()
    pause("Press any key to see what happens next...")
    write_md(
        """
You start running for your life towards the exit but now **ALARMS** are sounding and metal doors appear before the 
exit slowly inching closer to closing! This isnt good you begin to sprint as fast as you can with the guards hot on 
your trail! The door is *ALMOST* closed you HAVE to slide to make it!

You slide and the door *SLAMS* shut leaving the guards on the other side and some of the money you took alongside them!
**FREEDOM** you dart home as soon as possible to count your winnings from the casino!
        """
    )
    write_md(
        """
# 🏠 HOME
        """
    )
    write(
        f"""
Congratulations! You managed to scam the casino more than they could scam you! After counting the money you
[bold italic]won[/] you realize you managed to get a [bold]GRAND TOTAL[/] of [green]{balance:,}[/]!
        """
    )
    write(
        """
[bold green]THANKS FOR PLAYING![/]
        """
    )
    exit()
def ending_3():
    write_md(
        """
# 🏠HOME

You arrive back at your house empty handed with nothing to show for your efforts,
your wife is yelling at you and the kids are hungry. You just plop down in your 
trusty chair and begin to drift off into you dreams hoping to win it big some day

However, you vow to **NEVER** quit gambling because you *ARE* the **1%**
        """
    )
    write()
    write("[bold red]GAME OVER YOU WON NOTHING[/]")
    exit()
def happy_ending():
    global balance
    write_md(
        f"""
# 💰✨ CONGRATULATIONS 💰✨

You have won it big taking home a total of **${balance}**!
Now what to do with all this money... Well that's for you to 
decide!

Thanks for playing!
        """
    )
    exit()
def home():
    global balance
    write_md(
        """
# 🏠 HOME """)
    write(
        f"""
Well you decided to go home and keep the money you managed to make or just decided to cut your
losses and at least be able to feed the kids, You came home with a grand total of [green]{balance}[/green]
so dont feel so bad about yourself!

[red]GAME OVER![/red] Thanks for playing!
        """
    )
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
