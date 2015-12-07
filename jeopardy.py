#!/usr/bin/python
from prettytable import PrettyTable

topic1 = "America"
topic2 = "Japan"
topic3 = "Sports"
topic4 = "Nazo Nazo"
topic5 = "Music"

amount1 = "10"
amount2 = "20"
amount3 = "30"
amount4 = "40"
amount5 = "50"
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

score1 = 10
score2 = 20
score3 = 30
score4 = 40
score5 = 50

p1_score = 0
p2_score = 0

topic1_Q1 = "What is the capital of the United States?"
topic1_Q2 = "What is the longest river in America?"
topic1_Q3 = "Where does the name America come from?"
topic1_Q4 = "What country is north of America?"
topic1_Q5 = "What does USA stand for?"

topic1_A1 = "Washington"
topic1_A2 = "Mississippi"
topic1_A3 = "Amerigo Vespucci"
topic1_A4 = "Canada"
topic1_A5 = "United States of America"

topic2_Q1 = "What is Japan's country's song?"
topic2_Q2 = "What is the biggest lake in Japan?"
topic2_Q3 = "Who is on 5000 yen?"
topic2_Q4 = "When did the Kamakura Bakufu start?"
topic2_Q5 = "What is Japan's country's bird?"

topic2_A1 = "Kimigayo"
topic2_A2 = "Lake Biwa / Biwa-ko"
topic2_A3 = "Nitobe Inazo"
topic2_A4 = "1192"
topic2_A5 = "kiji"

topic3_Q1 = "How many members are on a soccer team?"
topic3_Q2 = "What is Hideo Nomo's uniform number?"
topic3_Q3 = "In tennis, what is the name of 0 points?"
topic3_Q4 = "Name 4 sports that don't use balls."
topic3_Q5 = "Where were the 1984 Olympics?"

topic3_A1 = "11"
topic3_A2 = "16"
topic3_A3 = "love"
topic3_A4 = "???"
topic3_A5 = "Los Angeles"

topic4_Q1 = "1, 2, 4, 8, 16, ?"
topic4_Q2 = "Z, Y, X, W, ?"
topic4_Q3 = "S, M, T, ?, T, F, S"
topic4_Q4 = "O, T, T, F, F, ?"
topic4_Q5 = "J, Y, K, A, N, ?, K"

topic4_A1 = "32"
topic4_A2 = "V"
topic4_A3 = "W"
topic4_A4 = "S"
topic4_A5 = "H"

topic5_Q1 = "Who are the members of Globe?"
topic5_Q2 = "Who sings 'Be With You'?"
topic5_Q3 = "Who sings 'Young Man'?"
topic5_Q4 = "How many keys are on a piano?"
topic5_Q5 = "What does SMAP stand for?"

topic5_A1 = "Keiko, Komuro Tetsuya, Marc Panther"
topic5_A2 = "Glay"
topic5_A3 = "Saijo Hideki"
topic5_A4 = "88"
topic5_A5 = "Sport Music Assemble People"

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
	print("To choose a topic and score, enter exactly what is typed on Board (capatilization)\n")

def getQuestion(cat, amnt):
	#if statements
	if cat == topic1:
		if amnt == amount1:
			return topic1_Q1
		elif amnt == amount2:
			return topic1_Q2
		elif amnt == amount3:
			return topic1_Q3
		elif amnt == amount4:
			return topic1_Q4
		elif amnt == amount5:
			return topic1_Q5
	elif cat == topic2:
		if amnt == amount1:
			return topic2_Q1
		elif amnt == amount2:
			return topic2_Q2
		elif amnt == amount3:
			return topic2_Q3
		elif amnt == amount4:
			return topic2_Q4
		elif amnt == amount5:
			return topic2_Q5
	elif cat == topic3:
		if amnt == amount1:
			return topic3_Q1
		elif amnt == amount2:
			return topic3_Q2
		elif amnt == amount3:
			return topic3_Q3
		elif amnt == amount4:
			return topic3_Q4
		elif amnt == amount5:
			return topic3_Q5
	elif cat == topic4:
		if amnt == amount1:
			return topic4_Q1
		elif amnt == amount2:
			return topic4_Q2
		elif amnt == amount3:
			return topic4_Q3
		elif amnt == amount4:
			return topic4_Q4
		elif amnt == amount5:
			return topic4_Q5
	elif cat == topic5:
		if amnt == amount1:
			return topic5_Q1
		elif amnt == amount2:
			return topic5_Q2
		elif amnt == amount3:
			return topic5_Q3
		elif amnt == amount4:
			return topic5_Q4
		elif amnt == amount5:
			return topic5_Q5
	else:
		return "You typed something incorrectly"

def getAnswer(cat, amnt):
	#if statements
	if cat == topic1:
		if amnt == amount1:
			return topic1_A1
		elif amnt == amount2:
			return topic1_A2
		elif amnt == amount3:
			return topic1_A3
		elif amnt == amount4:
			return topic1_A4
		elif amnt == amount5:
			return topic1_A5
	elif cat == topic2:
		if amnt == amount1:
			return topic2_A1
		elif amnt == amount2:
			return topic2_A2
		elif amnt == amount3:
			return topic2_A3
		elif amnt == amount4:
			return topic2_A4
		elif amnt == amount5:
			return topic2_A5
	elif cat == topic3:
		if amnt == amount1:
			return topic3_A1
		elif amnt == amount2:
			return topic3_A2
		elif amnt == amount3:
			return topic3_A3
		elif amnt == amount4:
			return topic3_A4
		elif amnt == amount5:
			return topic3_A5
	elif cat == topic4:
		if amnt == amount1:
			return topic4_A1
		elif amnt == amount2:
			return topic4_A2
		elif amnt == amount3:
			return topic4_A3
		elif amnt == amount4:
			return topic4_A4
		elif amnt == amount5:
			return topic4_A5
	elif cat == topic5:
		if amnt == amount1:
			return topic5_A1
		elif amnt == amount2:
			return topic5_A2
		elif amnt == amount3:
			return topic5_A3
		elif amnt == amount4:
			return topic5_A4
		elif amnt == amount5:
			return topic5_A5
	else:
		return "You typed something incorrectly"

def checkAnswer_p1(user_ans, ans, amnt):
	

	if user_ans == ans:
		print("That is... CORRECT")
		if amnt == amount1:
			score = score1
		elif amnt == amount2:
			score = score2
		elif amnt == amount3:
			score = score3
		elif amnt == amount4:
			score = score4
		elif amnt == amount5:
			score = score5
	global p1_score
	p1_score = score

def used_questions(cat, amnt):
	#if statements
	if cat == topic1:
		if amnt == amount1:
			global amount1_1
			amount1_1 = "--"
		elif amnt == amount2:
			return topic1_Q2
		elif amnt == amount3:
			return topic1_Q3
		elif amnt == amount4:
			return topic1_Q4
		elif amnt == amount5:
			return topic1_Q5
	elif cat == topic2:
		if amnt == amount1:
			return topic2_Q1
		elif amnt == amount2:
			return topic2_Q2
		elif amnt == amount3:
			return topic2_Q3
		elif amnt == amount4:
			return topic2_Q4
		elif amnt == amount5:
			return topic2_Q5
	elif cat == topic3:
		if amnt == amount1:
			return topic3_Q1
		elif amnt == amount2:
			return topic3_Q2
		elif amnt == amount3:
			return topic3_Q3
		elif amnt == amount4:
			return topic3_Q4
		elif amnt == amount5:
			return topic3_Q5
	elif cat == topic4:
		if amnt == amount1:
			return topic4_Q1
		elif amnt == amount2:
			return topic4_Q2
		elif amnt == amount3:
			return topic4_Q3
		elif amnt == amount4:
			return topic4_Q4
		elif amnt == amount5:
			return topic4_Q5
	elif cat == topic5:
		if amnt == amount1:
			return topic5_Q1
		elif amnt == amount2:
			return topic5_Q2
		elif amnt == amount3:
			return topic5_Q3
		elif amnt == amount4:
			return topic5_Q4
		elif amnt == amount5:
			return topic5_Q5
	else:
		return "You typed something incorrectly"
	initialTable()

def player1():
	initialTable()
	print("JEOPARDY")
	print("Player 1")
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
	#now player2
	player2()
	


#program start executing
instructions()
player1()

#program finishes executing
