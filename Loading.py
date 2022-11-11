from time import sleep
a = ['-', '\\', '|', '/']

n = 5
while n > 0:
    for i in range(len(a)):
        print(f'\r  [*]  Loading  {a[i]}', end='')
        sleep(0.5)
    n -= 1
print(f'\r  {" "*20}', end='')
