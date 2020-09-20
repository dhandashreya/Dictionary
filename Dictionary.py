import json
from difflib import get_close_matches
# load JSON data
data = json.load(open("data_dict.json"))
print("WELCOME TO ENGLISH DICTIONARY")


def dictionary(w):
    w = w.lower()    # word will be converted in lowercase

    # if word is present in JSON data then it's meaning will be given
    if w in data:
        return data[w]

    # if exact word isn't found so it's closest match will be given
    elif len(get_close_matches(w, data.keys())) > 0:
        new_word = input("Did you mean % s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0])
        new_word = new_word.lower()  # y and n will be in lowercase only
        if new_word == "y":
            print("Meaning of your word is:- ")
            return data[get_close_matches(w, data.keys())[0]]  # if user is satisfied with the new word given
        elif new_word == "n":
            return "The word doesn't exist. Please check again."  # if user isn't satisfied with the new word given
        else:
            return "We didn't understand your entry."  # if user has given an entry except for y and n
    else:
        return "The word doesn't exist. Please check again."


def get_meaning():
    # taking word from user
    word = input("Enter word: ")
    output = dictionary(word)

    # if our output is in a list
    if type(output) == list:
        for item in output:
            print(item)
    else:
        print(output)  # if our output is a string
    print()
    print("Do you want to exit: press n for no or for any other choice, dictionary will stop")
    choice = input()
    choice = choice.lower()
    if choice == "n":
        get_meaning()
    else:
        exit()


if __name__ == "__main__":
    get_meaning()
