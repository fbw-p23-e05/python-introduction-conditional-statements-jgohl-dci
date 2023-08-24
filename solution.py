import math

# Task 1
user_input1 = int(input('Enter a number: '))
user_input2 = int(input('Enter a number: '))
user_input3 = int(input('Enter a number: '))


if user_input1 == user_input2 and user_input1 == user_input3:
    print('The triple sum is: ', user_input1 * 3)
else:
    print('The sum is: ', user_input1 + user_input2 + user_input3)



# Task 2
user_input1 = int(input('Enter a number: '))
user_input2 = int(input('Enter a number: '))

if user_input1 > user_input2:
    print('The result of calculation is: ', (user_input1 - user_input2) * 2)
else:
    print('The result of calculation is: ', abs(user_input2 - user_input1))



# Task 3
user_input1 = int(input('Enter a number: '))

if user_input1 % 2 == 0:
    print(user_input1, 'is an even number.')
else:
    print(user_input1, 'is an odd number.')



# Task 4
user_input1 = float(input('Input the radius of a circle: '))
area = (user_input1 ** 2) * math.pi

print('The area of the circle with radius', user_input1, 'is', round(area, 2))
