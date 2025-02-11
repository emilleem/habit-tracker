import time


MENU = '''\033[1mWhat do you want to do (Q/q to quit)?\033[0m
                1. Add new habit (A/a)
                2. Track existing habit (T/t)
                3. View habit log (V/v)'''


def main():
    print("***** Welcome to the silly goofy habit tracker! *****")
    time.sleep(1)
    print("The creator of this habit tracker is learning, so please do not judge. \n") 
    time.sleep(1)

    run_tracker()


def run_tracker():
    while True:
            print(MENU)
            command = input("\n>> ").lower()
            print()

            if command == "a":
                new_habit = input("Very well! Name your new habit:\n>> ")
                description = input("Enter a habit description:\n>> ")
                create_habit(new_habit, description)
            elif command == "t":
                display_short_log()
                id = input("Enter the ID of the habit you'd like to track:\n>> ")
                track_habit(id)
            elif command == "v":
                display_log()
            elif command == "q":
                break
            else:
                raise ValueError
            

def create_habit(habit_name, habit_description):
     pass


def track_habit(habit_id):
     pass


def display_log():
     pass


def display_short_log():
     pass


if __name__ == "__main__":
    main()