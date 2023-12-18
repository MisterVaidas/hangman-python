import random
import hangman_words as words
import hangman_art as art

chosen_word = random.choice(words.word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6
print(art.logo)
display = ["_"] * word_length
guessed_letter = []

while not end_of_game:
  guess = input("Guess a letter: ").lower()
  if guess in guessed_letter:
    print(f"You've already guessed {guess}")
    continue
  else:
    guessed_letter.append(guess)
    
  if guess in chosen_word:
    for position in range(word_length):
      letter = chosen_word[position]
      if letter == guess:
        display[position] = letter
    print("Good guess!")
  else:
    print(f"{guess} is not in the word.")
    lives -= 1
    
  print(f"{''.join(display)}")
  
  if "_" not in display:
    end_of_game = True
    print("You win!")
  elif lives == 0:
    print(f"You lose. The word was {chosen_word}")
    
  print(art.stages[lives])