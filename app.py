# import requests

# url = "https://wordsapiv1.p.rapidapi.com/words/monday/typeOf"

# headers = {
# 	"X-RapidAPI-Host": "wordsapiv1.p.rapidapi.com",
# 	"X-RapidAPI-Key": "ec15220be3mshb409e3288051fd2p1c18fbjsn7819d389df2a"
# }

# response = requests.request("GET", url, headers=headers)

# print(response.text)

word = "hyenas"

def rounds(current_round):
  print(current_round)
  rounds_remaining = current_round -1
  return rounds_remaining
  

def determine_results(win, answer, results, rounds_remaining):
  '''
  checks the user entered word to determine the win state and the hints array
  '''
  if answer == word:
    win = True
    print("You Win!") 
    play_again()
  else:
    count = 0
    for letter in answer:
      if letter in word:
        results.insert(count, "*")
        if letter in word[count]:
          results.pop(count)
          results.insert(count, "$")
        count += 1
      else:
        results.insert(count, "-")
        count += 1
        
  current_round = rounds_remaining
  rounds_remaining = rounds(current_round)
  
  if rounds_remaining <= 0:
    print("Your five chances have been used! Bad Luck!")
    play_again()
  elif win != True:
    print(results)
    ask_question(rounds_remaining)

def ask_question(rounds_remaining):
  '''
  Asks the user to enter a word
  '''
  answer = input("please enter a word: ")
  win = False
  results = []
  determine_results(win, answer, results, rounds_remaining)

def play_again():
  play_again = input("Would you like to play again? Enter Y or N: ")
  if play_again == "Y" or play_again == "y" :
    ask_question(5)
  elif play_again == "N" or play_again == "n":
    print("Thanks and come back soon")
  else:
    play_again()

ask_question(5)