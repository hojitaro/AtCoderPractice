def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    b = [0]
    for i in range(len(a)):
        b.append(b[i] + a[i])

    out = []
    for i in range(q):
        l_i, r_i = map(int, input().split())
        out.append(b[r_i] - b[l_i - 1])

    print(*out, sep='\n')


if __name__ == '__main__':
    main()
