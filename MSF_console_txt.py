from time import sleep
from os import get_terminal_size, system, name


def print_msf_txt(string, i, wait=0.5)   :
    pre_str, cap_str, nxt_str = '', '', ''
    cap_str = string[i].upper()
    
    if string[i] == ' ':return
    if string[i] == '.': cap_str = '∙'
        
    if i == 0:
        nxt_str = string[i+1:].lower()
    else:
        pre_str = string[:i].lower()
        nxt_str = string[i+1:].lower()
    print(f"\r{' '.center(7)}{pre_str}{cap_str}{nxt_str}", end='')
    sleep(wait)
    

def backspace():
    print("\r" + ' '*(get_terminal_size()[0]-10), end='')



string = input("\n  [>]  Enter a Text : ")  #"Hello World ...." #
print()
try:
    i=0
    while True:    
        print_msf_txt(string, i%len(string), 0.4)
        i+=1
except KeyboardInterrupt:
    backspace()
    print('\r  [~]  Exiting ...')
    sleep(1)
    system('cls' if name in ['nt', 'dos'] else 'clear')


"""
pre_str, cap_str, nxt_str = '', '', ''
for i in range(len(string)):
    cap_str = string[i].upper()
    if string[i] == ' ':continue
    if string[i] == '.': cap_str = '∙'
        
    if i == 0:
        nxt_str = string[i+1:].lower()
    else:
        pre_str = string[:i].lower()
        nxt_str = string[i+1:].lower()
    print(f"\r{pre_str}{cap_str}{nxt_str}", end='')
    sleep(0.5)
print(f"\r{string}")
"""