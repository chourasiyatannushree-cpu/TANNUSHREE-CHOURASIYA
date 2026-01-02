# HANGMAN GAME 
import random

stages = [r'''
 ===================
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \
     |
 jgs_|___
''', r'''
 ===================
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      /
     |
 jgs_|___
''', r'''
 ===================
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |
     |
 jgs_|___
''', r'''
 ===================
      _______
     |/      |
     |      (_)
     |      \|
     |
     |
     |
 jgs_|___
''', r'''
 ===================
      _______
     |/      |
     |      (_)
     |
     |
     |
     |
 jgs_|___
''', r'''
 ===================
      _______
     |/      |
     |
     |
     |
     |
     |
 jgs_|___
''']

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

lives = 6
game_over = False
correct_letters = []

# Initial placeholder
display = "_" * word_length
print("Word to guess:")
print(display)

while not game_over:
    guess = input("\nGuess a letter: ").lower()

    if guess in correct_letters:
        print("⚠️ You already guessed that letter.")
        continue

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            if guess not in correct_letters:
                correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    if guess not in chosen_word:
        lives -= 1
        print(f"❌ Wrong guess! Lives left: {lives}")
        print(stages[lives])

        if lives == 0:
            game_over = True
            print("\n💀 YOU LOSE!")
            print(f"The word was: {chosen_word}")

    if "_" not in display:
        game_over = True
        print("\n🎉 YOU WIN!")