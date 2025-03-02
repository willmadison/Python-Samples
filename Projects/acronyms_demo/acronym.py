# NOTE: This version uses an array to store the first 
# letter of each word

def get_acronym(phrase):
    initials = []
    acronym = ""

    # Strip off the first letter of each word
    for word in phrase.split():
        if word not in ["a", "an", "the", "of"]:
            # In the special case of the word "without" the initials 
            # should always be 'W' and 'O'
            if word.casefold() == "without":
                initials.append('W')
                initials.append('O')
            else:
                initials.append(word[0])

    acronym = ".".join(initials) + "."

    return acronym.upper()


if __name__ == "__main__":
    phrase = input("\nPlease type in a phrase or full organizational name:\n")
    print("\nThe acronym for \"{}\" is {}\n".format(phrase, get_acronym(phrase)))
