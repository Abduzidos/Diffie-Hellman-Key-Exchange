def main():
    REMOTE_G = 5
    REMOTE_P = 3

    # Getting the G param
    LOCAL_G = int(input(
        'Choose a number between 0 to 99 a index for your G in the prime number table: '))
    while LOCAL_G not in range(0, 99):
        LOCAL_G = int(input(
            'Choose a number between 0 to 99 a index for your G in the prime number table: '))

    # Getting the P param
    LOCAL_P = int(input(
        'Choose a number between 0 to 99 a index for your P in the prime number table: '))
    while LOCAL_P not in range(0, 99):
        LOCAL_P = int(input(
            'Choose a number between 0 to 99 a index for your P in the prime number table: '))

    LOCAL_PRIVATE_KEY = int(input(
        'Choose a number to be your local private key (the little a): '))


if __name__ == "__main__":
    main()
