# f'{n:b} はnをbinaryで表現するという意味
# f'{n:010b}　で幅10桁で足りない分は0埋めする。

def main():
    n = int(input())
    print(f'{n:010b}')

if __name__ == '__main__':
    main()
