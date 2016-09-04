import sys
import random
from questions import questions

def welcome():
    print 'Welcome to the quiz! Answer to the questions by choosing correct letter: a, b, c or d.'
    print 'For every good answer you get 1 score.'
    print 'Good luck!'

def random_question(questions):
    question = random.choice(questions)
    questions.remove(question)
    return question
   
def question_answer(question):
    print question['question']
    print "a. %-25s b. %s" % (question ['answers']['a'], question['answers']['b'])
    print "c. %-25s d. %s" % (question['answers']['c'], question['answers']['d'])


welcome()

score = 0
correct_answers = ['a', 'b', 'c', 'd']
should_drawn = True
questions_count = len(questions)

while len(questions) > 0:
    if should_drawn:
        question = random_question(questions)
        should_drawn = True
   
    question_answer(question)
    player_answer = raw_input("Your answer: ").lower()

    # checking if it is a correct answer
    if player_answer == question['correct']:
        print "Correct! You get a score!"
        score += 1  
        if score == questions_count:
            print 'Congratulations! You answered all the questions. Your score is: ', score
    elif player_answer not in correct_answers:
        print 'Choose: a, b, c or d' 
        should_drawn = False       
    else: 
        print "Unfortunately, correct answer is %s. You lost." % (question['correct'].upper())
        print 'The end. Your score is: ', score
        break 


# the end of game
sys.exit(0)