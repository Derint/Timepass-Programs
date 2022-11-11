import os
from time import sleep
from turtle import bk


def marquee(text, bkwd=True, time=0.0253):
    i = 0
    size = os.get_terminal_size()
    while i < size[0]:
        calc = i
        if bkwd:
            calc = size[0]-i-len(text)-5

        txt2 = f'\r{" ".ljust(calc)}{text}'
        if calc < 0 and bkwd:
            break
        if not (len(txt2) < size[0] or bkwd):
            break
        print(txt2, end=' ')
        i += 1
        sleep(time)
    print(f'\r {" "*(len(txt2)+5)}', end=' ')


for _ in range(10):
    marquee('Hello', False, 0.04)
    marquee("Derint here", time=0.04)
