import requests

deck_shuffle_url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
response = requests.get(deck_shuffle_url)
deckObject = response.json()
# print(deckObject) 
# {'success': True, 'deck_id': 'ljbvmfjxs4mf', 'remaining': 52, 'shuffled': True}

deck_id = deckObject["deck_id"]

draw_5_cards_url = "https://deckofcardsapi.com/api/deck/{}/draw/?count=5".format(deck_id)
getCardsResponse = requests.get(draw_5_cards_url)
cardsJsonObject = getCardsResponse.json()
print(cardsJsonObject) 

valueSingles = []
valueDoubles = []
valueTriples = []
previousSuit = ""
suitCounter = 0
drawCounter = 0 # Number of draws

for card in cardsJsonObject["cards"]:
    drawCounter+=1
    value = card['value']
    suit = card['suit']
    print("value is "+value+ " and suit is "+ suit)

    # checking for doubles and triples
    if(valueDoubles.__contains__(value)):
        valueTriples.append(value)
        valueDoubles.remove(value)
    elif(valueSingles.__contains__(value)):
        valueDoubles.append(value)
        valueSingles.remove(value)
    else:
        valueSingles.append(value)

    # checking for all same suit
    if(suit == previousSuit):
        suitCounter+=1
        if(suitCounter==drawCounter): # in this case 5
            print("Congragulations!!. You draw " + suit + " for all " + drawCounter + " draws")
    elif(drawCounter == 1):
        suitCounter = 1
    else:
        suitCounter = 0
    previousSuit = suit    

if(len(valueDoubles)>0):
    print("Here is the list of doubles : ")
    for item in valueDoubles:
        print(item + "\n")
    # for(value in valueDoubles)
else:
    print("No doubles in this draw")

if(len(valueTriples)>0):
    print("Here is the list of triples : ")
    for item in valueTriples:
        print(item + "\n")
else:
    print("No tripples in this draw")




