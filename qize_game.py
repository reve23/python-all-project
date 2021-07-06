print("Welcome to Essential console quize")

start = input("Do you want to play?: ")
if start.lower() != "yes":
    quit()
print("Let's play")
score = 0
print("Score : " + str(score))
answer = input('''
Which language is more old? python or java?
Answer: ''')
if answer.lower() == "java":
    print("correct")
    score += 1
else:
    print("incorrect")
    
answer = input('''
We uses python for data science and machine learning. Which on is a machine learning library?
scikit-learn or django?
Answer: ''')
if answer.lower() == "scikit-learn":
    print("correct")
    score += 1
else:
    print("incorrect")
answer = input('''
java is a _____?_____ based language?oop or assembly?
Answer: ''')
if answer.lower() == "oop":
    print("correct")
    score +=1
else:
    print("incorrect")
answer = input('''
nodejs is __________ of javascript?
Answer: ''')
if answer.lower() == "runtime":
    print("correct")
    score +=1
else:
    print("incorrect")


print("Your total score: " + str(score))
print("You got: " + str((score/4)*100)+"%")
