import random
import colorama
from colorama import Fore
colorama.init(autoreset=True)


rock = "Rock"
paper = "Paper"
scissors = "Scissors"
computer_move = ""
win_count = draw_count = lose_count = total_rounds = 0
is_won = False
is_lost = False

while True:
    if win_count == 2:
        is_won = True
        print(f"{Fore.GREEN}"+""*5+"You won!")
        break
    if lose_count == 2:
        is_lost = True
        print(f"{Fore.RED}You lost! Try again...")
        break
    player_move = input("Choose [r]ock, [p]aper, [s]cissors: ")
    computer_random_number = random.randint(1, 3)

    if player_move == "End":
        break
    if player_move == "r":
        player_move = rock
    elif player_move == "p":
        player_move = paper
    elif player_move == "s":
        player_move = scissors
    else:
        raise SystemExit("Invalid Input! Try again...")

    if computer_random_number == 1:
        computer_move = rock
    elif computer_random_number == 2:
        computer_move = paper
    elif computer_random_number == 3:
        computer_move = scissors

    if (player_move == rock and computer_move == scissors) \
            or (player_move == paper and computer_move == rock) \
            or (player_move == scissors and computer_move == paper):
        win_count += 1
        total_rounds += 1
    elif player_move == computer_move:
        draw_count += 1
        total_rounds += 1
    else:
        lose_count += 1
        total_rounds += 1
    print(f"{Fore.BLUE}You chose: {player_move}")
    print(f"{Fore.LIGHTGREEN_EX}Computer chose: {computer_move}")
print(f"{Fore.YELLOW}"+" "*5+"Total"+" game stats:")
print(f"{Fore.GREEN}Total games played: {total_rounds}\nRounds ended in Draw: {draw_count}")

