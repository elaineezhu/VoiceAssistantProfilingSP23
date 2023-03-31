#!/usr/bin/env python3 

import argparse
import random

def main():
    parser = argparse.ArgumentParser(description= "Generate a secure, memorable password using the XKCD method")
    parser.add_argument("-w", "--words", help = "include WORDS words in the password (default=4)", dest = "WORDS", type = int, default = 4)
    parser.add_argument("-c", "--caps", help = "capitalize the first letter of CAPS random words (default=0)", dest = "CAPS", type = int, default = 0)
    parser.add_argument("-n", "--numbers", help = "insert NUMBERS random numbers in the password (default=0)", dest = "NUMBERS", type = int, default = 0)
    parser.add_argument("-s", "--symbols", help = "insert SYMBOLS random symbols in the password (default=0)", dest = "SYMBOLS", type = int, default = 0)
    args = parser.parse_args()

    # reads words and strips, then appends to WORDS list
    f = open("words.txt", "r")

    WORDS = []
    for line in f:
        stripped = line.strip()
        WORDS.append(stripped)
        
    f.close()

    password_list = []

    # handles capitalization argument
    for i in range(args.WORDS):
        if (args.CAPS > 0):
            password_list.append(random.choice(WORDS).capitalize())
            args.CAPS = args.CAPS - 1
        else:
            password_list.append(random.choice(WORDS))

    # handles numbers argument
    if args.NUMBERS > 0:
        NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        for i in range(args.NUMBERS):
            password_list.append(random.choice(NUMBERS))

    # handles symbols argument
    if args.SYMBOLS > 0:
        SYMBOLS = ['!', '@', '#', '$', '%', '^', '&', '*', '(' , ')' , '-', '+', '=', ':', ';', ',', '.', '?', '/']
        for i in range(args.SYMBOLS):
            password_list.append(random.choice(SYMBOLS))

    # shuffles the password list
    password = random.sample(password_list, len(password_list))

    print("".join(password))

if __name__== '__main__':
    main()