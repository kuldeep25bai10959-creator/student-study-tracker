import json

file_name = "study_data.json"

def load_data():
    try:
        with open(file_name, "r") as file:
            return json.load(file)
    except:
        return []

def save_data(data):
    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)

def add_session():
    subject = input("Enter subject: ")
    hours = float(input("Enter study hours: "))

    data = load_data()

    session = {
        "subject": subject,
        "hours": hours
    }

    data.append(session)
    save_data(data)

    print("Study session saved!")

def show_total():
    data = load_data()

    total = 0

    for session in data:
        total += session["hours"]

    print("Total study hours:", total)

while True:

    print("\n1. Add Study Session")
    print("2. Show Total Hours")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_session()

    elif choice == "2":
        show_total()

    elif choice == "3":
        break

    else:
        print("Invalid choice")