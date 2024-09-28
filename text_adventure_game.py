def adventure_game():
    print("You're in a dark room. Do you want to (1) open a door or (2) look for a window?")
    choice = input("> ")
    if choice == "1":
        print("You found a treasure!")
    elif choice == "2":
        print("You escaped the room!")
    else:
        print("Invalid choice!")

adventure_game()
