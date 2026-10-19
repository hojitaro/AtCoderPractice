import sys
from itertools import accumulate


def main():
    _input = sys.stdin.readline
    h, w = map(int, _input().split())
    rec = [[*accumulate(map(int, _input().split()))] for _ in range(h)]

    rec_sum = [[0] * (w + 1) for _ in range(h)]
    rec_sum.insert(1, [0, *rec[0]])
    for i in range(1, h):
        for j in range(w):
            rec_sum[i + 1][j + 1] = rec_sum[i][j + 1] + rec[i][j]

    out = []
    q = int(_input())
    for _ in range(q):
        a, b, c, d = map(int, _input().split())
        s1 = rec_sum[c][d]
        s2 = rec_sum[a - 1][d]
        s3 = rec_sum[c][b - 1]
        s4 = rec_sum[a - 1][b - 1]
        out.append(s1 - s2 - s3 + s4)

    print(*out, sep='\n')

if __name__ == '__main__':
    main()
