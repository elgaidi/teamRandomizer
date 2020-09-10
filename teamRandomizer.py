#!/usr/bin/env python2

import random
import datetime

now = datetime.datetime.now()

outputFile = open('TeamSchedule' + ' ' + now.strftime("%Y-%m-%d %H:%M:%S") + '.txt', 'w')

def printing(text):
    print(text)
    if outputFile:
        outputFile.write(str("\n" + text))

class Player:
	def __init__(self):
		self.name = "None"
		self.hcp = 0.0

	def getHcp(self):
		return self.hcp

	def setHcp(self, hcp):
		self.hcp = hcp

	def getName(self):
		return self.name

	def setName(self, name):
		self.name = name

class Team:
	def __init__(self):
		self.firstPlayer = Player()
		self.secondPlayer = Player()
		self.name = "None"

	def getPlayers(self):
		return self.firstPlayer, self.secondPlayer

	def setPlayers(self, player1, player2):
		self.firstPlayer = player1
		self.secondPlayer = player2

	def setName(self, name):
		self.name = name

	def getName(self):
		return self.name

Niklas = Player()
Tobbe = Player()
Mackan = Player()
Gabbe = Player()
Johan = Player()
Sammi = Player()
Emil = Player()
Dogge = Player()

Lag1 = Team()
Lag2 = Team()
Lag3 = Team()
Lag4 = Team()

Niklas.setHcp(6.9)
Niklas.setName("Niklas")
Tobbe.setHcp(7.5)
Tobbe.setName("Tobbe")
Mackan.setHcp(12.9)
Mackan.setName("Mackan")
Gabbe.setHcp(14.6)
Gabbe.setName("Gabbe")
Johan.setHcp(15.4)
Johan.setName("Johan")
Sammi.setHcp(19.0)
Sammi.setName("Sammi")
Emil.setHcp(24)
Emil.setName("Emil")
Dogge.setHcp(36.1)
Dogge.setName("Dogge")

seedingGroupOne = [Niklas, Tobbe, Mackan, Gabbe]
seedingGroupTwo = [Johan, Sammi, Emil, Dogge]
teams = [Lag1, Lag2, Lag3, Lag4]

printing("Seeding group one:")

for player in seedingGroupOne:
	printing(player.name + ", " + str(player.hcp) + " hcp")

printing("\nSeeding group two:")

for player in seedingGroupTwo:
	printing(player.name + ", " + str(player.hcp) + " hcp")

printing("\n")
raw_input("Press enter to start the team generation...")

for i in range(4):
	team = Team()

	firstPlayerSelection = random.randint(0, len(seedingGroupOne)-1)
	playerOne = seedingGroupOne[firstPlayerSelection]
	seedingGroupOne.pop(firstPlayerSelection)
	
	printing("First player: " + playerOne.name + ", " + str(playerOne.hcp))
	raw_input("\nPress enter for the next player...")

	secondPlayerSelection = random.randint(0, len(seedingGroupTwo)-1)
	playerTwo = seedingGroupTwo[secondPlayerSelection]
	seedingGroupTwo.pop(secondPlayerSelection)
	
	printing("Second player: " + playerTwo.name + ", " + str(playerTwo.hcp))
	team.setPlayers(playerOne, playerTwo)
	team.setName("Lag " + str(i + 1))
	teams[i] = team
	if( i < 3):
		raw_input("\nPress enter for the next team...")
	else:
		raw_input("\nPress enter to display the teams...")

printing("\nThe teams are the following: ")

i = 1
for team in teams:
	printing(team.name + ": " + team.firstPlayer.name + " " + team.secondPlayer.name)
	i += 1

raw_input("\nPress enter to randomize tee times:")

firstTeamFirstTeeTimeSelection = random.randint(0, len(teams)-1)
firstTeamFirstTeeTime = teams[firstTeamFirstTeeTimeSelection]
teams.pop(firstTeamFirstTeeTimeSelection)

secondTeamFirstTeeTimeSelection = random.randint(0, len(teams)-1)
secondTeamFirstTeeTime = teams[secondTeamFirstTeeTimeSelection]
teams.pop(secondTeamFirstTeeTimeSelection)

printing("\nTeams that will tee off at 10:20:")
printing(firstTeamFirstTeeTime.name + ": " +  firstTeamFirstTeeTime.firstPlayer.name + " " + firstTeamFirstTeeTime.secondPlayer.name)
printing(secondTeamFirstTeeTime.name + ": " + secondTeamFirstTeeTime.firstPlayer.name + " " + secondTeamFirstTeeTime.secondPlayer.name)

printing("\nTeams that will tee off at 10:30:")
printing(teams[0].name + ": " + teams[0].firstPlayer.name + " " + teams[0].secondPlayer.name)
printing(teams[1].name + ": " + teams[1].firstPlayer.name + " " + teams[1].secondPlayer.name)

if outputFile:
	outputFile.write("\n" + "\nThis team generation was done: " + now.strftime("%Y-%m-%d %H:%M:%S"))

