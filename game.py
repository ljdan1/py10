'''

✊ rock wins against scissors 🤚
🤚 scissors win against paper ✌
✌ paper wins against rock ✊

# source: wrpsa.com/the-official-rules-of-paper-scissors/

'''

import random

rock = "✊"

paper = "🤚"

scissors = "✌"

print("--------------------------------------------------------------------------------")

your_choice=int(input('''                           choose your choice

                            enter 0 ->rock
                            enter 1 ->paper
                            enter 2 ->scissors

'''))

list = [rock,paper,scissors]

if your_choice>=3 or your_choice<0:

    print("please enter the valid number 0 1 or 2")
else:

    print('''You choose:
    ''',list[your_choice])
    computer_choice=random.randint(0,2)
    print('''Computer chooses:
    ''',list[computer_choice])


    if your_choice==0 and computer_choice==2:
        print("congratulations! 🎉 You win! 🎉")
    elif computer_choice==0 and your_choice==2:
        print("sorry another time 😥 You lose!")
    elif computer_choice > your_choice:
        print("sorry another time 😥 You lose!")
    elif computer_choice == your_choice:
        print("Ii is draw!😐 ")
    elif your_choice > computer_choice:
        print("congratulations! 🎉 You win! 🎉")
