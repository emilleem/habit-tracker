import time
import random
import os


MENU = '''\033[1mWhat do you want to do (Q/q to quit)?\033[0m
                1. Add new habit (A/a)
                2. Track existing habit (T/t)
                3. View habit log (V/v)'''

HABITS = "habits.json"

existing_ids = []

def main():
    if not os.path.isfile(HABITS):
         f = open(HABITS, "x")
         f.close()
    
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
                id = generate_habit_id()
                create_habit(id, new_habit, description)
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
            

def generate_habit_id():
    while True:
        id = "#"
        for _ in range(3):
            id += random.choice("0123456789")
        
        if id not in existing_ids:
            existing_ids.append(id)
            return id


def create_habit(habit_id, habit_name, habit_description):
    pass


def track_habit(habit_id):
    pass


def display_log():
    pass


def display_short_log():
    pass


if __name__ == "__main__":
    main()