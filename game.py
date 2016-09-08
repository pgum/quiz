import random
from questions import questions

def print_welcome():
    print 'Welcome to the quiz! Answer to the questions by choosing correct letter: a, b, c or d.'
    print 'For every good answer you get 1 score.'
    print 'Good luck!'

def random_question(questions):
    question = random.choice(questions)
    questions.remove(question)
    return question
   
def print_question(question):
    print question['question']
    print "a. %-25s b. %s" % (question ['answers']['a'], question['answers']['b'])
    print "c. %-25s d. %s" % (question['answers']['c'], question['answers']['d'])

def get_answer(question):
    possible_answers = question['answers'].keys();
    player_answer = raw_input("Your answer: ").lower()
    while player_answer not in possible_answers:
        print 'Choose: %s' % ','.join(possible_answers)
        print_question(question)
        player_answer = raw_input("Your answer: ").lower()
    return player_answer

score = 0
questions_count = len(questions)

print_welcome()

while len(questions) > 0:
    question = random_question(questions)
    print_question(question)
    player_answer = get_answer(question)    

    if player_answer == question['correct']:
        print "Correct! You get a score!"
        score += 1  
    else:
        print "Unfortunately, correct answer is %s. You lost." % (question['correct'].upper())        
        break 

if score == questions_count:
    print 'Congratulations! You answered all the questions. Your score is: ', score
else: 
    print 'The end. Your score is: ', score
