def number_pattern(n):
    if not isinstance(n, int):
        return 'Argument must be an integer value.'
    elif n < 1:
        return 'Argument must be an integer greater than 0.'
    else:
        number = [str(n) for n in range(1,n+1)]
        return ' '.join(number)

print(number_pattern(4))