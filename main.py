# I do not want to make this without OOP anymore 

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
habit_counts = {}

sad = ":("
not_bad = ":3"
great = ":D!"

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
                print("In the following table, prepare to find the ID of the habit! ... \n")
                time.sleep(1)
                display_log(HABITS)
                time.sleep(1)
                id = input("\nEnter the ID of the habit you'd like to track:\n>> ")
                confirm = input("\nDid you really complete this habit? (y/n)").lower()
                if confirm == "y":
                    track_habit(id)
                elif confirm == "n":
                    print("Nothing to track then! :D")
                    time.sleep(1)
                else: 
                    raise ValueError
                print("\nHere are your new stats!")
                display_log(HABITS)
                display_counts(habit_counts)
            elif command == "v":
                print("Okay!! ...\n")
                time.sleep(1)
                display_log(HABITS)
                time.sleep(2)
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
    habit_counts[habit_id] = 0

    with open(HABITS, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(new_habit)
    print("***** New habit created successfully! *****")
    print(f"Name: {habit_name}\nDescription: {habit_description}\n")
    time.sleep(1)


def track_habit(habit_id):
    if habit_id in habit_counts:
        habit_counts[habit_id] += 1
    else: 
        raise ValueError


def display_log(file_path):
    titled = False

    print("-" * 60)
    print(f"| {'YOUR EXISTING HABITS:':56} |")
    print("-" * 60)
    with open(file_path, "r") as f:
        content = csv.reader(f)
        for row in content:
            print(f"| {row[0]:16} | {row[1]:24} | {row[2]:10} |")
            if not titled:
                print("-" * 60)
                titled = True
    print("-" * 60)


def display_counts(habit_counts):
    smiley = None
    for key, value in habit_counts.items():
        if value == 0: smiley = sad
        elif value >= 1: smiley = not_bad
        elif value > 5: simley = great

        print(f"You completed habit with the ID '{key}' {value} times {smiley}.")


if __name__ == "__main__":
    main()