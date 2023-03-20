def main():
    x = int(input('Input integer number: '))
    while x != 1:
        print(x, end=' -> ')
        if x % 2 == 0:
            x //= 2
        else:
            x = 3 * x + 1
    print(x)

if __name__ == '__main__':
    main()
