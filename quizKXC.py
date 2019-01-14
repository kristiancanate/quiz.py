q1A = False
q1U = int (0)
score = int (0)

print ("""Hello, and welcome to my one question quiz.
In this program, you will be asked one question and given four options
to choose from.
To answer, you will enter the number associated to the option.
When you are ready to answer the question, hit enter.""")
input ("")

while q1A == False:
    try:
        print ("""Which of the following is my favorite color?
1) Blue
2) Red
3) Green
4) Yellow""")
        q1U = int (input ("Your answer: "))
        print ("")
        if q1U == 2:
            score += 1
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

print ("You got", score*100, "% out of 100%.")
