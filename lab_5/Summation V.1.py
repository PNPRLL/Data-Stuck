def summation(n):
    total = 0
    # วนลูปตั้งแต่ 1 ถึง n
    for i in range(1, n + 1):
        total += i
    return total

def main():
    n = int(input())
    print(summation(n))

main()
