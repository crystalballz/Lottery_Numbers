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
	"Alaska": "AK", 
	"Alabama": "AL",
	"Arkansas": "AR",
	"Arizona": "AZ",
	"California": "CA",
	"Colorado": "CO",
	"Connecticut": "CT",
	"Delaware": "DE",
	"Florida": "FL",
	"Georgia": "GA",
	"Hawaii": "HI",
	"Iowa": "IA",
	"Idaho": "ID",
	"Illinois": "IL",
	"Indiana": "IN",
	"Kansas": "KS",
	"Kentucky": "KY",
	"Louisiana": "LA",
	"Massachusetts": "MA",
	"Maryland": "MD",
	"Maine": "ME",
	"Michigan": "MI",
	"Minnesota": "MN",
	"Missouri": "MO",
	"Mississippi": "MS",
	"Montana": "MT",
	"North Carolina": "NC",
	"North Dakota": "ND",
	"Nebraska": "NE", 
	"New Hampshire": "NH",
	"New Jersey": "NJ",
	"New Mexico": "NM",
	"Nevada": "NV",
	"New York": "NY",
	"Ohio": "OH",
	"Oklahoma": "OK",
	"Oregon": "OR",
	"Pennsylvania": "PA",
	"Rhode Island": "RI",
	"South Carolina": "SC", 
	"South Dakota": "SD",
	"Tennessee": "TN",
	"Texas": "TX",
	"Utah": "UT",
	"Virginia": "VA",
	"Vermont": "VT",
	"Washington": "WA",
	"Wisconsin": "WI",
	"West Virginia": "WV",
	"Wyoming": "WY"
}

lotteryGames = {
	"Powerball": ["","","","",""],
	"Mega Millions": ["","","","","",""],

}

class Lottery:

	def __init__(self):

		print "\nStarting Lottery Numbers\n"

	def stateSelector(self):
		state = raw_input("Which state are you in? (You can use state initials or full state names)\n")
		if (state in usStates) or (state.upper() in usStates.values()):
			self.gameSelector(state)
		elif state == "exit":
			exit(0)
		else:
			print "\nYou did not choose a valid state. Please try again.\n"
			self.stateSelector()


	def gameSelector(self,state):
		print "You have selected the state of %s" % str(state)
		gameToPlay = raw_input("Which game would you like to play?")


	def quickPick(self,game):
		numbers = ""

		return numbers


	def writeToFile(self, state, game, numbers):
		self.writeLocation = os.path.join(os.path.expanduser('~'), 'Desktop')
		self.writeFilePath = os.path.join(self.writeLocation, usStates[state] + "_" + game + ".txt")
		self.writeFile = open(self.writeFilePath, "w")
		self.writeFile.write(numbers)
		self.writeFile.close()
		if debug: 
			print "%s %s file written to desktop" % (usStates[state],game)




if __name__ == "__main__":
	l = Lottery()
	l.stateSelector()




