from time import sleep
import os


print("Welcome to secret auction program.")

bidders = {}
bid_flag = False

while bid_flag is False:
    name = input("What is your name?: ")
    bid = input("What is your bid?: $")
    bid_float = True
    try:
        float(bid)
        bid_float = True

    except:
        bid_float = False

    if bid_float is True and float(bid)>0:
        bidders[name] = float(bid)
    else:
        print("Your bid is not a positive amount of money. It will be ignored")

    more = input('Are there any other bidders? Type "yes" or "no"').lower()
    if more != "yes":
        bid_flag = True
    else:
        sleep(0.5)
        if os.name == 'posix':
            os.system('clear')
        else:
            os.system('cls')
if bidders:
    good_bid = 0
    bid_name = ""
    for key in bidders:
        if bidders[key] > good_bid:
            good_bid = bidders[key]
            bid_name = key
    print(f"The winner is {bid_name} with a bid of ${good_bid}")
else:
    print("There are no bidders with valid bids.")
