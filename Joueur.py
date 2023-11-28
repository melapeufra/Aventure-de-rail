import collections

class Joueur(object):
    
    def __init__(self, H,T,B,P,N):
        
        self.name           = '' 
        
        self.hand           = collections.Counter(H)
        
        self.tickets        = {x:False for x in T}
        self.numTrains      = N
        self.points         = 0
        self.playerPosition = P
        
        self.playerBoard    = B
        
    def removeCardsFromHand(self, color, numColor):
        """Enlevés une ou plus de cartes de de "hand" assure que toutes 
        les cartes sont en "hand, erreur sinon
        cards: list
        """
        assert self.hand[color] >= numColor
        self.hand[color] -= numColor
        
    #add card to hand
    def addCardToHand(self, card):
        """adds a single card to hand
        assumes card is a valid choice
        card: String
        """
        if card != None:
            self.hand[card] += 1
    
    #add ticket to hand
    def addTicket(self, ticket):
        """adds a single ticket to tickets
        ticket: tuple(city1, city2, value)
        """
        self.tickets[ticket] = False
    
    def completeTicket(self, ticket):
        """updates the value in the tickets dict to True for key: ticket
        ticket: tuple(city1, city2, value)
        """
        assert ticket in self.tickets
        self.tickets = True
    
    def getHand(self):
        return self.hand
    
    def addPoints(self, numPoints):
        self.points += numPoints
    
    def subtractPoints(self, numPoints):
        self.points -= numPoints
        
    def getPoints(self):
        return self.points
        
    def getTickets(self):
        return self.tickets
    
    def getNumTrains(self):
        return self.numTrains
    
    def playNumTrains(self, numTrains):
        assert numTrains <= self.numTrains
        self.numTrains -= numTrains
        
    def setPlayerName(self, name):
        """sets playerName to name
        name: string
        """
        self.name = name
    
    def getName(self):
        return self.name