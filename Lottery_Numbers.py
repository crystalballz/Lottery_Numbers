#!/usr/bin/python

#THIS PYTHON SCRIPT ALLOWS USERS TO SELECT WHICH STATE AND LOTTERY GAME THEY WANT TO PLAY AND OUTPUTS QUICKPICK NUMBERS TO A TEXT FILE ON THE DESKTOP
#AUTHOR: CRISTOBAL MITCHELL
#DATE MODIFIED: 1/21/2016
#VERSION 0.0.1

#TODO


#DEBUG FLAG
debug = False

#IMPORTS
import random
import os
import sys

if debug:
	print "All modules have been imported"

#GLOBAL DICTIONARIES
usStates = {
	"AK": ["","",""], 
	"AL": ["","",""],
	"AR": ["Powerball","Mega Millions","Lucky for Life","Cash 3","Cash 4","Natural State Jackpot"],
	"AZ": ["Powerball","Mega Millions","Pick 3","Fantasy 5"],
	"CA": ["Powerball","Mega Millions","SuperLotto Plus","Daily 3","Daily 4"],
	"CO": ["Powerball","Mega Millions","Cash 5","Pick 3","Colorado Lotto"],
	"CT": ["Powerball","Mega Millions"],
	"DE": ["Powerball","Mega Millions"],
	"FL": ["Powerball","Mega Millions"],
	"GA": ["Powerball","Mega Millions"],
	"HI": ["","",""],
	"IA": ["Powerball","Mega Millions"],
	"ID": ["Powerball","Mega Millions"],
	"IL": ["Powerball","Mega Millions","Pick 3","Pick 4","Lotto","Lucky Day Lotto"],
	"IN": ["Powerball","Mega Millions"],
	"KS": ["Powerball","Mega Millions"],
	"KY": ["Powerball","Mega Millions"],
	"LA": ["Powerball","Mega Millions"],
	"MA": ["Powerball","Mega Millions"],
	"MD": ["Powerball","Mega Millions"],
	"ME": ["Powerball","Mega Millions"],
	"MI": ["Powerball","Mega Millions"],
	"MN": ["Powerball","Mega Millions"],
	"MO": ["Powerball","Mega Millions"],
	"MS": ["","",""],
	"MT": ["Powerball","Mega Millions"],
	"NC": ["Powerball","Mega Millions"],
	"ND": ["Powerball","Mega Millions"],
	"NE": ["Powerball","Mega Millions"], 
	"NH": ["Powerball","Mega Millions"],
	"NJ": ["Powerball","Mega Millions"],
	"NM": ["Powerball","Mega Millions"],
	"NV": ["Powerball","Mega Millions"],
	"NY": ["Powerball","Mega Millions","Cash4Life","Numbers","Win 4"],
	"OH": ["Powerball","Mega Millions"],
	"OK": ["Powerball","Mega Millions"],
	"OR": ["Powerball","Mega Millions"],
	"PA": ["Powerball","Mega Millions"],
	"RI": ["Powerball","Mega Millions"],
	"SC": ["Powerball","Mega Millions"], 
	"SD": ["Powerball","Mega Millions"],
	"TN": ["Powerball","Mega Millions"],
	"TX": ["Powerball","Mega Millions"],
	"UT": ["","",""],
	"VA": ["Powerball","Mega Millions"],
	"VT": ["Powerball","Mega Millions"],
	"WA": ["Powerball","Mega Millions"],
	"WI": ["Powerball","Mega Millions"],
	"WV": ["Powerball","Mega Millions"],
	"WY": ["Powerball","Mega Millions"],
}

lotteryGames = {
	"Powerball": [5,69,1,26],
	"Mega Millions": [5,75,1,15],
	"Pick 3": [0,0,0,0,3,9],
	"Pick 4": [0,0,0,0,4,9],
	"Lotto": [6,45,0,0],
	"Lucky Day Lotto": [5,45,0,0],
	"Cash4Life": [5,60,1,4],
	"Numbers": [0,0,0,0,3,9],
	"Win 4": [0,0,0,0,4,9],
	"Fantasy 5": [5,41,0,0],
	"Lucky for Life": [5,48,1,18],
	"Cash 3": [0,0,0,0,3,9],
	"Cash 4": [0,0,0,0,4,9],
	"Natural State Jackpot": [5,39,0,0],
	"SuperLotto Plus": [5,47,1,27],
	"Daily 3": [0,0,0,0,3,9],
	"Daily 4": [0,0,0,0,4,9],
	"Cash 5": [5,32,0,0],
	"Colorado Lotto": [6,42,0,0],
	"Lotto!": [6,44,0,0],
	"Cash5": [5,35,0,0],
}

class Lottery:

	def __init__(self):

		print "\nStarting Lottery Numbers\n"

	
	def stateSelector(self):
		state = raw_input("Which state are you in? (Please use state initials)\n").upper()
		if state.upper() in usStates:
			self.gameSelector(state)
		elif state == "exit":
		 	exit(0)
		else:
			print "\nYou did not choose a valid state. Please try again.\n"
			self.stateSelector()


	def gameSelector(self,state):
		print "\nYou have selected the state of %s" % str(state)
		gameToPlay = raw_input("\nWhich game would you like to play? (If you are unsure about what games are available type 'list')\n").title()
		if gameToPlay == "List":
			print
			print usStates[state]
			self.gameSelector(state)
		if gameToPlay in usStates[state]:
			print "Selected %s..." % gameToPlay
			self.quickPick(state,gameToPlay)


	def quickPick(self,state,game):
		numbers = []
		if lotteryGames[game][0] != 0:
			for i in range(lotteryGames[game][0]):
				x = random.randint(1,lotteryGames[game][1])
				if x not in numbers:
					numbers.append(x)
			numbers.sort()
		if lotteryGames[game][2] != 0:
			for i in range(lotteryGames[game][2]):
				x = random.randint(1,lotteryGames[game][3])
				numbers.append(x)		
		try:
			for i in range(lotteryGames[game][4]):
				x = random.randint(0,lotteryGames[game][5])
				numbers.append(x)
		except IndexError:
			pass
		print numbers
		self.writeToFile(state,game,numbers)


	def writeToFile(self, state, game, numbers):
		self.writeLocation = os.path.join(os.path.expanduser('~'), 'Desktop')
		self.writeFilePath = os.path.join(self.writeLocation, state + "_" + game + ".txt")
		self.writeFile = open(self.writeFilePath, "w")
		self.writeFile.write(str(numbers))
		self.writeFile.close()
		if debug: 
			print "%s %s file written to desktop" % (usStates[state],game)




if __name__ == "__main__":
	l = Lottery()
	l.stateSelector()




