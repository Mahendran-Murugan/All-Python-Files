import random


def rock_paper_scissor():
    d = {'R': "ROCK", 'P': 'PAPER', "S": "SCISSOR"}
    choices = ['ROCK', 'PAPER', 'SCISSOR']
    usr_points = 0
    com_points = 0
    while com_points < 10 and usr_points < 10:
        print("Options are\nr: ROCK\np: PAPER\ns: SCISSOR")
        usr_choice = input("Enter your choice:").upper()
        try:
            print("Your choice is :", d[usr_choice])
        except Exception as e:
            print("Enter a valid Input")
            continue
        com_choice = random.choice(choices)
        print("Computer choice is :", com_choice)
        if d[usr_choice] == 'ROCK':
            if d[usr_choice] == com_choice:
                print('Tie')
            elif com_choice == d['P']:
                print('Computer won')
                com_points += 1
            else:
                print('Player won')
                usr_points += 1
            print("Player\tComputer")
            print(usr_points, com_points, sep='\t\t')
            continue
        elif d[usr_choice] == 'PAPER':
            if d[usr_choice] == com_choice:
                print('Tie')
            elif com_choice == d['S']:
                print('Computer won')
                com_points += 1
            else:
                print('Player won')
                usr_points += 1
            print("Player\tComputer")
            print(usr_points, com_points, sep='\t')
            continue
        else:
            if d[usr_choice] == com_choice:
                print('Tie')
            elif com_choice == d['R']:
                print('Computer won')
                com_points += 1
            else:
                print('Player won')
                usr_points += 1
            print("Player\tComputer")
            print(usr_points, com_points, sep='\t')
            continue
    else:
        print("Match Over")
        if usr_points > com_points:
            print("Player won the match")
        else:
            print("Computer won the match")


usr_in = input("Do you want to play 'ROCK PAPER SCISSOR'(y/n) ?").upper()
if usr_in == 'Y':
    rock_paper_scissor()
else:
    print("If you change your mind come here to play\nThank you")
