#---------------------------------------------------------------------------
# Constants
#---------------------------------------------------------------------------
Gold = ("Gold", "01ecf94f-c408-4e43-8984-211fbdc25001") #The GUID from markers.o8g
Power = ("Power", "01ecf94f-c408-4e43-8984-211fbdc25002") #The GUID from markers.o8g
STR_Up = ("STR_Up", "01ecf94f-c408-4e43-8984-211fbdc25003") #The GUID from markers.o8g
Burn = ("Burn", "01ecf94f-c408-4e43-8984-211fbdc25004") #The GUID from markers.o8g
MilitaryColor = "#ae0603" #A shade of red from the Military Icon
IntrigueColor = "#006b34" #A shade of green from the Intrigue Icon
PowerColor = "#1a4d8f" #A shade of blue from the Power Icon
GameURL = "http://tinyurl.com/aGoT-LCG-OCTGN"
FAQ_URL = "http://www.fantasyflightgames.com/ffg_content/agotlcg/support/FAQ-TR-updates/AGoT-FAQ.pdf"
LeagueURL = "http://tinyurl.com/aGoT-OCTGN-League-S1"
#---------------------------------------------------------------------------
# Table group actions
#---------------------------------------------------------------------------
def googleDriveWebsite(group, x = 0, y = 0):
	mute()
	
	openUrl("{}".format(GameURL))
	
def faqWebsite(group, x = 0, y = 0):
	mute()
	
	openUrl("{}".format(FAQ_URL))
	
def OCTGN_LeagueWebsite(group, x = 0, y = 0):
	mute()
	
	openUrl("{}".format(LeagueURL))
	
def flipCoin(group, x = 0, y = 0):
	mute()
	n = rnd(1, 2)
	if n == 1:
		notify("**{} flips heads.**".format(me))
	else:
		notify("**{} flips tails.**".format(me))
		
def sixSided(group, x = 0, y = 0):
	mute()
	n = rnd(1,6)
	notify("**{} rolls a {} on a 6-sided die.**".format(me, n))
	
def twelveSided(group, x = 0, y = 0):
	mute()
	n = rnd(1,12)
	notify("**{} rolls a {} on a 12-sided die.**".format(me, n))
	
def xSided(group, x = 0, y = 0):
	mute()
	sides = askInteger("Roll a how many sided die? (minimum 3)", 3)
	if sides == None: return
	elif sides < 3:
		whisper("Please choose a number greater than or equal to 3.")
		return
	else:
		n = rnd(1,sides)
		notify("**{} rolls a {} on a {}-sided die.**".format(me, n, sides))

def recalcPower(group, x = 0, y = 0):
	mute()
	index = 0
	for person in players:
		person.counters['Power'].value = 0
		personCards = (card for card in table
						if card.controller == person)
		for card in personCards:
			if card.markers[Power] > 0:
				person.counters['Power'].value += card.markers[Power]
		notify("{} has a total of {} power.".format(person.name,person.counters['Power'].value))

def cancelAllHighlight(group, x = 0, y = 0):
	mute()
	for card in group:
		card.target(False)
		if card.controller == me:
			card.highlight = None

def turnDone(group, x = 0, y = 0):
	mute()
	notify("**{} is done.**".format(me))

def restoreAll(group, x = 0, y = 0): 
	mute()
	myCards = (card for card in table
				if card.controller == me
				and card.owner == me)
	for card in myCards:
		if card.isFaceUp:
			card.orientation &= ~Rot90
			card.highlight = None
	notify("{} stands all their cards.".format(me))

def announceMil(group, x = 0, y = 0):
	mute()
	notify("**{} declares a MIL challenge.**".format(me))

def announceInt(group, x = 0, y = 0):
	mute()
	notify("**{} declares an INT challenge.**".format(me))

def announcePow(group, x = 0, y = 0):
	mute()
	notify("**{} declares an PWR challenge.**".format(me))

def holdOn(group, x = 0, y = 0):
	mute()
	notify("**Please wait.  {} has an action/question.**".format(me))

def announceUO(group, x = 0, y = 0):
	mute()
	notify("**{} responds: Unopposed.**".format(me))

def announceOpp(group, x = 0, y = 0):
	mute()
	notify("**{} responds: Opposed/Defend.**".format(me))
	
def scoop(group, x = 0, y = 0):
	mute()
	
	if not confirm("Scoop your side of the table?"): return
	
	for c in me.hand: 
		if not c.Type == "House Card" and not c.Type == "Agenda":
			c.moveTo(me.Deck)			
	for c in me.piles['Discard Pile']: c.moveTo(me.Deck)
	for c in me.piles['Dead Pile']: c.moveTo(me.Deck)
	for c in me.piles['Hold']: c.moveTo(me.Deck)

	myCards = (card for card in table
        	if card.owner == me)

	for card in myCards:
		if card.Type == "House Card": 
			card.moveTo(me.hand)
		elif card.Type == "Agenda":
			card.moveTo(me.hand)
		elif card.Type == "Plot": 
			card.moveTo(me.piles['Plot Deck'])
		else: 
			card.moveTo(me.Deck)
	
	notify("{} scoops their side of the table.".format(me))

#---------------------------------------------------------------------------
# Table card actions
#---------------------------------------------------------------------------
def displayErrata(card, x = 0, y = 0):
	mute()
	
	notify('{} - Errata Text:'.format(card.name))
	notify('{}'.format(card.ErrataText))
	
def cardLookup(card, x = 0, y = 0):
	mute()
	
	if card.isFaceUp:
		webSite = ""
		webSite += "http://www.cardgamedb.com/index.php/GoT/gotcardsearch.html?ft=0"
		webSite += "&name={}".format(card.name)
		webSite += "&type={}".format(card.Type)
		openUrl("{}".format(webSite))
	else:
		whisper("Card must be face up to use this feature.")
	
def kneel(card, x = 0, y = 0):
    mute()
    card.orientation ^= Rot90
    if card.orientation & Rot90 == Rot90:
        notify('{} kneels {}.'.format(me, card))
    else:
        notify('{} stands {}.'.format(me, card))

def flipcard(card, x = 0, y = 0):
    mute()
    if card.isFaceUp:
        notify("{} turns {} face down.".format(me, card))
        card.isFaceUp = False
    else:
        card.isFaceUp = True
        notify("{} turns {} face up.".format(me, card))

def addGold(card, x = 0, y = 0):
	mute()
	notify("{} adds a Gold to {}.".format(me, card))
	card.markers[Gold] += 1
    
def addPower(card, x = 0, y = 0):
    mute()
    notify("{} adds a Power to {}.".format(me, card))
    card.markers[Power] += 1
    me.counters['Power'].value += 1
	
def addSTR_Up(card, x = 0, y = 0):
	mute()
	card.markers[STR_Up] += 1
	
def addBurn(card, x = 0, y = 0):
	mute()
	card.markers[Burn] += 1
    
def subGold(card, x = 0, y = 0):
    mute()
    notify("{} subtracts a Gold to {}.".format(me, card))
    card.markers[Gold] -= 1
    
def subPower(card, x = 0, y = 0):
    mute()
    notify("{} subtracts a Power to {}.".format(me, card))
    card.markers[Power] -= 1 
    me.counters['Power'].value -= 1
	
def subSTR_Up(card, x = 0, y = 0):
    mute()
    card.markers[STR_Up] -= 1
	
def subBurn(card, x = 0, y = 0):
    mute()
    card.markers[Burn] -= 1
	
def addMilitaryHighlight(card, x = 0, y = 0):
	mute()
	card.highlight = MilitaryColor
	card.target(False)
	
def addIntrigueHighlight(card, x = 0, y = 0):
	mute()
	card.highlight = IntrigueColor
	card.target(False)
	
def addPowerHighlight(card, x = 0, y = 0):
	mute()
	card.highlight = PowerColor
	card.target(False)

def cancelHighlight (card, x = 0, y = 0):
	mute()
	card.highlight = None
	card.target(False)

#---------------------------
#movement actions
#---------------------------

#------------------------------------------------------------------------------
# Hand Actions
#------------------------------------------------------------------------------

def randomDiscard(group):
	mute()
	card = group.random()
	if card == None: return
	card.moveTo(me.piles['Discard pile'])
	notify("{} randomly discards {}.".format(me, card))
 
def discardMany(group):
	count = 0
	discAmount = None
	
	mute()
	if len(group) == 0: return
	if discAmount == None: discAmount = askInteger("Randomly discard how many cards?", 2)
	if discAmount == None: return
	
	for index in range(0,discAmount):
		card = group.random()
		if card == None: break
		card.moveTo(me.piles['Discard pile'])
		count += 1
		notify("{} randomly discards {}.".format(me,card))
	notify("{} randomly discards {} cards.".format(me, count))

def mulligan(group):
	count = None
	draw = None
	mute()
	
	if not confirm("Are you sure you want to Mulligan?"): return
	if draw == None: draw = askInteger("How many cards would you like to draw for your Mulligan?", len(me.hand))
	if draw == None: return
	
	for card in group:
		card.moveToBottom(me.deck)
			
	me.deck.shuffle()
		
	for card in me.deck.top(draw):
		card.moveTo(me.hand)
	notify("{} mulligans and draws {} new cards.".format(me, draw))

#------------------------------------------------------------------------------
# Pile Actions
#------------------------------------------------------------------------------

def shuffle(group):
	group.shuffle()

def draw(group):
	mute()
	if len(group) == 0: return
	group[0].moveTo(me.hand)
	notify("{} draws a card.".format(me))
	
def drawRandom(group):
	mute()
	
	card = group.random()
	if card == None: return
	card.moveTo(me.hand)
	notify("{} randomly draws a plot card.".format(me))

def drawMany(group):
	drawAmount = None
	
	mute()
	if len(group) == 0: return
	if drawAmount == None: drawAmount = askInteger("Draw how many cards?", 7)
	if drawAmount == None: return
	
	if len(group) < drawAmount:
		drawAmount = len(group)
	
	for card in group.top(drawAmount):
		card.moveTo(me.hand)
	notify("{} draws {} cards.".format(me, drawAmount))
 
def discardManyFromTop(group):
	count = 0
	discAmount = None
	
	mute()
	if len(group) == 0: return
	if discAmount == None: discAmount = askInteger("Discard how many from top?", 4)
	if discAmount == None: return
	
	for index in range(0,discAmount):
		card = group.top()
		card.moveTo(me.piles['Discard pile'])
		count += 1
		if len(group) == 0: break
	notify("{} discards {} cards from the top of their Deck.".format(me, count))
 
def moveToHold(group, count = None, a = 0):
	count = 0
	moveAmount = None
	
	mute()
	group.shuffle()
	if len(group) == 0: return
	if moveAmount == None: moveAmount = askInteger("Move how many cards to your Hold?", 30)
	if moveAmount == None: return
	
	for index in range(0,moveAmount):
		if len(group) == 0: return
		card = group.top()
		card.moveTo(me.piles['Hold'])
		count += 1		
	notify("{} moved {} cards from the top of their Deck to their Hold.".format(me, count))
	
def reshuffle(group):
	count = None
	
	mute()
	if len(group) == 0: return
	if not confirm("Are you sure you want to reshuffle the {} back into your Deck?".format(group.name)): return
	
	myDeck = me.deck
	for card in group:
		card.moveTo(myDeck)
	myDeck.shuffle()
	notify("{} shuffles thier {} back into their deck.".format(me, group.name))
	
def moveOneRandom(group):
	mute()
	if len(group) == 0: return
	if not confirm("Are you sure you want to move one random card from your {} to your Hand?".format(group.name)): return
	
	card = group.random()
	if card == None: return
	card.moveTo(me.hand)
	notify("{} randomly moves {} from their discard to thier hand.".format(me, card.name))
	
