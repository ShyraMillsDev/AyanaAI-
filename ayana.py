from ayana_ai.talk import ask_ayana

if __name__ == "__main__":
    user_input = input("What do you want to tell Ayana? ")
    reply = ask_ayana(user_input)
    print("\nAyana says:\n" + reply)