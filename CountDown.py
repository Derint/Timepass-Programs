from time import sleep

Time = input("  [>]  Enter Time (HH:MM:SS) :: ")

temp = Time.split(':')

h, m, s = 0, 0, 0

if len(temp) == 3:
    h, m, s = int(temp[0]), int(temp[1]), int(temp[2])
elif len(temp) == 2:
    m, s = int(temp[0]), int(temp[1])
elif len(temp) == 1:
    s = int(temp[0])
else:
    print("  [!]  Invalid Input ")
    exit()


if m and not 0 <= m <= 59:
    print("  [!]  Invalid Minute")
    exit()

if s and not 0 <= s <= 59:
    print("  [!]  Invalid Second")
    exit()

if s == 0:
    s = 59

t_h, t_m, t_s = str(h), str(m), str(s)

# print(f"  H : {h}, M : {m}, S: {s}, {s and not 0<= s<=59}")
# exit()
try:
    while h or m or s:
        t_h, t_m, t_s = str(h), str(m), str(s)

        if int(m) < 10:
            t_m = f'0{m}'
        if int(s) < 10:
            t_s = f'0{s}'
        if int(h) < 10:
            t_h = f'0{h}'

        print(f'\r  [*]  Count-Down  {t_h}:{t_m}:{t_s}', end='')
        s -= 1
        if s == 0:
            if m or h:
                s = 59
            if m > 0:
                m -= 1

        if m == 0 and h:
            m = 59

            if h:
                h -= 1

        sleep(1)

    print(f'\r       Count-Down  {t_h}:{t_m}:00', end='')
    sleep(0.005)
    print(f"\r {' '*50}", end='')
    print("\r  [+]  Time's Up  ")

    import winsound
    duration = 500  # milliseconds
    freq = 700  # Hz
    for i in range(8):
        winsound.Beep(freq, duration)

except KeyboardInterrupt:
    print(f'\r {" "*8}', end='')
    print('\r  [~]  Stopping Countdown now...')
    sleep(1)
