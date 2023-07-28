#Title AASCII

print("""

 __       __                                __                            __         ______             __            __ 
|  \     /  \                              |  \                          |  \       /      \           |  \          |  \
| $$\   /  $$  ______    ______   __    __ | $$  ______   _______    ____| $$      |  $$$$$$\ __    __  \$$ ________ | $$
| $$$\ /  $$$ |      \  /      \ |  \  |  \| $$ |      \ |       \  /      $$      | $$  | $$|  \  |  \|  \|        \| $$
| $$$$\  $$$$  \$$$$$$\|  $$$$$$\| $$  | $$| $$  \$$$$$$\| $$$$$$$\|  $$$$$$$      | $$  | $$| $$  | $$| $$ \$$$$$$$$| $$
| $$\$$ $$ $$ /      $$| $$   \$$| $$  | $$| $$ /      $$| $$  | $$| $$  | $$      | $$ _| $$| $$  | $$| $$  /    $$  \$$
| $$ \$$$| $$|  $$$$$$$| $$      | $$__/ $$| $$|  $$$$$$$| $$  | $$| $$__| $$      | $$/ \ $$| $$__/ $$| $$ /  $$$$_  __ 
| $$  \$ | $$ \$$    $$| $$       \$$    $$| $$ \$$    $$| $$  | $$ \$$    $$       \$$ $$ $$ \$$    $$| $$|  $$    \|  \
 \$$      \$$  \$$$$$$$ \$$       _\$$$$$$$ \$$  \$$$$$$$ \$$   \$$  \$$$$$$$        \$$$$$$\  \$$$$$$  \$$ \$$$$$$$$ \$$
                                 |  \__| $$                                              \$$$                            
                                  \$$    $$                                                                              
                                   \$$$$$$                                                                               

""")

#Counter Values for Correct Answer

correct = 0

#Tuple for Correct and Incorrect Answers

questions = ("Q1: The capitol of Maryland is Baltimore",
             "Q2: The largest city in Maryland is Cumberalnd",
             "Q3: Maryland borders Virginia")

answers = ("F", "F", "T")

#For questions in index print out questions

for index in range(len(questions)):

#Set index values and re-set values

  userAnswer = ""

  question = questions[index]

  correctAnswer = answers[index]

#Display Question

  print(question)
  print()

#Ask for input from user in while loop with counter
  
  while (userAnswer != "T" and userAnswer != "F"):
    userAnswer = input("Enter T or F: ")
    print()
  
#Count correct answers based on while loop iterations

    if(userAnswer == correctAnswer):
      correct += 1

#Display results

print()
print(f"You got {correct} out of 3 correct!")
