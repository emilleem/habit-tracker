# I do not want to make this without OOP anymore 

import csv
import habit
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
habits = []

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
                name = input("Very well! Name your new habit:\n>> ")
                description = input("Enter a habit description:\n>> ")
                new_habit = habit.Habit(name, description, generate_unique_id())
                print("\nGenerated new habit!\n")
                print(new_habit.__str__())
                time.sleep(1)
                
                habits.append(new_habit)
            elif command == "t":
                pass
            elif command == "v":
                pass
            elif command == "q":
                break
            else:
                raise ValueError
            

def generate_unique_id():
    while True:
        id = ""
        for _ in range(3):
            id += random.choice("0123456789")
        
        if id not in existing_ids:
            existing_ids.append(id)
            return id


if __name__ == "__main__":
    main()