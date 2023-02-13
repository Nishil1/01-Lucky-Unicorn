
def yes_no(content):
    while True:
        question = input(content).lower()
        no = ["no", "n"]
        yes = ["yes", "y"]

        if question in no:
            print("Show Instructions")
            return question

        elif question in yes:
            return question
        else:
            print("Please enter yes or no")

played_before = yes_no("Have you played this game before? ")