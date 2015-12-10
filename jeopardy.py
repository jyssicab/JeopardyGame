#!/usr/bin/python
from prettytable import PrettyTable
import time
from termcolor import colored
import readchar

lastCategory = ""
lastAmount = ""
lastAnswer = ""

guessed = 1

currentPlayer = "Player1"

player1 = "Player1"
player2 = "Player2"
player3 = "Player3"

topic1 = "America"
topic2 = "Animals"
topic3 = "Sports"
topic4 = "Nazo Nazo"
topic5 = "Music"

amount = ["10", "20", "30", "40", "50"]

amount1 = ["10", "20", "30", "40", "50"]
amount2 = ["10", "20", "30", "40", "50"]
amount3 = ["10", "20", "30", "40", "50"]
amount4 = ["10", "20", "30", "40", "50"]
amount5 = ["10", "20", "30", "40", "50"]

score_earned = [10,20,30,40,50]

p1_score = 0
p2_score = 0
p3_score = 0


topic1_Q = ["What is the capital of the United States?",
	"What is the longest river in America?", 
	"Which State of the USA was once part of Mexico?", 
	"What country is north of America?", 
	"Which of the following cities is in Nevada?"]

topic1_A = ["washington",
	"mississippi",
	"texas",
	"canada",
	"reno"]


topic2_Q = ["What food makes up to nearly all of a Giant Panda's diet?",
	"What is the largest type of 'big cat' in the world?",
	"What is the name of an adult female horse?",
	"Bees are found on every continent of earth except for one, which is it?",
	"What are female elephants called"]

topic2_A = ["bamboo",
	"tiger",
	"mare",
	"antarctica",
	"cows"]



topic3_Q = ["How many members are on a soccer team?",
	"What is Hideo Nomo's uniform number?",
	"In tennis, what is the name of 0 points?",
	"Which is the only country to have played in each and every World Cup?",
	"What sport used the term 'home run' long before baseball?"]

topic3_A = ["11",
	"16",
	"love",
	"brazil",
	"cricket"]

topic4_Q = ["1, 2, 4, 8, 16, ?",
	"z, y, x, w, ?",
	"s, m, t, ?, t, f, s",
	"o, t, t, f, f, ?",
	"j, y, k, a, n, ?, k"]

topic4_A = ["32",
	"v",
	"w",
	"s",
	"h"]

topic5_Q = ["What was Madonna's first UK top ten single?",
	"Which singer appeared in the feature film, Battleship?",
	"In May 2015, who dressed up as George Michael to celebrate their 27th birthday and posted the snaps on Twitter?",
	"How many keys are on a piano?",
	"Which pop band features Sharleen Spiteri on lead vocals?"]

topic5_A = ["holiday",
	"rihanna",
	"adele",
	"88",
	"texas"]


#declaration of functions
def initialTable():
	x = PrettyTable()
	x.add_column(topic1, [amount1[0], amount1[1], amount1[2], amount1[3], amount1[4]])
	x.add_column(topic2, [amount2[0], amount2[1], amount2[2], amount2[3], amount2[4]])
	x.add_column(topic3, [amount3[0], amount3[1], amount3[2], amount3[3], amount3[4]])
	x.add_column(topic4, [amount4[0], amount4[1], amount4[2], amount4[3], amount4[4]])
	x.add_column(topic5, [amount5[0], amount5[1], amount5[2], amount5[3], amount5[4]])
	
	print x.get_string(header=True, border=True)

def instructions():
	print colored("INSTRUCTIONS", 'red')
	print colored("---To choose a topic and score, enter exactly what is typed on Board (capatilization)---", 'yellow')
	print colored("---Returning champion selected topic first---", 'yellow')
	print colored("---Buzz in to answer quesiton---", 'yellow')
	print colored("\t" + player1 + " use key a", 'blue')
	print colored("\t" + player2 + " use key l\n", 'green')

def getQuestion(cat, amnt):
	#if statements
	if cat == topic1:
		i = 0
		for x in amount:
			if amnt == x:
				return topic1_Q[i]
			i += 1
	elif cat == topic2:
		i = 0
		for x in amount:
			if amnt == x:
				return topic2_Q[i]
			i += 1
	elif cat == topic3:
		i = 0
		for x in amount:
			if amnt == x:
				return topic3_Q[i]
			i += 1
	elif cat == topic4:
		i = 0
		for x in amount:
			if amnt == x:
				return topic4_Q[i]
			i += 1
	elif cat == topic5:
		i = 0
		for x in amount:
			if amnt == x:
				return topic5_Q[i]
			i += 1
	else:
		return "You typed something incorrectly"

def getAnswer(cat, amnt):
	#if statements
	if cat == topic1:
		i = 0
		for x in amount:
			if amnt == x:
				return topic1_A[i]
			i += 1
	elif cat == topic2:
		i = 0
		for x in amount:
			if amnt == x:
				return topic2_A[i]
			i += 1
	elif cat == topic3:
		i = 0
		for x in amount:
			if amnt == x:
				return topic3_A[i]
			i += 1
	elif cat == topic4:
		i = 0
		for x in amount:
			if amnt == x:
				return topic4_A[i]
			i += 1
	elif cat == topic5:
		i = 0
		for x in amount:
			if amnt == x:
				return topic5_A[i]
			i += 1
	else:
		return "You typed something incorrectly"

def checkAnswer_p1(user_ans, ans, amnt):
	global guessed

	global currentPlayer
	i = 0
	for x in amount:
		if amnt == x:
			score = score_earned[i]
		i += 1
	if user_ans == ans:
		print("That is... CORRECT")
		currentPlayer = player1
		guessed = 1
	else:
		print("That is... WRONG")
		score = -score
		if guessed == 1:
			guessed = 0
		else:
			guessed = 1
	global p1_score
	p1_score = p1_score + score
	print(p1_score)

def checkAnswer_p2(user_ans, ans, amnt):
	global guessed
	global currentPlayer
	i = 0
	for x in amount:
		if amnt == x:
			score = score_earned[i]
		i += 1
	if user_ans == ans:
		print("That is... CORRECT")
		currentPlayer = player2
		guessed = 1
	else:
		print("That is... WRONG")
		score = -score
		if guessed == 1:
			guessed = 0
		else:
			guessed = 1
	global p2_score
	p2_score = p2_score + score
	print(p2_score)


def used_questions(cat, amnt):
	#if statements
	if cat == topic1:
		i = 0
		for x in amount:
			if amnt == x:
				global amount1
				amount1[i] = "--"				
			i += 1
	elif cat == topic2:
		i = 0
		for x in amount:
			if amnt == x:
				global amount2
				amount2[i] = "--"				
			i += 1
	elif cat == topic3:
		i = 0
		for x in amount:
			if amnt == x:
				global amount3
				amount3[i] = "--"				
			i += 1
	elif cat == topic4:
		i = 0
		for x in amount:
			if amnt == x:
				global amount4
				amount4[i] = "--"				
			i += 1
	elif cat == topic5:
		i = 0
		for x in amount:
			if amnt == x:
				global amount5
				amount5[i] = "--"				
			i += 1
	else:
		return "You typed something incorrectly"

def player2_turn(category, answer, amount):
	print colored(player2 + " answer the question", 'green', 'on_yellow')
	user_answer = raw_input("Answer: ")
	#function that checks answer
	checkAnswer_p2(user_answer, answer, amount)
	#function to cross of used questions on board
	used_questions(category, amount)

def player1_turn(category, answer, amount):
	print colored(player1 + " answer the question", 'blue', 'on_yellow')
	user_answer = raw_input("Answer: ")
	#function that checks answer
	checkAnswer_p1(user_answer, answer, amount)
	#function to cross of used questions on board
	used_questions(category, amount)

def match_category(cat):
	if cat == topic1:
		return 1
	elif cat == topic2:
		return 1
	elif cat == topic3:
		return 1
	elif cat == topic4:
		return 1
	elif cat == topic5:
		return 1
	return 0

def match_amount(amnt):
	i = 0
	for x in amount:
		if amnt == x:
			return 1				
		i += 1
	return 0

def choose_question():
	initialTable()
	category = raw_input("Choose Category: ")
	while match_category(category) == 0:
		category = raw_input("Doesn't match... Choose Category: ")
	amount = raw_input("Choose Amount: ")
	while match_amount(amount) == 0:
		amount = raw_input("Doesn't match... Choose Amount: ")

	print("\nYou chose " + category + " at " + amount)
	time.sleep(2)
	#call function, pass in category and amount, then it will return question
	#function contains if statments
	question = getQuestion(category, amount)
	answer = getAnswer(category, amount)
	#print(answer)#GET RID OF THISSSSSSS
	print("")
	counter = 5
	print("Buzz in...")
	time.sleep(2)
	while counter > 0:
		print("\t   " + str(counter))
		time.sleep(1)
		counter -= 1
	print("Your question is...  " + question)
	global lastCategory
	lastCategory = category
	global lastAnswer
	lastAnswer = answer
	global lastAmount
	lastAmount = amount
	keyInput(category, answer, amount)

	

def keyInput(cat, ans, amnt):
	#win = curses.initscr()
	#key = win.getch()
	print("Enter Key: ")
	#key = raw_input("Enter Key: ")
	#print("Enter Key: ")
	is_key = False
	while is_key == False:
		key = readchar.readchar()
		if key == 'a':
			is_key = True
		elif key == 'l':
			is_key = True

	if key == 'a':
		#player1
		player1_turn(cat, ans, amnt)
	elif key == 'l':
		#player2
		player2_turn(cat, ans, amnt)

#program start executing
print("")
player1 = raw_input("Player1 enter your name: ")
player2 = raw_input("Player2 enter your name: ")
print("")
instructions()

#for loop 25 times
n = 25
counter = 0

#global currentPlayer
currentPlayer = player1
guessed = 1
lastCategory = "none"
lastAmount = "none"
lastAnswer = "none"
#key pressed for turn
while counter < n:
	if guessed == 0:
		if currentPlayer == player1:
			player1_turn(lastCategory, lastAnswer, lastAmount)
		elif currentPlayer == player2:
			player2_turn(lastCategory, lastAnswer, lastAmount)
	else:
		print colored(player1 + "'s Score " + str(p1_score) + "\t\t" + player2 + "'s Score " + str(p2_score) + "\t", 'white' , 'on_green')
		print colored("\t\t" + currentPlayer + " choose a question\t\t", 'blue', 'on_white')
		choose_question()#player 1 selects first topic
		counter += 1

#program finishes executing
