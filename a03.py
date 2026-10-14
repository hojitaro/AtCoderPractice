# set の検索は平均 O(1) なので、全体で O(N)

def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    q = set(map(int, input().split()))
    
    print('Yes' if any(k - a in q for a in p) else 'No')

if __name__ == '__main__':
    main()
