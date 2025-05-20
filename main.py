import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


# HINT: You can call clear() to clear the output in the console.
bidderDict = {}


def addBidder(name, price):
    bidderDict[name] = price
    cls()


# def checkHighest():
#   maxValue=max(bidderDict.values())
#   maxKey=max(bidderDict, key=bidderDict.get)
#   print(f"The winner is {maxKey} with ${maxValue} bid")
def checkHighest(bidValues):  # passing bidderDict{} values to the bidValues parameter
    highestBid = 0
    for bid in bidValues:  # loop through the keys inside the bidValues{}
        tempHighest = bidValues[bid]  # reading the value of the current key from the bidValues{}
        if tempHighest > highestBid:  # checking if tempHighest is greater than highestBid
            highestBid = tempHighest  # sets the highestBid's value to the tempHighest's
            winner = bid  # stores the key from the current highest value from bidValues{}
    print(f"The winner is {winner} with ${highestBid} bid")


print("Blind Auction")
print("Welcome to the secret auction house!")

startBid = False
while not startBid:
    bidderName = input("Please enter your name: ")
    bidPrice = int(input("Please enter your price: $"))
    addBidder(bidderName, bidPrice)
    addAnother = input("is there another bidder? y/n\n").lower()
    if addAnother == "y":
        cls()
    elif addAnother == "n":
        startBid = True
checkHighest(bidderDict)
