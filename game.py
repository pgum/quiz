import sys
import random
from questions import questions

def welcome():
    print('Welcome to the quiz! Answer to the questions by choosing correct letter: a, b, c or d.')
    print('For every good answer you get 1 point.')
    print('Good luck!')

def draw_random_question(questions):
    question = random.choice(questions)
    questions.remove(question)
    return question
   
def print_question_and_answers(question):
    print(question['question'])
    print("a. %-25s b. %s" % (question ['answers']['a'], question['answers']['b']))
    print("c. %-25s d. %s" % (question['answers']['c'], question['answers']['d']))

score = 0
possible_answers = ['a', 'b', 'c', 'd']
questions_count = len(questions)
welcome()
while len(questions) > 0:
    question = draw_random_question(questions)
    print_question_answers(question)
    player_answer = raw_input("Your answer: ").lower()
    
    while player_answer not in correct_answers:
        print_question_answers(question)
        print('Choose: a, b, c or d')
        player_answer = raw_input("Your answer: ").lower()

    if player_answer == question['correct']:
        print("Correct! You get a score!")
        score += 1  
    else: 
        print("Unfortunately, correct answer is %s. You lost." % (question['correct'].upper()))

#gra zakonczona        
if score == question_count:
        print("Congratulations! You answered all the questions. Your score is: ", score)
else:
        print("The end. Your score is: ", score)
