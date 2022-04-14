import random
import datetime

# create dictionary to map each word to its respective key
words = open("words.txt")
dict_words = {}

for line in words:
    line = line.strip()

    if line[0] in dict_words:
        dict_words[line[0]].append(line)
    else:
        dict_words[line[0]] = list()
        dict_words[line[0]].append(line)

# making a list for days to build tuples and map characters 
days = []
for i in range(1, 27):
    days.append(i)


def get_word_of_the_day(day):
    # if day is 27, it'll correspond to 1, if day is 28, it'll correspond to 2, therefore:
    if day > 26:
        day = day - 26

    # mapped each day to their corresponding character
    words_mapped = list(zip(days, dict_words.keys()))

    # to properly access the correct tuple, I had to subtract user input by 1 since index starts at 0
    word_tuple = words_mapped[day - 1]

    # accessing the key value that corresponds to the user input, in its respective tuple
    get_letter = word_tuple[1]

    # now that the list is accessed, just need to randomize which item in the list to get
    return random.choice(dict_words.get(get_letter))


if __name__ == '__main__':
    print(get_word_of_the_day(12))

    print(get_word_of_the_day(datetime.datetime.today().day))
