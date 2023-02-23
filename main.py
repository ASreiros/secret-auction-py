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
        print("Your bid is not float. It will be ignored")
        bid_float = False

    if bid_float is True:
        bidders[name] = float(bid)

    more = input('Are there any other bidders? Type "yes" or "no"').lower()
    if more != "yes":
        bid_flag = True

