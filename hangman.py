import random


def play_hangman():
  words = ["python", "intern", "coding", "script", "module"]
  secret_word = random.choice(words)
  guessed_letters = set()
  incorrect_guesses = 0
  max_incorrect = 6

  print("=== Welcome to Hangman ===")
  print(f"You have {max_incorrect} incorrect guesses allowed.\n")

  while incorrect_guesses < max_incorrect:
    display_word = " ".join(
        [letter if letter in guessed_letters else "_" for letter in secret_word]
    )
    print(f"Word: {display_word}")
    print(
        f"Incorrect guesses left: {max_incorrect - incorrect_guesses}"
        f"/{max_incorrect}"
    )
    if guessed_letters:
      print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")

    if "_" not in display_word:
      print(
          f"\nCongratulations! You guessed the word '{secret_word}' correctly!"
      )
      return

    guess = input("Enter a single letter: ").strip().lower()

    if len(guess) != 1 or not guess.isalpha():
      print("Please enter a single valid alphabet letter.\n")
      continue

    if guess in guessed_letters:
      print(f"You already guessed '{guess}'. Try another letter.\n")
      continue

    guessed_letters.add(guess)

    if guess in secret_word:
      print(f"Good job! '{guess}' is in the word.\n")
    else:
      incorrect_guesses += 1
      print(f"Sorry, '{guess}' is not in the word.\n")

  print(f"Game over! Out of guesses. The word was '{secret_word}'.")


if __name__ == "__main__":
  play_hangman()