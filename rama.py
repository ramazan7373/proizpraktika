print('(1 задание)')
for x in range(1, 101):
    if x % 3 == 0 and x % 5 == 0:
        print('FizzBuzz')
    elif x % 3 == 0:
        print('Fizz')
    elif x % 5 == 0:
        print('Buzz')
    else:
        print(x)
print('')

print('(2 задание)')
daw = sorted([1, 4, 6], key=lambda gr: gr==4)
own = sorted([11, 33, 22], key=lambda gr: gr==33)
print(daw)
print(own)
