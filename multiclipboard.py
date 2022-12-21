import sys
import clipboard
import json

SAVED_DATA = "clipboard.json"

def save_content(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)

def load_content(filepath):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            return data
    except:
        return {}

if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_content(SAVED_DATA)
    if command == "save":
        key = input("Enter a Key: ")
        data[key] = clipboard.paste()
        save_content(SAVED_DATA, data)
        print("Data Saved!")

    elif command == "load":
        key = input("Enter a Key: ")
        if key in data:
            clipboard.copy(data[key])
            print("Data copied to clipboard.")
        else:
            print("Key does not exit.")

    elif command == "list":
        print(data)

    else:
        print("unkown command")
else:
    print("Please pass exactly one command")
