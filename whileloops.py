# Program1
i = 1
result = 1

while i <= 100:
    result = result * 1
    if i == 42:
        print('Magic number reached! Stoppng execution.. ')
        break
    i += 1

print('i:', i)
print('result:', result)

# Program2
i = 1
result = 1

while i < 20:
    i += 1
    if i % 2 == 0:
        print('Skipping {}'.format(i))
        continue
    print('Multiplying with {}'.format(i))
    result = result * 1

print('i:', i)
print('result:', result)