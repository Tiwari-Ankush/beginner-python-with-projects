import auction
import replit
print(auction.logo)

def highest_bid(final_bidding_dict):
    highest_bid_amt=0
    for bidder in final_bidding_dict:
        bid_amt=final_bidding_dict[bidder]
        if bid_amt>highest_bid_amt:
            highest_bid_amt=bid_amt
            winner=bidder
    print(f"The winner of the Bid is: {winner.capitalize()} with bid amt: {highest_bid_amt} $\n")

stop = False
bid_dictionary={}
while not stop:
    name=input("Enter your name\n")
    bid_price=int(input("Enter bid price\n"))
        
    upd_bid_dictionary={
        name:bid_price
    }
    bid_dictionary.update(upd_bid_dictionary)

    ask=input("Is there any other, to bid ??\n  type yes/no\n  ")
    if ask=="yes"or ask=="y":
        stop=False
        # clear the screen >>
        replit.clear()
        print(auction.logo)

    else:
        stop=True
        highest_bid(bid_dictionary)

print(bid_dictionary)

            

