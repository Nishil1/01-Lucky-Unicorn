import random

# This function asks the user whether they have played this game before
def display_instructions(question):
    Instructions = "You can bet an amount from 1-10 dollars, each game costs 1 dollar and a token" \
                   "will be randomly generated where you could win nothing, 50 cents or 5 dollars."
    while True:
        response = input(question).lower()
        no = ["no", "n"]
        yes = ["yes", "y"]

        if response in no:
            print(Instructions)
            break;
        elif response in yes:
            break;
        else:
            print("Please enter yes or no")



# Function checks the amount spend is a valid whole integer between 1-10

def get_intitial_betting_amount(question):
    while True:
        try:
            amount = float(input(question))

            if 10>= amount >=1:
                print("You have asked to play with ${}".format(amount))
                return amount
            else:
                print("Please enter a number between 1 and 10")
        except ValueError:
            print("Please enter a whole integer")


def start_game(input_string,initialBalance):
    round =1;
    currentBalance = initialBalance

    while True:
        print("Round: ", round)
        currentBalance = generate_random_token(initialBalance, currentBalance)
        if currentBalance < 1:
            break;
        response = input(input_string);
        if response == "":
            round= round + 1;
        else:
            break;




    print("Your final balance is {}.Thanks for playing!".format(currentBalance))








def generate_random_token(starting_balance,current_balance):

    for item in range(0, 1):
        chosen_number = random.randint(1, 100)
        # Increases Balance by 4 - if random number is between 1-5(unicorn)
        if 1 <= chosen_number <= 5:
            chosen = "unicorn"
            current_balance += 4


        # Decreases Balance by 1 - if random number is between 6-36(donkey)
        elif 6 <= chosen_number <= 36:
            chosen = "donkey"
            current_balance -= 1


        else:
            # Decreases Balance by 0.5 - if random number is outside boundaries of unicorn and donkey and is even
            if chosen_number % 2 == 0:
                chosen = "horse"
                current_balance -= 0.5

            else:
                # Decreases Balance by 0.5 - if random number is outside boundaries of unicorn and donkey and is odd

                chosen = "zebra"
                current_balance -= 0.5

        print("You got a {}, your balance is {}".format(chosen, current_balance))
            # Displays starting balance`

    # Displays End Balance

    return current_balance





# Main routine starts here

display_instructions("Have you played this game before? ")
amount = get_intitial_betting_amount("How much money would you like to bet? ")
start_game("Press <enter> to start playing or 'xxx' to quit", amount)





