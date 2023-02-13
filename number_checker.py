def num_check(response):
    while True:
        try:
            amount = int(input(response))

            if amount <= 10 and amount>= 1:
                print("You have asked to play with ${}".format(amount))
                return response
            else:
                print("Please enter a number between 1 and 10")
        except ValueError:
            print("Please enter a whole integer")




