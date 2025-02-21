import requests

deck_shuffle_url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
response = requests.get(deck_shuffle_url)
deckObject = response.json()
# print(deckObject) 
# {'success': True, 'deck_id': 'ljbvmfjxs4mf', 'remaining': 52, 'shuffled': True}

deck_id = print(deckObject["deck_id"])

