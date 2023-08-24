# Task 7
print('*', 2 * '*', 3* '*', 4* '*', 5* '*', sep='\n')

i = 4

while i >= 1:
    print(i * '*')
    i -= 1



# Task 8
num1 = 0
num2 = 1

while num1 <= 50:
    print(num1)
    new_num = num1 + num2
    num1 = num2
    num2 = new_num
    