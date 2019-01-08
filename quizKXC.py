answered = False
answer = int (0)
score = int (0)

print ("Hello, and welcome to my one question quiz.")
print ("In this program, you will be asked one question and given four options")
print ("to choose from.")
print ("To answer, you will enter the number associated to the option.")
print ("When you are ready to answer the question, hit enter.")
input ("")

while answered == False:
    try:
        print ("Which of the following is my favorite color?")
        print ("1) Blue")
        print ("2) Red")
        print ("3) Green")
        print ("4) Yellow")
        answer = int (input ("Your answer: "))
        print ("")
        if answer == 2:
            score += 1
            answered = True
        elif 0 < answer < 5:
            answered = True
        else:
            print ("That was not one of the options. Please input a positive")
            print ("integer from 1 to 4.")
            print ("")
    except ValueError:
        print ("")
        print ("That's not even an integer!")
        print ("")

print ("You got", score*100, "% out of 100%.")
