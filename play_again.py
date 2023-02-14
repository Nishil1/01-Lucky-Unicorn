balance = int(input("How much would you like to play with? "))

rounds_played = 0


while rounds_played < balance:
    #ask question
    play_again = input("Press <enter> to play again or type xxx to quit")
    # loop
    if play_again == "":
        import random

        # Main routine
        STARTING_BALANCE = 100

        balance = STARTING_BALANCE
        # Generates token 20 times
        for item in range(0, 20):
            chosen_number = random.randint(1, 100)
            # Increases Balance by 4 - if random number is between 1-5(unicorn)
            if 1 <= chosen_number <= 5:
                chosen = "unicorn"
                balance += 4

            # Decreases Balance by 1 - if random number is between 6-36(donkey)
            elif 6 <= chosen_number <= 36:
                chosen = "donkey"
                balance -= 1


            else:
                # Decreases Balance by 0.5 - if random number is outside boundaries of unicorn and donkey and is even
                if chosen_number % 2 == 0:
                    chosen = "horse"
                    balance -= 0.5

                else:
                    # Decreases Balance by 0.5 - if random number is outside boundaries of unicorn and donkey and is odd

                    chosen = "zebra"
                    balance -= 0.5
            print("You got a {}, your balance is {}".format(chosen, balance))
            # Displays starting balance
        print("Starting Balance: ${}".format(STARTING_BALANCE))
        # Displays End Balance
        print("Final Balance: ${:.2f}".format(balance))
     rounds_played += 1
    print(rounds_played)
    elif play_again == "xxx":
        quit()
print("Sorry you dont have enough money")