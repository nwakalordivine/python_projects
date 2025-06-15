from utili import logo

print(logo)
bidder_information = {
        "bidder_name": [],
        "bidder_price": []
    }


def auction():
    # TODO-1: Ask the user for input
    bidder = input("What is your name?: ")
    bid = int(input("what is your bid?: $"))
    # TODO-2: Save data into dictionary {name: price}
    bidder_information["bidder_name"].append(bidder)
    bidder_information["bidder_price"].append(bid)
    # TODO-3: Whether if new bids need to be added
    global more_bidders


continue_bid = True
while continue_bid is True:
    auction()
    more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if more_bidders == "yes":
        print("\n" * 20)
    elif more_bidders == "no":
        # TODO-4: Compare bids in dictionary
        winner_price = 0
        for price in bidder_information["bidder_price"]:
            if price > winner_price:
                winner_price = price

        bidder_id = bidder_information["bidder_price"].index(winner_price)
        print(f"The winner is {bidder_information["bidder_name"][bidder_id]}"
              f" with a bid of ${bidder_information["bidder_price"][bidder_id]}")
        continue_bid = False
