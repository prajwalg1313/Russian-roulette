import random
import time


def spin_chamber():
    #Load and spin the revolver chamber
    print("\nSpinning the chamber :", end="", flush=True)
    time.sleep(1)
    print(" 🔄")
    # Random chamber position 1–6
    return random.randint(1, 6)


def pull_trigger(chamber, bullet_position):
    #Simulate pulling the trigger
    print("Pulling the trigger:", end="", flush=True)
    time.sleep(1)
    return chamber == bullet_position


def play():
    #Run one round of Russian Roulette
    print("\nWelcome to Russian Roulette:")
    player = input("Enter your name: ")
    
    bullet_position = random.randint(1, 6)
    chamber = spin_chamber()

    print(f"\nAlright {player} here we go")
    time.sleep(1.5)

    # Only one simple if
    if pull_trigger(chamber, bullet_position):
        print("\n Bang! You lost.")
    else:
        print("\n Click! You survived.")


def main():
    #Loop the game until user quits
    while True:
        play()
        again = input("\nPlay again? (y/n): ").lower().strip()
        if again != 'y':
            print("\nThanks for playing, good luck")
            break


if __name__ == "__main__":
    main()
