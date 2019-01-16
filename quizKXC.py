#score = int (0)
def run_quest (quest,check,ansU,ansR):
    print (quest)
    while check == False:
        try:
            ansU = int (input ("Your answer: "))
            print ("")
            if ansU == ansR:
                #score += 1
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

q1T = """Which of the following is my favorite color?
1) Blue
2) Red
3) Green
4) Yellow"""
q1C = False
q1U = int (0)
q1R = 2

q2T = """Which one of these pets have I previously owned?
1) Spider
2) Dog
3) Snake
4) Lizard"""
q2C = False
q2U = int (0)
q2R = 4

print ("""Hello, and welcome to my one question quiz.
In this program, you will be asked one question and given four options
to choose from.
To answer, you will enter the number associated to the option.
When you are ready to answer the question, hit enter.""")
input ("")

run_quest (q1T,q1C,q1U,q1R)
run_quest (q2T,q2C,q2U,q2R)

#print ("You got", score*50, "% out of 100%.")
