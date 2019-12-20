SUITE='H D S C'.split()
RANK='1 2 3 4 5 6 7 8 9 10 J Q K A'.spilt()

cards=[]

for s in SUITE:
    for r in RANK:
        cards.append((s,r))

"create a deck of cards"

class deck:
    
    def __init__(self):
        self.allcards=cards
    
    def shuffle(self):
        shuffle(self.card)
        
    def split_half:
        
        return(self.cards[:26],self.cards[26:])
        