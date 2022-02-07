import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

patterns = [rock , paper , scissors]

print("0 for rock & 1 for paper & 2 for scissors")
user = int(input("Enter your choise : "))
computer = random.randint(0,2)
if (user==computer):
    print ("your choise : \n"+patterns[user] + '\n'+"computer choise : \n"+ patterns[computer] + '\n' + "its  a draw")
elif(user == 0 and computer==2):
    print("your choise : \n"+patterns[user] + '\n'+"computer choise : \n"+ patterns[computer] + '\n' + "you won")
elif (computer==0 and user==2):
    print("your choise : \n"+patterns[user] + '\n'+"computer choise : \n"+ patterns[computer] + '\n' + "computer won")
elif(user == 2 and computer==1):
    print("your choise : \n"+patterns[user] + '\n'+"computer choise : \n"+ patterns[computer] + '\n' + "you won")
elif (computer==2 and user==1):
    print("your choise : \n"+patterns[user] + '\n'+"computer choise : \n"+ patterns[computer] + '\n' + "computer won")
elif(user == 1 and computer==0):
    print("your choise : \n"+patterns[user] + '\n'+"computer choise : \n"+ patterns[computer] + '\n' + "you won")
elif (computer==1 and user==0):
    print("your choise : \n"+patterns[user] + '\n'+"computer choise : \n"+ patterns[computer]+ '\n' + "computer won")

'''
        *****Rules*****
1- Rock wins against scissors.
2- Scissors win against paper.
3- Paper wins against rock.
'''