# JeopardyGame

Pre-Instructions:
1. Install prettytable with su -c "easy_intall prettytable"
2. Install termcolor with su -c "easy_intall termcolor"
3. Install readchar with su -c "easy_intall readchar"

This is a 2 player game.

INSTRUCTIONS
1. In terminal,
	$python jeopardy.py
2. Type in a name.
3. Player1 chooses the first category and worth.
4. After 5 seconds the question is displayed.
5. Player1 buzz in with key 'a', Player2 key 'l'.
	The goal is to know the answer and press the key first.
6. Enter the answer all LOWERCASE. It will be checked and the point value will be rewarded or deducted.
	All answers are one word.
7. If answer is correct, then the current player continues to choose the category.
	If get wrong, then other player gets chance to answer.
	If both get it wrong, then last player to got the answer correct chooses next category.
8. Do not type in a category amount if it has already been used.
