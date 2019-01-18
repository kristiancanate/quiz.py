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

q3T = """What is my favorite number?
1) 4
2) 28
3) 16
4) 7"""
q3C = False
q3U = int (0)
q3R = 1

q4T = """Which of these 'Lil' rappers do I like the most?
1) Lil Yachty
2) Lil Pump
3) Lil Skies
4) Lil Uzi Vert"""
q4C = False
q4U = int (0)
q4R = 4

q5T = """Which of these devices do I prefer to play on?
1) Xbox
2) Switch
3) PlayStation
4) PC"""
q5C = False
q5U = int (0)
q5R = 3

q6T = """Which of these pasta varieties is my favorite?
1) Macaroni
2) Lasagna
3) Spaghetti
4) Fettuccine"""
q6C = False
q6U = int (0)
q6R = 2

q7T = """Which of these video game series is my favorite?
1) Halo
2) Grand Theft Auto
3) Mortal Kombat
4) Call of Duty"""
q7C = False
q7U = int (0)
q7R = 4

q8T = """Which is my favorite season?
1) Spring
2) Summer
3) Fall
4) Winter"""
q8C = False
q8U = int (0)
q8R = 3

q9T = """Which of these sodas do I prefer to drink?
1) Mountain Dew
2) Sprite
3) Crush
4) Dr Pepper"""
q9C = False
q9U = int (0)
q9R = 1

q10T = """Which Doritos flavor is my favorite?
1) Spicy Sweet Chili
2) Cool Ranch
3) Nacho Cheese
4) Spicy Nacho"""
q10C = False
q10U = int (0)
q10R = 2

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
