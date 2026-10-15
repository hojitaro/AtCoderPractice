def main():
    n, k = map(int, input().split())
    if k <= n + 1:
        print(((k - 1) * (k - 2)) // 2)
    elif n + 2 <= k <= 2 * n:
        print((6 * n * k - 2 * k**2 + 6 * k - 3 * n**2 - 9 * n - 4) // 2)
    elif 2 * n + 1 <= k <= 3 * n:
        print(((3 * n - k + 1) * (3 * n - k + 2)) // 2)
    elif 3 * n + 1 <= k:
        print(0)

if __name__ == '__main__':
    main()

# 模範解答↓
# def c2(x):  # C(x, 2)、x < 2 なら 0
#    return x * (x - 1) // 2 if x >= 2 else 0

#n, k = map(int, input().split())
#s = k - 3
#print(c2(s+2) - 3*c2(s-n+2) + 3*c2(s-2*n+2) - c2(s-3*n+2))