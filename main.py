import json
import os
from datetime import datetime

memory_file = "memory.json"

def load_memory():
    if os.path.exists(memory_file):
        with open(memory_file, "r") as f:
            return json.load(f)
    return {}

def save_memory(data):
    with open(memory_file, "w") as f:
        json.dump(data, f, indent=4)

memory = load_memory()

if "name" not in memory:
    memory["name"] = input("Enter your name: ")
    memory["favorite_language"] = input("Enter your favorite language: ")
    save_memory(memory)

print(f"\nHello {memory['name']}!")

while True:
    print("\n1. Show My Profile")
    print("2. Show Time")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print("\nUser Profile")
        print("Name:", memory["name"])
        print("Favorite Language:", memory["favorite_language"])

    elif choice == "2":
        print("Current Time:", datetime.now().strftime("%H:%M:%S"))

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid Choice")
