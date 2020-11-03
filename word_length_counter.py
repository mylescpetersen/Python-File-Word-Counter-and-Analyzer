#!/bin/env python3

# For sys.argv
import sys
# For math.ceil, math.floor
import math

# Global list of data class objects
data_list = []

# Class to hold the lengths, counts and sets of unique words
class data:

    def __init__(self, length):
        self.length = length
        self.count = 0
        self.words = set()

    def increment_count(self):
        self.count += 1


# Initializes array with all possible word length objects
def populate():
    global data_list
    for i in range(1,35):
        data_list.append(data(i))

def main():
    global data_list
    populate()
    check_args()


# Checks to see which arguments are passed and tries to find given file path
def check_args():
    SORT_ARG = False
    PRINT_WORDS_ARG = False

    # Not enough args to have an input file
    if len(sys.argv) < 3:
        print("program: missing '--infile <filename> [--sort] [--print-words]'\n")
        return

    # Checks if last arg is --infile --> no valid file
    if sys.argv[-1] == "--infile":
        print("program: missing '--infile <filename> [--sort] [--print-words]'\n")
        return

    # Checks args for --sort and --print-words
    for i in range(len(sys.argv)):

        # Checks if arg following --infile is --sort or --print-words, if yes print "no file"
        if sys.argv[i] == "--infile" and i != len(sys.argv):

            # Arg following --infile is not --sort or --print-words, saves that arg as path var
            if sys.argv[i +1] != "--sort" and sys.argv[i +1] != "--print-words":
                path = sys.argv[i + 1]

            else:
                # Arg following --infile is --sort or --print-words
                print("program: missing '--infile <filename> [--sort] [--print-words]'\n")
                return

            # Checks if file path is valid
            if check_file(path) == 0:
                return

        if sys.argv[i] == "--sort":
            SORT_ARG = True

        if sys.argv[i] == "--print-words":
            PRINT_WORDS_ARG = True


    # Determines which print function to use based off args given

    if PRINT_WORDS_ARG and SORT_ARG:
        print_sort_words()

    elif PRINT_WORDS_ARG:
        print_words()

    elif SORT_ARG:
        print_sort()

    else:
        print_basic()


# Checks if given path is valid (only runs is a path is given)
def check_file(path):
    # Chars to remove from file
    chars = '.,;()'

    try:
        file = open(path, "r")

    except FileNotFoundError:

        print("unable to open \'" + path + "\' for reading\n")
        return 0

    for line in file:
        # Removes unwanted chars from each line
        for i in chars:
            line = line.replace(i, ' ')

        # Sends each word to be put into data object array
        for word in line.split():
            classify(word)




# Assigns every individual word to its respective data instance
def classify(word):
    global data_list

    for cur_data in data_list:

        if len(word) == cur_data.length:

            cur_data.increment_count()
            cur_data.words.add(word)



# ------------- Helper functions for print (all take in global data_list) ------------------


# Sorts lengths based off of count
def sort_data(li):
    li.sort(key=lambda length: length.count, reverse=True)


# Prints the basic output (no sorting or words)
def print_output(li):
    for item in li:
        if item.count!=0:
            print("Count[%02d]=%02d;"% (item.length,item.count))


# Calculates median
def print_median(li):
    lengths = set()
    for i in li:
        if i.count != 0:
            lengths.add(i.length)
    lengths_list = list(lengths)

    # Odd number of unique lengths (median is middle length)
    if len(lengths_list) % 2 !=0:
        median = lengths_list[int(len(lengths_list) / 2)]
        median = float(median)
        print("Median word length:",median)

    # Even number of unique lengths (median is average of 2 middle lengths)
    else:
        med1 = math.floor(lengths_list[int(len(lengths_list) / 2)])
        med2 = math.ceil(lengths_list[int(len(lengths_list) / 2) - 1])

        median = (med1 + med2) / 2
        print("Median word length:", median)


# Formats all unique words and prints them
def get_words(li):

    for item in li:
        if item.count!=0:
            cur_words = list(sorted(item.words))
            words_string = ""
            for i in range(len(cur_words)):

                # Checks if second to last/last word
                if i < len(cur_words) - 1:
                    # Is not second to last/last word
                    words_string = words_string + "\"" + cur_words[i] + "\"" + ", "

                else:
                    # Is second to last/last word
                    if len(cur_words) != 1:

                        # Removes the added "," from string
                        words_string = words_string[:-2]
                        words_string = words_string + " "

                        # Adds "and" for last element
                        words_string = words_string +  "and " + "\"" + cur_words[-1] + "\""


                    # Only one word for given length
                    else:
                        words_string = "\"" + cur_words[i] + "\""

            print("Count[%02d]=%02d;"% (item.length,item.count), "(words:",words_string + ")")


# -------------- End of printing helper functions -----------------



# ------------ Printing functions based off args given -------------


# No --sort or --print-words
def print_basic():
    global data_list
    print_output(data_list)
    return

# Just --sort
def print_sort():
    global data_list
    sort_data(data_list)
    print_output(data_list)
    print_median(data_list)
    return


# Just --print-words
def print_words():
    global data_list
    get_words(data_list)
    return


# Both --sort and --print-words
def print_sort_words():
    global data_list
    sort_data(data_list)
    get_words(data_list)
    return


# -------------- End of printing functions -----------------


#Do not change this
if __name__ == "__main__":
    main()

    
