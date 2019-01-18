from quizDataKXC import *
score = int (0)

def run_quest (quest,check,ansU,ansR):
    print (quest)
    while check == False:
        try:
            ansU = int (input ("Your answer: "))
            print ("")
            if ansU == ansR:
                global score
                score += 1
                check = True
            elif 0 < ansU < 5:
                check = True
            else:
                print ("""That was not one of the options. Please input a positive
integer from 1 to 4.
""")
        except ValueError:
            print ("""
That's not even an integer!
""")

print ("""Hello, and welcome to my one question quiz.
In this program, you will be asked one question and given four options
to choose from.
To answer, you will enter the number associated to the option.
When you are ready to answer the question, hit enter.""")
input ("")

run_quest (q1T,q1C,q1U,q1R)
run_quest (q2T,q2C,q2U,q2R)
run_quest (q3T,q3C,q3U,q3R)
run_quest (q4T,q4C,q4U,q4R)
run_quest (q5T,q5C,q5U,q5R)
run_quest (q6T,q6C,q6U,q6R)
run_quest (q7T,q7C,q7U,q7R)
run_quest (q8T,q8C,q8U,q8R)
run_quest (q9T,q9C,q9U,q9R)
run_quest (q10T,q10C,q10U,q10R)

print ("You got", score*10, "% out of 100%.")

if -1 < score < 5:
    print ("Who are you and why are you taking this quiz?")
elif 4 < score < 8:
    print ("""Alright cool, so you know about me.
You must either be my friend or really observant.""")
elif 7 < score < 11:
    print ("You know a little bit too much about me...")
