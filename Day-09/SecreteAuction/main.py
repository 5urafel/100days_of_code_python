def bidder(form):
    winner_bid = 0
    for name in form:
        if form[name] > winner_bid:
            winner_bid = form[name]
            winner_name = name
    print(f'the winner is {winner_name} with a bid of ${winner_bid}')


form = {}
condition = 'yes'

while condition.lower() == 'yes':
    name = input('What is your Name? \n')
    bid = int(input('What is your Bid? \n'))
    form[name] = bid
    print(form)
    condition = input('is there any other bidder type "yes" or "no".')

mydict = form
bidder(mydict)
