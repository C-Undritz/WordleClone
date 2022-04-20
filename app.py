import requests
import os
if os.path.exists("env.py"):
    import env


# word = "hello"
rapidapi_key = os.environ.get("WORDSAPI_KEY")


def generate_word():
	'''
	Generates a word
	'''
	url = "https://random-words5.p.rapidapi.com/getMultipleRandom"
	querystring = {
		"count": "1",
		"wordLength": "5"
	}
	headers = {
		"X-RapidAPI-Host": "random-words5.p.rapidapi.com",
		"X-RapidAPI-Key": rapidapi_key
	}

	response = requests.request("GET", url, headers=headers, params=querystring)
	print(response.text)


# def rounds(current_round):
# 	print(current_round)
# 	rounds_remaining = current_round - 1
# 	return rounds_remaining


# def determine_results(win, answer, results, rounds_remaining):
# 	'''
# 	checks the user entered word to determine the win state and the hints array
# 	'''
# 	if answer == word:
# 		win = True
# 		print("You Win!") 
# 		play_again()
# 	else:
# 		count = 0
# 		for letter in answer:
# 			if letter in word:
# 				results.insert(count, "*")
# 				if letter in word[count]:
# 					results.pop(count)
# 					results.insert(count, "$")
# 				count += 1
# 			else:
# 				results.insert(count, "-")
# 				count += 1
    
# 	current_round = rounds_remaining
# 	rounds_remaining = rounds(current_round)
  
# 	if rounds_remaining <= 0:
# 		print("Your five chances have been used! Bad Luck!")
# 		play_again()
# 	elif win != True:
# 		print(results)
# 		ask_question(rounds_remaining)


# def ask_question(rounds_remaining):
#     '''
#     Asks the user to enter a word
#     '''
#     answer = input("please enter a word: ")
#     win = False
#     results = []
#     determine_results(win, answer, results, rounds_remaining)


# def play_again():
# 	play_again = input("Would you like to play again? Enter Y or N: ")
	
# 	if play_again == "Y" or play_again == "y":
# 		ask_question(5)
# 	elif play_again == "N" or play_again == "n":
# 		print("Thanks and come back soon")
# 	else:
# 		play_again()


def validate_word(word):
	'''
	Takes the word generated and written by user to check that it is a valid word
	'''
	url = "https://wordsapiv1.p.rapidapi.com/words/" + word + "/typeOf"

	headers = {
		"X-RapidAPI-Host": "wordsapiv1.p.rapidapi.com",
		"X-RapidAPI-Key": rapidapi_key
	}

	response = requests.request("GET", url, headers=headers)
	data = response.text
	print(data)
	result = ""

	x = 2
	while x < 9:
		result += data[x]
		x += 1

	if result == 'success':
		print("Value Entered is not a word")
	else:
		print("that is a word")



# ask_question(5)
# validate_word()
generate_word()