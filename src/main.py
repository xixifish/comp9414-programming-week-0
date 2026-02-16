# Write a Python program that finds all the prime numbers
# between 1 and 1000 (inclusive) and stores them in a list.
def loops_3_1():
    prime_numbers = []
    for i in range(2, 1001):
        is_prime = True

        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(i)
    return prime_numbers


# Write a Python program that counts the number of digits of
# a natural number n, i.e., n is a positive, integer number
def while_3_1(n):
    number_digits = 0
    while n != 0:
        number_digits += 1
        n //= 10  # // divides and keeps only the integer part
    return number_digits


# Write a Python program that takes a user's age as input
# and determine the ticket price for a theme park based on the
# following critieria:
# Children aged 3 and below enter for free
# Children aged 4 to 10 pay $10
# Adults aged 11 to 17 pay $15
# Adults aged 18 to 59 pay $20
# Seniors aged 60 and above pay $12
