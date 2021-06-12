import requests

params = (
    ('deck_count', '1'),
)

response = requests.get('https://deckofcardsapi.com/api/deck/new/shuffle/', params=params)

print (response.text)