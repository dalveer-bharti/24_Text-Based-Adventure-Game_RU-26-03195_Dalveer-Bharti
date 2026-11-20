import random
# Starting game values
health = 100
score = 0

# Keep True to use fixed damage (30) for the assignment test cases.
# Change to False to use random damage between 10 and 40.
TEST_MODE = True


def forest():
    """Show the player's current status and available locations."""
    print("\nWelcome to the Forest!")
    print("Health:", health)
    print("Score:", score)


def cave():
    """Make the player face a monster in the cave."""
    global health, score

    if TEST_MODE:
        damage = 30
    else:
        damage = random.randint(10, 40)

    print("\nA monster attacks!")
    print("Damage:", damage)

    health -= damage
    print("Health:", health)

    if health > 0:
        print("You found a key!")
        score += 20
        print("Score:", score)


def river():
    """Give the player treasure for crossing the river."""
    global score

    print("\nYou crossed the river.")
    print("You found a treasure!")
    score += 50
    print("Score:", score)
    print("Health:", health)


def start_game():
    """Run the game until the player quits or loses all health."""
    global health, score

    print("=== TEXT-BASED ADVENTURE GAME ===")
    print("Explore the forest, cave and river!")

    while health > 0:
        forest()

        print("\nChoose an action:")
        print("1. Enter Cave")
        print("2. Cross River")
        print("3. Quit Game")

        choice = input("Enter your choice (1, 2 or 3): ").strip()

        if choice == "1":
            cave()

            if health <= 0:
                print("\nGame Over!")
                print("Final score:", score)
                print("Final health:", health)

        elif choice == "2":
            river()

        elif choice == "3":
            print("\nYou left the adventure.")
            print("Final score:", score)
            print("Final health:", health)
            break

        else:
            print("\nInvalid choice. Enter 1, 2 or 3.")
            print("No health lost.")

    if health <= 0:
        print("\nThanks for playing!")


if __name__ == "__main__":
    start_game()
