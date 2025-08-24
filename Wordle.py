Red = "\033[0;31m"
Green = "\033[0;32m"
Yellow = "\033[0;33m"
White = "\033[0;37m" 

def wordle(word):
  won = False
  lost = False
  guesses = 0
  
  while won != True and lost != True:
    count = 0
    guess = input(White + "\nEnter your guess: ")
    if len(guess) > 5 or len(guess) < 5:
      print("Please enter a 5-letter word!")
    else:
      for i in range(0,5):
        if word[i] == guess[i]:
          print(Green + guess[i], end = "")
          count += 1
        elif guess[i] in word:
          print(Yellow + guess[i], end = "")
        else:
          print(Red + guess[i], end = "")
      
      guesses += 1
      if count == 5:
        won = True
        return White + "\nYou won!"
      if guesses == 6:
        lost = True
        return Red + "\nYou Lost! The word was " + word

print(wordle("audio"))
          
