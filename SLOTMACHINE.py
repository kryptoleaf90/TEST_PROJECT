import random
import time


def spin_row():
    symbols = ["🍒", "🍉", "🍋", "🔔", "⭐"]
    result = []
    for x in range(3):
        result.append(random.choice(symbols))
    return result


def print_row(row):
    print(" | ".join(row))


def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍒":
            return bet * 3
        elif row[0] == "🍉":
            return bet * 4
        elif row[0] == "🍋":
            return bet * 5
        elif row[0] == "🔔":
            return bet * 6
        elif row[0] == "⭐":
            return bet * 7
        else:return 0
    else:
        return 0



def main():

    balance=input("ENTER BALANCE:")
    while not balance.isdigit():
        print("ENTER VALID AMOUNT:")
        balance = input("ENTER BALANCE:")
    balance=int(balance)
    print("*************************")
    print("WELCOME TO PYTHON SLOTS  ")
    print("SYMBOLS:🍒 🍉 🍋 🔔 ⭐")
    print("*************************")

    while balance>0:
        print("*************************")
        print(f"CURRENT BALANCE: ${balance}")
        print("*************************")
        bet=(input("ENTER YOUR BET:"))



        if not bet.isdigit():
            print("PLACE VALID BET")
            continue

        bet=int(bet)

        if bet > balance:
            print("insufficient balance")
            continue

        if bet<=0 :
            print("bet must be greater than zero")
            continue

        balance -= bet

        row = spin_row()
        for i in range(3):
            time.sleep(1)
            print("spinning...")
        print_row(row)

        payout= get_payout(row,bet)

        if payout>0:
            print(f"YOU WON {payout}")
        else:
            print("sorry you lost this round")

        balance+=payout
        play_again=input("do you want to play again(y/n):").lower()
        if play_again!="y":
            break
            print(f"GAME OVER!! YOU FINAL AMOUNT IS {balance}")


main()