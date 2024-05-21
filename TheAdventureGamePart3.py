# Adevnture Game Task 3
place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river? ")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    else:
       pass #handle invalid action later!
elif place == "cave":
    action = input("light a torch or proceed in the dark? ")
    if action == "light a torch":
        print("Now it's easier to see!")
    elif action == "proceed in the dark":
        print("Be careful!")
    else:
        pass  # Handle invalid place later
else:
    pass #handle invalid action later!