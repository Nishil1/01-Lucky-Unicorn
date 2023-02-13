# This function asks the user whether they have played this game before
def yes_no(content):
    Instructions = "You can bet an amount from 1-10 dollars, each game costs 1 dollar and a token" \
                   "will be randomly generated where you could win nothing, 50 cents or 5 dollars."
    while True:
        question = input(content).lower()
        no = ["no", "n"]
        yes = ["yes", "y"]

        if question in no:
            print(Instructions)
            return question
        elif question in yes:
            return question
        else:
            print("Please enter yes or no")

# Function checks the amount spend is a valid whole integer between 1-10
def num_check(response):
    while True:
        try:
            amount = int(input(response))

            if 10>= amount >=1:
                print("You have asked to play with ${}".format(amount))
                return response
            else:
                print("Please enter a number between 1 and 10")
        except ValueError:
            print("Please enter a whole integer")
# Main routine starts here

played_before = yes_no("Have you played this game before? ")
already_played = num_check("How much would you like to play with? ")