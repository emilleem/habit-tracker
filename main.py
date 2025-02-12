import csv
import time
import random
import os


MENU = '''\033[1mWhat do you want to do (Q/q to quit)?\033[0m
                1. Add new habit (A/a)
                2. Track existing habit (T/t)
                3. View habit log (V/v)'''

HABITS = "habits.csv"

# needs to be updated so that the program fetches data if there are already tracked habits
existing_ids = []
existing_habits = []

def main():
    if not os.path.isfile(HABITS):
         f = open(HABITS, "x")
         writer = csv.writer(f)
         writer.writerow(["Habit name", "Habit description", "Habit ID"])
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
                new_habit_description = input("Enter a habit description:\n>> ")
                create_habit(new_habit, new_habit_description, generate_habit_id())
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


def create_habit(habit_name, habit_description, habit_id):
    new_habit = [habit_name, habit_description, habit_id]

    existing_habits.append(new_habit)
    with open(HABITS, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(new_habit)
    print("***** New habit created successfully! *****")
    print(f"Name: {habit_name}\nDescription: {habit_description}\n")
    time.sleep(1)


def track_habit(habit_id):
    pass


def display_log():
    pass


def display_short_log():
    pass


if __name__ == "__main__":
    main()