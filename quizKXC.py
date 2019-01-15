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

q1A = False
q2A = False
q1U = int (0)
q2U = int (0)
#score = int (0)

print ("""Hello, and welcome to my one question quiz.
In this program, you will be asked one question and given four options
to choose from.
To answer, you will enter the number associated to the option.
When you are ready to answer the question, hit enter.""")
input ("")

print ("""Which of the following is my favorite color?
1) Blue
2) Red
3) Green
4) Yellow""")
while q1A == False:
    try:
        q1U = int (input ("Your answer: "))
        print ("")
        if q1U == 2:
            #score += 1
            q1A = True
        elif 0 < q1U < 5:
            q1A = True
        else:
            print ("""That was not one of the options. Please input a positive
integer from 1 to 4.
""")
    except ValueError:
        print ("""
That's not even an integer!
""")

print ("""Which one of these pets have I previously owned?
1) Spider
2) Dog
3) Snake
4) Lizard""")
while q2A == False:
    try:
        q2U = int (input ("Your answer: "))
        print ("")
        if q2U == 4:
            #score += 1
            q2A = True
        elif 0 < q2U < 5:
            q2A = True
        else:
            print ("""That was not one of the options. Please input a positive
integer from 1 to 4.
""")
    except ValueError:
        print ("""
That's not even an integer!
""")

#print ("You got", score*50, "% out of 100%.")
