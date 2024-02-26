for number in range(1, 101):
    is_prime = True

    divider = 2
    while divider <= number ** 0.5 and is_prime:
        is_prime = (number % divider) != 0
        divider += 1

    if is_prime:
        print(f'{number} is prime')