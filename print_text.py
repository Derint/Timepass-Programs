from random import randint, random
from time import sleep
import os
from argparse import ArgumentParser

def get_args():
    parser = ArgumentParser()
    parser.add_argument("-t", "--text", dest="text", help="Input Text of String.")
    parser.add_argument("-s", "--sleep", dest="sleep", help="Time for next word to be printed.")
    return parser.parse_args()


def getLetter(x, s, wait):
    global counter
    while True:
        r_no = randint(30, 125)
        print(f'\r  [*]  Generating your text here :: {s}{chr(r_no)}', end='')
        if chr(r_no) == '\n':
            os.system('cls')
            print('\n\n')
        if x == chr(r_no):
            break
        sleep(wait)
        counter-=-1


try:
    counter = 0
    print('\n')
    ags = get_args()
    skip_chars = ['~', '\n', ' ']
    
    string = input("  [>]  Your Text Here :: ") if ags.text is None else ags.text
    time = input("  [>]  Time to sleep :: ") if ags.sleep is None else ags.sleep
    
    if time == '':
        time = (0.001*random())*randint(1, 90)
    time = float(time)

    if None in  [ags.text, ags.sleep]:print('\n')

    for i in range(len(string)):
        if string[i] in skip_chars:continue
        getLetter(string[i], string[:i], abs(time))

    print('\r'+" "*(len(string)*10), end='')
    print(f'\r  [+]  Generated Text :: {string}')
    print(f'  [~]  Loop Ran : {counter} time(s).')
    print('\n')

except KeyboardInterrupt:
    print('\r'+" "*(len(string)*10), end='')
    print(f'\r  [~]  Exiting Now ....... ')
    sleep(1)
    os.system('cls')
    exit()

except Exception as e:
    print("\n !! EXCEPTION OCCURED : ", e)
    exit()