import os

from art import logo

sair = True
# Clear screen
os.system('cls')
# Show logo
print(logo)
bids = []

# Function add bids to array
def add_bids(name, bid):
    bids.append({"name": name, "bid": bid})

while sair:
    name = input("What is your name?: ")
    bid  = int(input("What's your bid?: $"))
    add_bids(name, bid)
    moreplayers = input("Are there any other bidders? Type 'yes' or 'no'")

    if moreplayers == 'no':
        sair = False
    # else:
    #     os.system('cls')

    


# Function find winner
def find_winner():
    winner = {"name": "", "bid": 0}
    
    for d in bids:
        if d['bid'] > winner['bid']:
            winner['name'] = d['name']
            winner['bid'] = d['bid']
    
    return winner



winner = find_winner()
wname = winner['name']
wbid = winner['bid']

print(f"The winner id {wname.title()} with a bid of ${wbid}")