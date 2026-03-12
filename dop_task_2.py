def digit_root(num):
    while num >= 10:
        total = 0
        for digit in str(num):
            total += int(digit)
        num = total
    return num

print(digit_root(192932))