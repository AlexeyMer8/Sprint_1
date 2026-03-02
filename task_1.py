time_string = '1h 45m,360s,25m,30m 120s,2h 60s'
time_list = time_string.split(',')
counter_minute = 0

for d in time_list:
    detail = d.split()
    for m in detail:
        if 'h' in m:
            hourse = int(m.replace('h', ''))
            counter_minute += hourse * 60
        elif 'm' in m:
            minute = int(m.replace('m', ''))
            counter_minute += minute
        else:
            second = int(m.replace('s', ''))
            counter_minute += int(second / 60)
print(counter_minute)

    