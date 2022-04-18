import requests

url = "https://wordsapiv1.p.rapidapi.com/words/gtyrud/typeOf"

headers = {
	"X-RapidAPI-Host": "wordsapiv1.p.rapidapi.com",
	"X-RapidAPI-Key": "ec15220be3mshb409e3288051fd2p1c18fbjsn7819d389df2a"
}

response = requests.request("GET", url, headers=headers)

print(response.text)