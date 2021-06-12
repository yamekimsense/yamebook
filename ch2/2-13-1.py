
import requests

response = requests.request("GET", "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1")

print(response.text)
