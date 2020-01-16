print("You enter a dark room with three floors, such a bore.")
print("1. floor 1")
print("2. floor 2")
print("3. floor 3")
print("Note, only floor one has anything in it right now. The others will come in the dlc")

floor = input("-~-~-~> ")
steak = 0
if floor == "1":
    print("You see a giant cake eating a steak")
    print("what do you do not do?")
    print("1. Take the steak, eat the cake")
    print("2. Make loud noises, while hearing voices")
    print("Or choose your own adventure and don't be a corporate zombie")

    cake = input("-~-~-~> ")

    if cake == "2":
        print("The cake flops on you and you die from insanity. Good Job!")
    elif cake == "1":
        print("You become a normal american.")
        print("Gain key item, steak")
        print("You continue on, through winding passages and slowly become hungry")
        print("1. Eat the steak")
        print("2. Keep going")

        eat = input("-~-~-~> ")

        steak = 1

        if steak == 0:
            print("""Somehow you broke the game. Good job, you're now being digested
             in the bowels of the zachulu. Please report this bug and we will get
             todd howard to spend a few years hyping it's sixteen times fix.""")

        elif steak == 1 and eat == "1":
            print("You feel reinvigorted and keep going")
            print("You see a small cave up ahead, with staglites and stlagmites conviently forming a mouth")
            print("1. Go into the cave")
            print("2. Continue on")

            cave = input("-~-~-~> ")

            if cave == "1":
                print("You poke yourself on one of the 'teeth' and begin bleeding out.")
                print("PLACEHOLDER")
            elif cave == "2":
                print("You keep going further only to see the cave again! You've been walking in circles!")
                print("1. Scream in anger")
                print("2. Look for another exit")

                circles = input("-~-~-~> ")

                if circles == "1":
                    print("""Your scream awakens an army of human vampire bat things
                    that fly out of the cave and eat you alive. Did you know bats use sound to
                    figure out which way to go? It's called ecolocation. Good job! You finally learned
                    something instead of just playing games!""")
                elif circles == "2":
                    print("PLACEHOLDER")
        elif steak == 1 and eat == "2":
            print("You suffer from starvation and die. Good job!")
    else:
        print(f"Well, {cake} was perhaps better.")

        steak = 0
        print("You continue on, through winding passages and slowly become hungry")
        print("1. Look around for something to eat")
        print("2. Keep going")

        food = input("-~-~-~-~> ")

        if food == "1":
            print("You find a dead body.")
            deadbody = 1
            print("1. Eat the flesh of the forgone")
            print("2. Look for something else")

            eat = input("-~-~-~> ")

            if eat == "1":
                print("You get E-coli from the body and die slowly. You probally should have cooked it first.")
            elif eat == "2":
                print("You find a stove, an electric one that works.")

                stove = input("-~-~-~> ")

                print("1. Cook the body")
                print("2. Sit on the stove")
                print("3. Go in the oven")
                if stove == "1":
                    print("You turn the stove on and cooked the body")
                    print("Good job, you canibal, going for a genocide run?")
                    print("PLACEHOLDER")
                elif stove == "2":
                    print("You sit on the stove for some reason. Are you stupid?")
                    print("1. Yes")
                    print("2. No")
                    print("3. I don't care")

                    stupid = input("-~-~-~> ")

                    if stupid == "1":
                        print("My apologies. I didn't know you had a condition.")
                        print("""You are saved by a heavenly angel and brought to the city,
                        where you are helped and end up living a long and prosperous life.""")
                    elif stupid == "2":
                        print("""You accidently turn the stove on and don't get off,
                        burning yourself. I would feel sorry for you if you didn't pretend
                        to be smart.""")
                    elif stupid == "3":
                        print("At least the dead feed the ecosystem. Be cursed forevermore!")
                        print("""You are turned into a living statue, unable to move or be destroyed,
                        forever trapped as a unmoving stone, as you were in life.""")
        elif food == "2":
            print("You meet with a terrible fate and die. Good job!")
        else:
            print("You go somewhere and do something. Continue?")
            print("1. Yes")
            print("2. No.")

            Continue = "-~-~-~> "

            if Continue == "1":
                print("PLACEHOLDER")
            elif Continue == "2":
                print("PLACEHOLDER")
            else:
                print("I'm fed up with your unwillingness to abide by my rules. Die scum.")

                why = input("-~-~-~> ")

                print("You are killed by the game itself. That was stupid.")
elif floor == "2":
    print("PLACEHOLDER")

elif floor == "3":
    print("PLACEHOLDER")

else:
    print("You phase through the ground and see the map. You're going to have a bad time")
