""" The main module of the min_max program """
import random


def user_input():
    """
    Asks the user for numbers until 0 is entered and then calls min_max with the list of numbers
    :return: a list of numbers entered by the user
    """
    numbers = []
    while True:
        number = int(input('Zahl (0=Ende)? '))
        if number == 0:
            break
        numbers.append(number)
    min_max(numbers)
    return numbers


def random_numbers():
    """
    Generates 15 random numbers between -999 and 999 and calls min_max with the list of numbers
    :return: a list of 15 random numbers
    """
    numbers = random.sample(range(-999, 999), 15)
    min_max(numbers)
    return numbers


def min_max(numbers):
    """
    Prints the smallest and biggest number in the list
    :param numbers: a list of numbers

    """
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
