import random


def user_input():
    numbers = list()
    while True:
        number = int(input('Zahl (0=Ende)? '))
        if number == 0:
            break
        numbers.append(number)
    min_max(numbers)
    return numbers


def random_numbers():
    numbers = random.sample(range(-999, 999), 15)
    min_max(numbers)
    return numbers


def min_max(numbers):
    smallest = 2147483647
    biggest = -2147483648
    for number in numbers:
        if number < smallest:
            smallest = number
        if number > biggest:
            biggest = number
    print(smallest)
    print(biggest)


if __name__ == '__main__':
    user_input()
    random_numbers()
