import random
import time
import os


class colors:
    reset = '\033[0m'
    bold = '\033[01m'
    disable = '\033[02m'
    underline = '\033[04m'
    reverse = '\033[07m'
    strikethrough = '\033[09m'
    invisible = '\033[08m'

    class fg:
        black = '\033[30m'
        red = '\033[31m'
        green = '\033[32m'
        orange = '\033[33m'
        blue = '\033[34m'
        purple = '\033[35m'
        cyan = '\033[36m'
        lightgrey = '\033[37m'
        darkgrey = '\033[90m'
        lightred = '\033[91m'
        lightgreen = '\033[92m'
        yellow = '\033[93m'
        lightblue = '\033[94m'
        pink = '\033[95m'
        lightcyan = '\033[96m'

    class bg:
        black = '\033[40m'
        red = '\033[41m'
        green = '\033[42m'
        orange = '\033[43m'
        blue = '\033[44m'
        purple = '\033[45m'
        cyan = '\033[46m'
        lightgrey = '\033[47m'


emojis = ["🍓", "🍎", "🍉", "🍇", "🍒", "🍊", "🍋", "🍑", "🍌", "🥝", "🥭", "🍍", "🍈", "🍏", "🍐", "🥑", "🥥", "🍬", "💰", "✨"]


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def spin_animation():
    for _ in range(10):
        for _ in range(3):
            print(random.choice(emojis), end=' ')
        print()
        time.sleep(0.1)
        clear_screen()


def print_rules():
    print(f"{colors.fg.green}{colors.bold}Game Rules:{colors.reset}")
    print("1. Enter your initial balance.")
    print("2. Choose a bet amount for each spin.")
    print("3. Choose a multiplier (1 or 2):")
    print("   - Multiplier 1: You win, lose, or stay with your bet amount.")
    print("   - Multiplier 2: If you win, you get double your bet as a reward, if you lose you lose the possible profit of your bet twice.")
    print("4. Special rewards if you get three consecutive emojis from these (🍬, 💰, ✨):")
    print("   - Three 🍬: Your bet multiplied by 5.")
    print("   - Three 💰: Your bet multiplied by 10.")
    print("   - Three ✨: JACKPOT of 2500 $!")
    print("5. If you get two matching emojis, you keep your balance and don't lose anything.")
    print("6. If you get only one emoji, you lose your bet.")
    print(f"{colors.fg.cyan}{colors.bold}Good luck!{colors.reset}")


def casino_game():
    print_rules()
    balance = float(input("Enter your initial balance: "))
    clear_screen()
    
    while balance > 0:
        print(f"\nYour current balance is: {balance:.2f} $")
        bet = float(input("Enter your bet: "))
        
        if bet > balance:
            print("Insufficient balance! Try again.")
            continue

        multiplier = int(input("Choose a multiplier (1 or 2): "))
        
        if multiplier not in [1, 2]:
            print("Invalid multiplier! Try again.")
            continue

        total_bet = bet * multiplier
        
        if total_bet > balance:
            print("Insufficient balance! Try again.")
            continue

        balance -= total_bet
        print(f"{colors.fg.orange}Spinning the slot machine...{colors.reset}")
        spin_animation()
        
        result = [random.choice(emojis) for _ in range(3)]
        print(" | ".join(result))

        if result[0] == result[1] == result[2]:
            if result[0] == "🍬":
                win = total_bet * 5
            elif result[0] == "💰":
                win = total_bet * 10
            elif result[0] == "✨":
                win = 2500
            else:
                win = total_bet * 2
            print(f"{colors.fg.green}Congratulations! You won {win:.2f} ${colors.reset}")
            balance += win
        elif result[0] == result[1] or result[1] == result[2] or result[0] == result[2]:
            print(f"{colors.fg.yellow}You got your bet back: {total_bet:.2f} ${colors.reset}")
            balance += total_bet
        else:
            print(f"{colors.fg.red}Unfortunately, you lost your bet.{colors.reset}")
        
        if balance <= 0:
            print("Your balance is 0 $. The game is over.")
            break

        continue_game = input("Do you want to play again? (yes/no): ").lower()
        if continue_game != 'yes':
            break    
    print(f"Your final balance is: {balance:.2f} $. Thank you for playing!")


casino_game()