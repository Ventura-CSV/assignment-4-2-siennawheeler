def main():
    result = []
    a1 = int(input('Enter your first number: '))
    a2 = int(input('Enter your second number: '))
    N = int(input('Enter the number of sequences: '))
    result.append(a1)
    result.append(a2)
    """
    ########################################
    Code Your Program here
    ########################################
    """

    while N <= 2:
        N = int(input('The number of sequences must be greater than two: '))

    total = 0
    x = 2
    while x < N:
        total = a1 + a2
        result.append(total)
        a1 = a2
        a2 = total
        x = x + 1

    print(result)


        
    ########################################
    # Do not delete the return statement
    ########################################
    return result



if __name__ == '__main__':
    main()
