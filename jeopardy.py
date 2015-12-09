#!/usr/bin/python
from prettytable import PrettyTable
import time
from termcolor import colored

player1 = "Player1"
player2 = "Player2"
player3 = "Player3"

topic1 = "America"
topic2 = "Japan"
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
	"Where does the name America come from?", 
	"What country is north of America?", 
	"What does USA stand for?"]

topic1_A = ["Washington",
	"Mississippi",
	"Amerigo Vespucci",
	"Canada",
	"United States of America"]


topic2_Q = ["What is Japan's country's song?",
	"What is the biggest lake in Japan?",
	"Who is on 5000 yen?",
	"When did the Kamakura Bakufu start?",
	"What is Japan's country's bird?"]

topic2_A = ["Kimigayo",
	"Lake Biwa / Biwa-ko",
	"Nitobe Inazo",
	"1192",
	"kiji"]



topic3_Q = ["How many members are on a soccer team?",
	"What is Hideo Nomo's uniform number?",
	"In tennis, what is the name of 0 points?",
	"Name 4 sports that don't use balls.",
	"Where were the 1984 Olympics?"]

topic3_A = ["11",
	"16",
	"love",
	"???",
	"Los Angeles"]

topic4_Q = ["1, 2, 4, 8, 16, ?",
	"Z, Y, X, W, ?",
	"S, M, T, ?, T, F, S",
	"O, T, T, F, F, ?",
	"J, Y, K, A, N, ?, K"]

topic4_A = ["32",
	"V",
	"W",
	"S",
	"H"]

topic5_Q = ["Who are the members of Globe?",
	"Who sings 'Be With You'?",
	"Who sings 'Young Man'?",
	"How many keys are on a piano?",
	"What does SMAP stand for?"]

topic5_A = ["Keiko, Komuro Tetsuya, Marc Panther",
	"Glay",
	"Saijo Hideki",
	"88",
	"Sport Music Assemble People"]


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
	print(user_ans)
	print(ans)
	i = 0
	for x in amount:
		if amnt == x:
			score = score_earned[i]
		i += 1
	if user_ans == ans:
		print("That is... CORRECT")
	else:
		print("That is... WRONG")
		score = -score
	global p1_score
	p1_score = p1_score + score
	print(p1_score)

def checkAnswer_p2(user_ans, ans, amnt):
	i = 0
	for x in amount:
		if amnt == x:
			score = score_earned[i]
		i += 1
	if user_ans == ans:
		print("That is... CORRECT")
		i = 0
	else:
		print("That is... WRONG")
		score = -score
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

def player3_turn():
	user_answer = raw_input("Answer: ")
	#function that checks answer
	checkAnswer_p3(user_answer, answer, amount)
	#function to cross of used questions on board
	used_questions(category, amount)

def player2_turn(category, answer, amount):
	print colored(player2 + " answer the question", 'green')
	user_answer = raw_input("Answer: ")
	#function that checks answer
	checkAnswer_p2(user_answer, answer, amount)
	#function to cross of used questions on board
	used_questions(category, amount)

def player1_turn(category, answer, amount):
	print colored(player1 + " answer the question", 'blue')
	user_answer = raw_input("Answer: ")
	#function that checks answer
	checkAnswer_p1(user_answer, answer, amount)
	#function to cross of used questions on board
	used_questions(category, amount)

def choose_question():
	initialTable()
	category = raw_input("Choose Category: ")
	amount = raw_input("Choose Amount: ")
	print("\nYou chose " + category + " at " + amount)
	#call function, pass in category and amount, then it will return question
	#function contains if statments
	question = getQuestion(category, amount)
	answer = getAnswer(category, amount)
	print(answer)
	counter = 5
	print("Buzz in...")
	while counter > 0:
		print(counter)
		time.sleep(1)
		counter -= 1
	print("Your question is...  " + question)
	keyInput(category, answer, amount)

def keyInput(cat, ans, amnt):
	key = raw_input("Enter Key: ")
	if key[0] == 'a':
		#player1
		player1_turn(cat, ans, amnt)
	elif key[0] == 'l':
		#player2
		player2_turn(cat, ans, amnt)

#program start executing
player1 = raw_input("Player1 enter your name: ")
player2 = raw_input("Player2 enter your name: ")
#player3 = raw_input("Player3 enter your name: ")

instructions()

#for loop 25 times
n = 25
counter = 1


#key pressed for turn
while counter < n:
	print colored(player1 + " choose a question", 'blue', 'on_white')
	choose_question()#player 1 selects first topic
	print colored(player2 + " choose a question", 'green', 'on_white')
	choose_question()#player 1 selects first topic
	#print(player3 + " choose a question")
	#choose_question()#player 1 selects first topic
	#player1_turn()
	#player2_turn()
	#player3_turn()
	counter += 1

#program finishes executing
