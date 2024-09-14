'''
    Perfect number is a number that the sum of its divisors(without self value) is equal to itself is called Perfect Number.
'''

num = int(input('Enter a Number: '))


def perfect_num(num):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum = sum + i

    if sum == num:
        print("your number is Perfect")
    else:
        print("is not perfect")


perfect_num(num)
