import time
import random
print('welcome to the roullete game!')
while True:   
    num_of_players = int(input('How many players are you(1-5)? '))
    if num_of_players < 1 or num_of_players > 5:
        print('The amount of players needs to be between 1 and 5')
    else:
        print(f"You are {num_of_players} players, let's start!")
        break
stats = {}
for i in range(1, num_of_players + 1):
    stats[f"player_{i}"] = 100
print(stats)

Red = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,0]
Black = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,0]


def game_of_roullete(a):
    while True:
        bet_of_player = int(input(f"How much would player_{a} like to bet? "))
        number_of_bet = input(f"On what number do you want to bet {bet_of_player}$? ")
        if number_of_bet.lower() in ['red','black'] or Red or Black:
            stats[f"player_{a}"] -= bet_of_player
            what_user_wants = input('What would you like to do? ')
            if what_user_wants.lower() in ['play','spin']:
                Red_choice = random.choice(Red)
                Black_choice = random.choice(Black)
                spin = [Red_choice,Black_choice]
                number = random.choice(spin)
                print('Spinning...')
                time.sleep(1.25)
                print('The number is...')
                time.sleep(0.5)
                if number == 0:
                    print(number)
                elif number in Red:
                    print(f"{number} Red")
                else:
                    print(f"{number} Black")
                if number_of_bet.lower() == 'red':
                    if number == 0:
                        print(f"player_{a} was wrong.")
                        print(stats)
                        break
                    if number in Red:
                        print(f"player_{a} was right!")
                        stats[f"player_{a}"] = 2 * bet_of_player 
                        print(stats)
                        break
                    else:
                        print(f"player_{a} was wrong.")
                        print(stats)
                        break
                elif number_of_bet.lower() == 'black':
                    if number == 0:
                        print(f"player_{a} was wrong.")
                        print(stats)
                        break
                    elif number in Black:
                        print(f"player_{a} was right!")
                        stats[f"player_{a}"] += 2 * bet_of_player
                        print(stats)
                        break
                    else:
                        print(f"player_{a} was wrong.")
                        print(stats)
                        break
                elif number_of_bet in Red or Black:
                    if number == number_of_bet:
                        print(f"No way!player_{a} won")
                        stats[f"player_{a}"] += 3 * bet_of_player
                        print(stats) 
                        break
                    else:
                        print(f"player_{a} lost.")
                        del stats[f"player_{a}"]
                        print(stats)
                        break
                  
                    
            elif what_user_wants.lower() in ['quit','stop','exit']:
                print(f'{what_user_wants}{what_user_wants[-1]}ing...')
                time.sleep(1)
                break
            else:
                print(f"'{what_user_wants}' is an invalid command.") 
                print("you can either write spin/play to spin the roullete or quit/stop/exit to stop the game.")
        else:
            print(f"That is not a number in our roullete, print a real number.")
while True:
    for i in range(1,num_of_players + 1):
        game_of_roullete(i)
