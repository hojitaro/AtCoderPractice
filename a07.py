# いもす法
from itertools import accumulate


def main():
    d = int(input())
    n = int(input())
    diff = [0] * (d + 1)

    for _ in range(n):
        l, r = map(int, input().split())
        diff[l - 1] += 1
        diff[r] -= 1

    print(*accumulate(diff[:d]), sep='\n')

if __name__ == '__main__':
    main()
