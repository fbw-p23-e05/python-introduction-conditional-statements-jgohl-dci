which = str(input('Input the scale shortcut you d like to convert (F - Fahrenheit, C - Celsius): '))
which = which.capitalize()

if which == 'C' or which == 'F':
    temp = int(input('Input the value of temperature you d like to convert: '))

    if which == 'C':
        print('The temperature in Fahrenheit is:', int(temp * (9 / 5) + 32), 'degrees.')
    elif which == 'F':
        print('The temperature in Celsius is:', int((temp - 32) * (5 / 9)), 'degrees.')
else:
    print('Incorrect input')
