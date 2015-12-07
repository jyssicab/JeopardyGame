#!/usr/bin/python
from prettytable import PrettyTable

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


amount1_1 = "10"
amount2_1 = "20"
amount3_1 = "30"
amount4_1 = "40"
amount5_1 = "50"
amount1_2 = "10"
amount2_2 = "20"
amount3_2 = "30"
amount4_2 = "40"
amount5_2 = "50"
amount1_3 = "10"
amount2_3 = "20"
amount3_3 = "30"
amount4_3 = "40"
amount5_3 = "50"
amount1_4 = "10"
amount2_4 = "20"
amount3_4 = "30"
amount4_4 = "40"
amount5_4 = "50"
amount1_5 = "10"
amount2_5 = "20"
amount3_5 = "30"
amount4_5 = "40"
amount5_5 = "50"


score_earned = [10,20,30,40,50]

p1_score = 0
p2_score = 0


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
	x.add_column(topic1, [amount1_1, amount2_1, amount3_1, amount4_1, amount5_1])
	x.add_column(topic2, [amount1_2, amount2_2, amount3_2, amount4_2, amount5_2])
	x.add_column(topic3, [amount1_3, amount2_3, amount3_3, amount4_3, amount5_3])
	x.add_column(topic4, [amount1_4, amount2_4, amount3_4, amount4_4, amount5_4])
	x.add_column(topic5, [amount1_5, amount2_5, amount3_5, amount4_5, amount5_5])
	print x.get_string(header=True, border=True)

def instructions():
	print("To choose a topic and score, enter exactly what is typed on Board (capatilization)")
	print("Returning champion selected topic first")
	print("Buzz in to answer quesiton")
	print(player1 + " use key r\n" + player2 + " use key a\n" + player3 + " use key l\n")

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
	

	if user_ans == ans:
		print("That is... CORRECT")
		
		i = 0
		for x in amount:
			if amnt == x:
				score = score_earned[i]
			i += 1
	else:
		print("That is... WRONG")
		score = 0
	global p1_score
	p1_score = p1_score + score
	print(p1_score)

def checkAnswer_p2(user_ans, ans, amnt):
	

	if user_ans == ans:
		print("That is... CORRECT")
		i = 0
		for x in amount:
			if amnt == x:
				score = score_earned[i]
			i += 1
	else:
		print("That is... WRONG")
		score = 0
	global p2_score
	p2_score = p2_score + score
	print(p2_score)

def used_questions(cat, amnt):
	#if statements
	if cat == topic1:
		if amnt == amount1:
			global amount1_1
			amount1_1 = "--"
		elif amnt == amount2:
			global amount2_1
			amount2_1 = "--"
		elif amnt == amount3:
			global amount3_1
			amount3_1 = "--"
		elif amnt == amount4:
			global amount4_1
			amount4_1 = "--"
		elif amnt == amount5:
			global amount5_1
			amount5_1 = "--"
	elif cat == topic2:
		if amnt == amount1:
			global amount1_2
			amount1_2 = "--"
		elif amnt == amount2:
			global amount2_2
			amount2_2 = "--"
		elif amnt == amount3:
			global amount3_2
			amount3_2 = "--"
		elif amnt == amount4:
			global amount4_2
			amount4_2 = "--"
		elif amnt == amount5:
			global amount5_2
			amount5_2 = "--"
	elif cat == topic3:
		if amnt == amount1:
			global amount1_3
			amount1_3 = "--"
		elif amnt == amount2:
			global amount2_3
			amount2_3 = "--"
		elif amnt == amount3:
			global amount3_3
			amount3_3 = "--"
		elif amnt == amount4:
			global amount4_3
			amount4_3 = "--"
		elif amnt == amount5:
			global amount5_3
			amount5_3 = "--"
	elif cat == topic4:
		if amnt == amount1:
			global amount1_4
			amount1_3 = "--"
		elif amnt == amount2:
			global amount2_4
			amount2_4 = "--"
		elif amnt == amount3:
			global amount3_4
			amount3_4 = "--"
		elif amnt == amount4:
			global amount4_4
			amount4_4 = "--"
		elif amnt == amount5:
			global amount5_4
			amount5_4 = "--"
	elif cat == topic5:
		if amnt == amount1:
			global amount1_5
			amount1_5 = "--"
		elif amnt == amount2:
			global amount2_5
			amount2_5 = "--"
		elif amnt == amount3:
			global amount3_5
			amount3_5 = "--"
		elif amnt == amount4:
			global amount4_5
			amount4_5 = "--"
		elif amnt == amount5:
			global amount5_5
			amount5_5 = "--"
	else:
		return "You typed something incorrectly"

def player2_turn():
	initialTable()
	#print("JEOPARDY")
	print(player2)
	category = raw_input("Choose Category: ")
	amount = raw_input("Choose Amount: ")
	print("\nYou chose " + category + " at " + amount)
	#call function, pass in category and amount, then it will return question
	#function contains if statments	
	question = getQuestion(category, amount)
	answer = getAnswer(category, amount)
	print(answer)
	print("Your question is...  " + question)
	user_answer = raw_input("Answer: ")
	#function that checks answer
	checkAnswer_p2(user_answer, answer, amount)
	#function to cross of used questions on board
	used_questions(category, amount)

def player1_turn():
	initialTable()
	#print("JEOPARDY")
	print(player1)
	category = raw_input("Choose Category: ")
	amount = raw_input("Choose Amount: ")
	print("\nYou chose " + category + " at " + amount)
	#call function, pass in category and amount, then it will return question
	#function contains if statments	
	question = getQuestion(category, amount)
	answer = getAnswer(category, amount)
	print(answer)
	print("Your question is...  " + question)
	user_answer = raw_input("Answer: ")
	#function that checks answer
	checkAnswer_p1(user_answer, answer, amount)
	#function to cross of used questions on board
	used_questions(category, amount)
	


#program start executing
player1 = raw_input("Returning Champion enter your name: ")
player2 = raw_input("Player1 enter your name: ")
player3 = raw_input("Player2 enter your name: ")

instructions()

#for loop 25 times
n = 25
counter = 1
#player1_turn()
#key pressed for turn
while counter < n:
	player1_turn()
	player2_turn()
	counter += 1

#program finishes executing
