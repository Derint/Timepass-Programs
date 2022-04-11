from random import randint, random
from time import sleep
import os


def getLetter(x, s, wait):
    while True:
        r_no = randint(30, 125)
        print(f'\r  [*]  Generating your text here :: {s}{chr(r_no)}', end='')
        if chr(r_no) == '\n':
            os.system('cls')
            print('\n\n')
        if x == chr(r_no):
            break
        sleep(wait)


try:
    print('\n')
    string = input("  [>]  Your Text Here :: ")
    time = input("  [>]  Time to sleep :: ")

    if time == '':
        time = (0.001*random())*randint(1, 90)
    else:
        time = float(time)
    print('\n')
    for i in range(len(string)):
        getLetter(string[i], string[:i], 0.102)
    print('\n\n')

except KeyboardInterrupt:
    print(f'\r{" "*30}  [~]  Exiting Now ....... ')
    exit()
    os.system('cls')
