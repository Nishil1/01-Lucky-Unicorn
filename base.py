import random


# This function asks the user whether they have played this game before
def display_instructions(question):
    instructions = "You can bet an amount from 1-10 dollars, each game costs 1 dollar and a token "
    instructions_i = "will be randomly generated where you could win nothing if you get "
    instructions_ii = "a donkey, 50 cents if you get a horse or 5 dollars if your lucky and get a unicorn."
    while True:
        response = input(question).lower()

        if response == "no" or response == "n":
            print()
            statement_generator("How to Play", "*")
            print(instructions)
            print(instructions_i)
            print(instructions_ii)
            break
        elif response == "yes" or response == "y":
            break
        else:
            print("Please enter yes or no")
# Function checks the amount spend is a valid whole integer between 1-10


def get_initial_betting_amount(question):
    while True:
        try:
            response = float(input(question))

            if 10 >= response >= 1:
                print("You have asked to play with ${:.2f}".format(response))
                return response
            else:
                print("Please enter a number between 1 and 10")
        except ValueError:
            print("Please enter a whole integer")


# This function  checks whether user balance has not gone below
# 1 or over 10 and uses the "generate random token" function to generate a token.
def start_game(input_string, initial_balance):
    rounds = 0
    current_balance = initial_balance

    while True:

        if current_balance < 1:
            break
        response = input(input_string)
        if response == "":
            rounds = rounds + 1
            print()
            statement_generator("Round {}".format(rounds), ".")
            current_balance = generate_random_token(current_balance)
        else:
            break

    statement_generator("Results", "=")
    print("Your final balance is ${:.2f}. ".format(current_balance))
    print("Thanks for playing!")


# Function generates a random token and is combined with the "start_game" function
# to make sure the user has enough money to play.
def generate_random_token(current_balance):
    for item in range(0, 1):
        chosen_number = random.randint(1, 100)
        # Increases Balance by 4 - if random number is between 1-5(unicorn)
        if 1 <= chosen_number <= 5:
            chosen = "unicorn"
            current_balance += 4
            prize_decoration = "!"

        # Decreases Balance by 1 - if random number is between 6-36(donkey)
        elif 6 <= chosen_number <= 36:
            chosen = "donkey"
            current_balance -= 1
            prize_decoration = "D"
        else:
            # Decreases Balance by 0.5 - if random number is outside boundaries of unicorn and donkey and is even
            if chosen_number % 2 == 0:
                chosen = "horse"
                current_balance -= 0.5
                prize_decoration = "H"

            else:
                # Decreases Balance by 0.5 - if random number is outside boundaries of unicorn and donkey and is odd

                chosen = "zebra"
                current_balance -= 0.5
                prize_decoration = "Z"
        outcome = ("You got a {}, your balance is ${:.2f}".format(chosen, current_balance))
        statement_generator(outcome, prize_decoration)
        # Displays starting balance

    # Displays End Balance

    return current_balance


# Main routine starts here
def statement_generator(statement, decoration):
    sides = decoration * 3

    statement = "{} {} {}".format(sides, statement, sides)
    top_bottom = decoration * len(statement)
    print(top_bottom)
    print(statement)
    print(top_bottom)
    print()
    return ""


statement_generator("Welcome to Lucky Unicorn Game", "*")
display_instructions("Have you played this game before? ")
print()
statement_generator("Lets get Started...", "-")
print()
print()
get_amount = get_initial_betting_amount("How much money would you like to bet? ")
print()
print()
start_game("Press <enter> to start playing or 'xxx' to quit", get_amount)
