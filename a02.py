def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))

    for a_i in a:
        if a_i == x:
            print('Yes')
            return

    print('No')

if __name__ == '__main__':
    main()
