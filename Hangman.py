from HM_Word_Bank import word_bank
from HM_Art import hangman_art
from termcolor import colored 
import random


# function to set up game play
def game_setup(word_bank):
    print("\n" * 3)
    print(colored("   WELCOME TO HANGMAN!   ", "black", "on_light_red", attrs=["bold"]))
    print("\n" * 2)
    print("Choose a category!")
    print("\n")

    chosen_cat = ""
    while chosen_cat not in word_bank:
        for cat in word_bank:
            print(colored(cat, "blue"))
        print()
        chosen_cat = input("Your Choice: ").strip().title()
        print("\n")
        if chosen_cat not in word_bank:
            print("\nInvalid input. Please try again.\n")
    
    answer = random.choice(word_bank[chosen_cat]).lower()
    return chosen_cat, answer


# function for art display
def display_man(wrong_guesses):
	print()
	print("*******************")
	for line in hangman_art[wrong_guesses]:
		print(line)
	print()
	print("*******************")
	print()

# function for hint display
def display_hint(hint):
	print(" ".join(hint))

# function for answer display 
def display_answer(answer):
	print(" ".join(answer))

# function for guessed letters display
def display_guessed_letters(guessed_letters):
	print("Used: ", " ".join(sorted(guessed_letters)))


# function for entire game logic
def main():
	chosen_cat, answer = game_setup(word_bank)
	hint = ["_"] * len(answer)
	wrong_guesses = 0
	guessed_letters = set()
	is_running = True 

	while is_running:
		display_man(wrong_guesses)
		display_hint(hint)
		print("\n" * 2)
		display_guessed_letters(guessed_letters)
		print()
		guess = input(colored("Guess a letter: ", "magenta")).lower()
		print("\n")

		if len(guess) != 1 or not guess.isalpha():
			print("Invalid input. Please try again")
			continue
		
		if guess in guessed_letters:
			print(f"{guess} is already guessed!")
			continue 

		guessed_letters.add(guess)
	
		if guess in answer:
			for i in range(len(answer)):
				if answer[i] == guess:
					hint[i] = guess
		else:
			wrong_guesses += 1

		if "_" not in hint:
			display_man(wrong_guesses)
			display_answer(answer)
			print("\n" * 2)
			print(colored(f"YOU WIN!!! The correct answer was {answer}!","green"))
			print()
			is_running = False

		elif wrong_guesses >= len(hangman_art) - 1:
			display_man(wrong_guesses)
			display_answer(answer)
			print("\n" * 2)
			print(colored(f"YOU LOSE! ¯\\_(ツ)_/¯ Sorry the correct answer was {answer}.", "red"))
			print()
			is_running = False

if __name__ == "__main__": 
	while True: 
		main()
		play_again = input("Do you want to play again? (Y/N): ").strip().lower()
		print("\n")
		if play_again not in ("y","yes","yeah"):
			print(colored("Thanks for playing! See you next time!" ,"blue"))
			print("\n" * 2)
			break